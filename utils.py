import json
import re
from dataclasses import asdict, dataclass, is_dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Generator

    from typed_models import Attribute, BaseSchema


INDENT = 4
STATIC_SYMBOLS_DIRECTORY = Path("static_symbols")
GENERATED_SYMBOLS_DIRECTORY = Path("vanilla_mcdoc")
SAFE_GUARD_JAVA_NUMBERS = False  # Do we annotate, say, ints to have bounds (e.g. <=2147483647), or just mark them as "int"

# To get the latest of these (pinned to exact upstream commits, which go in upstream.json), run `python ci.py fetch`
with open('symbols.json', 'r', encoding='utf-8') as file:
    SYMBOLS_MAP: dict[str, dict[str, Any]] = json.load(file)
with open('versions.json', 'r', encoding='utf-8') as file:
    VERSION_IDS: list[str] = json.load(file)
# The vanilla-mcdoc and mcmeta commits the two files above came from, if they were fetched by ci.py
UPSTREAM_COMMITS: dict[str, str] = json.loads(Path("upstream.json").read_text(encoding="utf-8")) if Path("upstream.json").exists() else {}

LATEST_VERSION = VERSION_IDS[0]
ROOT_SYMBOLS_KEYS = {object_type: set(keys) for object_type, keys in SYMBOLS_MAP.items()}


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


def get_version_index(version: str) -> int:
    if version in VERSION_IDS:
        return VERSION_IDS.index(version)
    if LATEST_VERSION.startswith(version):  # pragma: no cover
        return 0
    raise TypeError(f"Invalid version: {version}. Must be one of {VERSION_IDS}.")  # pragma: no cover


def symbol_path_to_object_name(path: str) -> str:
    return symbol_path_to_import_string_and_name(path)[1]


def symbol_path_to_import_string_and_name(path: str) -> tuple[str, str]:
    """Turns a symbol path into both it's dot seperated components, and it's leaf/final part
       e.g. ::java::data::worldgen::IntProvider -> data.worldgen.IntProvider & IntProvider
       So we can do things like imports: from generated_symbolds.data.worldgen.IntProvider import IntProvider
    """
    *segments, identifier = path.removeprefix('::java::').split('::')
    module = f"{GENERATED_SYMBOLS_DIRECTORY.name}.{'.'.join(segments)}.{identifier}"
    return module, identifier


def is_valid_with_attributes(attributes: list[Attribute], current_version: str | None = None) -> bool:
    """
    Checks if an object is valid based on its 'since' and 'until' attributes compared to the current_version.
    If the object has no attributes, it is considered valid.
    If the object has a 'since' attribute, it is valid if the current_version is greater than or equal to the 'since' version.
    If the object has an 'until' attribute, it is valid if the current_version is less than or equal to the 'until' version.
    """
    current_index = get_version_index(current_version or SETTINGS.minecraft_version)
    for attr in attributes:
        if attr.name == "until":
            until_version: str = attr.value.value.value  # type: ignore[union-attr, assignment]
            if until_version is not None and current_index <= get_version_index(until_version):  # pragma: no cover
                return False
        elif attr.name == "since":
            since_version: str = attr.value.value.value  # type: ignore[union-attr, assignment]
            if since_version is not None and current_index > get_version_index(since_version):  # pragma: no cover
                return False
        elif attr.name == "deprecated":
            deprecated_version: str | None = attr.value.value.value if attr.value is not None else None  # type: ignore[union-attr, assignment]
            if deprecated_version is None or current_index <= get_version_index(deprecated_version):  # pragma: no cover
                return False
    return True


def iter_child_schemas(value: object) -> Generator[BaseSchema]:
    from typed_models import BaseSchema  # pylint: disable=C0415
    if isinstance(value, BaseSchema):
        yield value
    if isinstance(value, list):
        for item in value:
            yield from iter_child_schemas(item)


def to_json(obj: object) -> str:
    """Converts an object to a JSON string, handling special cases for certain types.
    Also removes None values recursively from dataclasses, dictionaries and lists."""
    return json.dumps(_convert(obj))


def _convert(value: object) -> object:
    """Gets everything into a JSON serializable format, recursively removing None values."""
    if is_dataclass(value) and not isinstance(value, type):
        return _convert(asdict(value))
    if isinstance(value, dict):
        return {k: _convert(v) for k, v in value.items() if v is not None}
    if isinstance(value, (list, tuple)):
        return [_convert(item) for item in value if item is not None]
    return value


def recursively_remove_none(value: object) -> object:
    if isinstance(value, dict):
        return {k: recursively_remove_none(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [recursively_remove_none(item) for item in value if item is not None]
    return value


def resource_path_to_python_path(resource_path: str) -> str:
    path, name = symbol_path_to_import_string_and_name(resource_path)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    return str(output_path)


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
