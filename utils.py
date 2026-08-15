import json
from typing import Any, TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from collections.abc import Generator

    from typed_models import Attribute, BaseSchema

INDENT = 4
GENERATED_SYMBOLS_DIRECTORY = Path("generated_symbols")
SAFE_GUARD_JAVA_NUMBERS = False  # Do we annotate, say, ints to have bounds (e.g. <=2147483647), or just mark them as "int" 

REFETCH_SYMBOLS = False
REFETCH_VERSIONS = False

if REFETCH_SYMBOLS:
    import requests  # type: ignore[import-untyped]

    print("Fetching latest symbols.json from https://raw.githubusercontent.com/SpyglassMC/vanilla-mcdoc/refs/heads/generated/symbols.json")
    response = requests.get("https://raw.githubusercontent.com/SpyglassMC/vanilla-mcdoc/refs/heads/generated/symbols.json")
    response.raise_for_status()
    SYMBOLS_MAP: dict[str, dict[str, Any]] = response.json()

    with open('symbols.json', 'w', encoding='utf-8') as file:
        json.dump(SYMBOLS_MAP, file, indent=4)
else:
    with open('symbols.json', 'r', encoding='utf-8') as file:
        SYMBOLS_MAP = json.load(file)

if REFETCH_VERSIONS:
    import requests

    print("Fetching latest version.json from https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.min.json")
    response = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.min.json")
    response.raise_for_status()
    VERSION_IDS: list[str] = [item["id"] for item in response.json()]

    with open('versions.json', 'w', encoding='utf-8') as file:
        json.dump(VERSION_IDS, file, indent=4)
else:
    with open('versions.json', 'r', encoding='utf-8') as file:
        VERSION_IDS = json.load(file)

LATEST_VERSION = VERSION_IDS[0]
ROOT_SYMBOLS_KEYS = dict({object_type: set(keys) for object_type, keys in SYMBOLS_MAP.items()})


def get_version_index(version: str) -> int:
    if version in VERSION_IDS:
        return VERSION_IDS.index(version)
    if LATEST_VERSION.startswith(version):
        return 0
    raise TypeError(f"Invalid version: {version}. Must be one of {VERSION_IDS}.")


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


def is_valid_with_attributes(attributes: list[Attribute], current_version: str = LATEST_VERSION) -> bool:
    """
    Checks if an object is valid based on its 'since' and 'until' attributes compared to the current_version.
    If the object has no attributes, it is considered valid.
    If the object has a 'since' attribute, it is valid if the current_version is greater than or equal to the 'since' version.
    If the object has an 'until' attribute, it is valid if the current_version is less than or equal to the 'until' version.
    """
    current_index = get_version_index(current_version)
    for attr in attributes or []:
        if attr.name == "until":
            until_version: str = attr.value.value.value  # type: ignore[union-attr, assignment]
            if until_version is not None and current_index <= get_version_index(until_version):
                return False
        elif attr.name == "since":
            since_version: str = attr.value.value.value  # type: ignore[union-attr, assignment]
            if since_version is not None and current_index > get_version_index(since_version):
                return False
        elif attr.name == "deprecated":
            deprecated_version: str | None = attr.value.value.value if attr.value is not None else None  # type: ignore[union-attr, assignment]
            if deprecated_version is None or current_index <= get_version_index(deprecated_version):
                return False
    return True


def iter_child_schemas(value: object) -> Generator[BaseSchema]:
    from typed_models import BaseSchema
    if isinstance(value, BaseSchema):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from iter_child_schemas(item)


def resource_path_to_python_path(resource_path: str) -> str:
    path, name = symbol_path_to_import_string_and_name(resource_path)
    output_path = GENERATED_SYMBOLS_DIRECTORY.joinpath(*path.split(".")[1:-1], name).with_suffix(".py")
    return str(output_path)


def manage_directory_and_inits(path: Path) -> None:
    """Creates the subfolders required, plus the __init__ files too"""
    path.mkdir(parents=True, exist_ok=True)
    current = path
    while current != GENERATED_SYMBOLS_DIRECTORY.parent and current != current.parent:
        init_file = current / "__init__.py"
        if not init_file.exists():
            init_file.parent.mkdir(parents=True, exist_ok=True)
            init_file.write_text("\n", encoding="utf-8")
        current = current.parent


def write_file_if_changed(path: Path, contents: str) -> None:
    old_contents = path.read_text(encoding="utf-8") if path.exists() else None
    if contents != old_contents:
        print("File change detected:", path)
        path.write_text(contents, encoding="utf-8")
