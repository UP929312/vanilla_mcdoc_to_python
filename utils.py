import json
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from typed_models import Attribute


STATIC_SYMBOLS_DIRECTORY = Path("static_symbols")
GENERATED_SYMBOLS_DIRECTORY = Path("vanilla_mcdoc")
SAFE_GUARD_JAVA_NUMBERS = False  # Do we annotate, say, ints to have bounds (e.g. <=2147483647), or just mark them as "int"

# To get the latest of these (pinned to exact upstream commits, which go in upstream.json), run `python .github/scripts/fetch.py`
with open('symbols.json', 'r', encoding='utf-8') as file:
    SYMBOLS_MAP: dict[str, dict[str, Any]] = json.load(file)
with open('versions.json', 'r', encoding='utf-8') as file:
    VERSION_IDS: list[str] = json.load(file)
# Every registry's entries (e.g. all the loot condition types) for one Minecraft version: `python .github/scripts/fetch.py version <version>`
with open('registries.json', 'r', encoding='utf-8') as file:
    REGISTRIES_FILE: dict[str, Any] = json.load(file)
REGISTRIES_VERSION: str = REGISTRIES_FILE["minecraft_version"]
REGISTRIES: dict[str, list[str]] = REGISTRIES_FILE["registries"]
# Vanilla's own data pack and resource pack files (mcmeta's <version>-data-json and -assets-json tags), for
# vanilla_mcdoc.vanilla. They're about 25 MB, so `python .github/scripts/fetch.py vanilla` downloads them, rather than them being committed
VANILLA_ZIPS = [Path("mcmeta/data-json.zip"), Path("mcmeta/assets-json.zip")]
# The vanilla-mcdoc and mcmeta commits symbols.json and versions.json came from, if they were fetched by .github/scripts/fetch.py
UPSTREAM_COMMITS: dict[str, str] = json.loads(Path("upstream.json").read_text(encoding="utf-8")) if Path("upstream.json").exists() else {}

LATEST_VERSION = VERSION_IDS[0]


def name_inline_resources(symbols_map: dict[str, dict[str, Any]]) -> None:
    """Most of vanilla-mcdoc's resource types refer to a named type (e.g. recipe is ::java::data::recipe::Recipe), but a
    few are written inline, e.g. world_clock is just `struct {}`, so would have no class of their own. Give each a symbol
    named after its directory, e.g. ::java::data::world_clock::WorldClock, which the resource refers to instead."""
    resources = symbols_map["mcdoc/dispatcher"]["minecraft:resource"]
    for directory, schema in resources.items():
        if schema["kind"] == "reference" or (schema["kind"] == "union" and all(member["kind"] == "reference" for member in schema["members"])):
            continue  # Already named (or one named type per version, e.g. chat_type is OldChatType until 1.19.1, then ChatType)
        name = "".join(part.capitalize() for part in directory.split("/")[-1].split("_"))  # e.g. world_clock -> WorldClock
        path = f"::java::data::{directory.replace('/', '::')}::{name}"
        symbols_map["mcdoc"][path] = schema
        resources[directory] = {"kind": "reference", "path": path, "attributes": schema.get("attributes", [])}


name_inline_resources(SYMBOLS_MAP)
ROOT_SYMBOLS_KEYS = {object_type: set(keys) for object_type, keys in SYMBOLS_MAP.items()}  # After, so it has those symbols too


@dataclass
class Settings:
    """Options for one generation run. main.py sets these from its command line arguments, before anything gets parsed."""
    minecraft_version: str = LATEST_VERSION  # Which version to generate for, symbols.json has since/until attributes for every version
    include_model_dump: bool = True  # The raw symbols.json data at the bottom of each file, handy for development


SETTINGS = Settings()


def minecraft_to_python_version(version: str) -> str:
    """Turn a Minecraft version into a Python package version (PEP 440), so pip orders them like Minecraft does, e.g.
    26.3 -> 26.3.0, 26.4-snapshot-3 -> 26.4.0a3, 26.4-pre-1 -> 26.4.0b1, 26.4-rc-1 -> 26.4.0rc1 (pip skips the last 3 unless --pre)"""
    match = re.fullmatch(r"(\d+)\.(\d+)(?:\.(\d+))?(?:-(snapshot|pre|rc)-?(\d+))?", version)
    if match is None:
        raise ValueError(f"Can't turn {version} into a Python package version (old style snapshots like 25w14a aren't supported)")
    major, minor, patch, stage, number = match.groups()
    stage_letters = {"snapshot": "a", "pre": "b", "rc": "rc"}  # i.e. alpha, beta, release candidate
    suffix = f"{stage_letters[stage]}{number}" if stage else ""
    return f"{major}.{minor}.{patch or 0}{suffix}"


def zip_version(path: Path) -> str | None:
    """Which Minecraft version one of VANILLA_ZIPS is for, from its folder (e.g. mcmeta-26.3-data-json/), or None if it isn't there."""
    if not path.exists():
        return None
    with zipfile.ZipFile(path) as archive:
        match = re.fullmatch(r"mcmeta-(.+)-(?:data|assets)-json", archive.namelist()[0].split("/")[0])
    return match[1] if match else None


def version_problem(version: str) -> str | None:
    """Why vanilla_mcdoc can't be generated for this Minecraft version (e.g. registries.json being another one's), or None if it can."""
    if version not in VERSION_IDS:
        return f"Unknown Minecraft version {version!r}, see versions.json"
    try:
        minecraft_to_python_version(version)  # It has to be able to be a package version, e.g. 25w14a can't
    except ValueError as error:
        return str(error)
    if version != REGISTRIES_VERSION:
        return f"registries.json is for {REGISTRIES_VERSION}, run `python .github/scripts/fetch.py version {version}` first"
    if any(zip_version(path) != version for path in VANILLA_ZIPS):
        return f"mcmeta/ doesn't have vanilla's files for {version}, run `python .github/scripts/fetch.py vanilla` first"
    return None


def get_version_index(version: str) -> int:
    if version in VERSION_IDS:
        return VERSION_IDS.index(version)
    if LATEST_VERSION.startswith(version):  # pragma: no cover
        return 0
    raise TypeError(f"Invalid version: {version}. Must be one of {VERSION_IDS}.")  # pragma: no cover


def symbol_path_to_import_string_and_name(path: str) -> tuple[str, str]:
    """Turns a symbol path into both it's dot separated components, and it's leaf/final part
       e.g. ::java::data::worldgen::IntProvider -> data.worldgen.IntProvider & IntProvider
       So we can do things like imports: from generated_symbolds.data.worldgen.IntProvider import IntProvider
    """
    *segments, identifier = path.removeprefix('::java::').split('::')
    module = f"{GENERATED_SYMBOLS_DIRECTORY.name}.{'.'.join(segments)}.{identifier}"
    return module, identifier


def symbol_path_to_object_name(path: str) -> str:
    return symbol_path_to_import_string_and_name(path)[1]


# Every symbol's class or alias name. Names made up for helper classes avoid these, even if their file doesn't import
# that symbol: Processor's `rule` variant would otherwise be ProcessorRule, a real symbol, and as its parent class Rule
# has `rules: list[ProcessorRule]` (which pydantic reads in the variant's file), each rule would be read as a processor.
SYMBOL_NAMES = {symbol_path_to_object_name(path) for path in ROOT_SYMBOLS_KEYS["mcdoc"]}


# TODO: Move this to BaseSchema
def is_valid_with_attributes(attributes: list[Attribute], current_version: str | None = None) -> bool:
    """
    Checks if an object is valid based on its 'since' and 'until' attributes compared to the current_version.
    If the object has no attributes, it is considered valid.
    If the object has a 'since' attribute, it is valid if the current_version is greater than or equal to the 'since' version.
    If the object has an 'until' attribute, it is valid if the current_version is before the 'until' version.
    Deprecated things still are, as the game still accepts them (Spyglass just warns), e.g. vanilla's models still use the old rotations.
    """
    current_index = get_version_index(current_version or SETTINGS.minecraft_version)
    for attr in attributes:
        if attr.name == "until" and current_index <= get_version_index(str(attr.plain_value)):  # pragma: no cover
            return False
        if attr.name == "since" and current_index > get_version_index(str(attr.plain_value)):  # pragma: no cover
            return False
        # if attr.name == "deprecated" and current_index >= get_version_index(str(attr.plain_value)):  # pragma: no cover
        #     return False
    return True


def resource_path_to_python_path(resource_path: str) -> Path:
    path, name = symbol_path_to_import_string_and_name(resource_path)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    return output_path


def manage_directory_and_inits(path: Path) -> None:
    """Creates the subfolders required, plus the __init__ files too"""
    path.mkdir(parents=True, exist_ok=True)
    current = path
    while current not in {GENERATED_SYMBOLS_DIRECTORY.parent, current.parent}:
        init_file = current / "__init__.py"
        if not init_file.exists():  # pragma: no cover
            init_file.parent.mkdir(parents=True, exist_ok=True)
            init_file.write_text("\n", encoding="utf-8")
        current = current.parent


def write_file_if_changed(path: Path, contents: str) -> None:
    old_contents = path.read_text(encoding="utf-8") if path.exists() else None
    if contents != old_contents:  # pragma: no cover
        print("File change detected:", path)
        path.write_text(contents, encoding="utf-8")
