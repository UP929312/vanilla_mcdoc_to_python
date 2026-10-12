"""Validates every vanilla data pack file (from mcmeta's <version>-data-json tag) with vanilla_mcdoc/'s models, for the
version it was generated for, as checks.yml does. Run it from the repo root, after main.py.

python .github/scripts/validate.py

It fails if any file isn't valid, apart from KNOWN_INVALID's, or if one of those is.
"""
import importlib
import io
import json
import re
import sys
import zipfile
from functools import cache
from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import TypeAdapter, ValidationError

from fetch import MCMETA, download, log

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # The repo root, for the generator and vanilla_mcdoc/ (Python only adds this script's folder)
if TYPE_CHECKING:
    from typed_models import BaseSchema

# Vanilla's own files that vanilla-mcdoc gets wrong, so they aren't valid. This says when one is, so it can come off.
# e.g. "data/minecraft/recipe/map_cloning.json": "crafting_transmute's result can leave out its id, to keep the input item"
KNOWN_INVALID: dict[str, str] = {}


def resource_type(resource: str, resources: dict[str, BaseSchema]) -> str | None:
    """The symbol a data pack file is, from its path in its namespace, e.g. ::java::data::recipe::Recipe for
    recipe/stone.json, or None if it isn't a resource type. resources is the minecraft:resource dispatcher."""
    from typed_models import ReferenceSchema, UnionSchema

    if resource.startswith("tags/"):
        return "::java::data::tag::Tag"
    directory = max((key for key in resources if resource.startswith(f"{key}/")), key=len, default=None)  # e.g. worldgen/biome, not worldgen
    if directory is None:
        return None
    branch = resources[directory]
    if isinstance(branch, UnionSchema) and len(branch.members) == 1:  # e.g. chat_type, whose other member is for older versions
        branch = branch.members[0]
    assert isinstance(branch, ReferenceSchema), f"{directory} isn't one named type"
    return branch.path


@cache
def type_adapter(symbol_path: str) -> TypeAdapter[object]:
    """For validating a symbol's data, e.g. TypeAdapter(Recipe) for ::java::data::recipe::Recipe"""
    from utils import symbol_path_to_import_string_and_name

    module, name = symbol_path_to_import_string_and_name(symbol_path)
    return TypeAdapter(getattr(importlib.import_module(module), name))


def invalid_files(archive: zipfile.ZipFile, resources: dict[str, BaseSchema]) -> tuple[int, dict[str, str]]:
    """How many data pack files the zip has, and why each one that isn't valid isn't. resources is the minecraft:resource dispatcher."""
    count = 0
    failures: dict[str, str] = {}
    for name in archive.namelist():
        path = name.partition("/")[2]  # Without the zip's own folder
        # e.g. data/minecraft/recipe/stone.json, or in one of the built-in packs, data/minecraft/datapacks/trade_rebalance/data/...
        if (match := re.fullmatch(r"(?:data/minecraft/datapacks/[^/]+/)?data/[^/]+/(.+\.json)", path)) is None:
            continue
        count += 1
        if (symbol_path := resource_type(match[1], resources)) is None:
            failures[path] = "vanilla-mcdoc doesn't have this resource type"
            continue
        try:
            type_adapter(symbol_path).validate_python(json.loads(archive.read(name)))
        except ValidationError as error:
            first, *others = error.errors()
            failures[path] = f"{'.'.join(map(str, first['loc']))}: {first['msg']}" + (f" (and {len(others)} more)" if others else "")
    return count, failures


def validate() -> None:
    from schema_resolution import get_schema_graph
    from utils import SETTINGS

    minecraft_version: str = importlib.import_module("vanilla_mcdoc").__minecraft_version__
    SETTINGS.minecraft_version = minecraft_version  # So the schema graph has that version's resource types
    log(f"Validating vanilla's data for {minecraft_version}")
    with zipfile.ZipFile(io.BytesIO(download(f"{MCMETA[0]}/archive/refs/tags/{minecraft_version}-data-json.zip"))) as archive:
        count, failures = invalid_files(archive, get_schema_graph().dispatchers["minecraft:resource"])
    unexpected = {path: why for path, why in failures.items() if path not in KNOWN_INVALID}
    valid_now = sorted(KNOWN_INVALID.keys() - failures.keys())
    log(f"{count - len(failures)} of {count} files are valid, and {len(failures) - len(unexpected)} of the rest are known not to be")
    for path, why in sorted(unexpected.items()):
        log(f"  {path}: {why}")
    for path in valid_now:
        log(f"  {path} is valid now (or gone), so take it off KNOWN_INVALID")
    if unexpected or valid_now:
        sys.exit(1)


if __name__ == "__main__":
    validate()
