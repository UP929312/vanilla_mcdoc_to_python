import json
from typing import Any, TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from collections.abc import Generator

    from typed_models import Attribute, BaseSchema

INDENT = 4
ROOT_PACKAGE = Path("generated_symbols")

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
    assert path.startswith("::java::")  # Always true.
    segments = path.removeprefix('::java::').split('::')
    assert len(segments) >= 2  # Always true
    # Import from the module file for the referenced symbol (module includes the final name)
    module = f"{ROOT_PACKAGE.name}." + '.'.join(segments)
    return module, segments[-1]


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


def extract_child(model: BaseSchema) -> BaseSchema:
    """For TemplateSchema, get it's child, for everything else, return the input as is"""
    from typed_models import TemplateSchema, UnionSchema, StructSchema
    if not isinstance(model, TemplateSchema):
        return model
    if not isinstance(model.child, UnionSchema):
        return model.child
    # There will always be at least one and only one StructSchema in the union, so we just get it and return.
    return next(member for member in model.child.members if isinstance(member, StructSchema))
