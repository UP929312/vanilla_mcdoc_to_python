import re
from collections.abc import Iterable
from functools import cache
from typing import TYPE_CHECKING

from context import Import, SingleSymbolContext
from static_symbols.minecraft_types import IdSpec
from utils import GENERATED_SYMBOLS_DIRECTORY, manage_directory_and_inits, symbol_path_to_import_string_and_name, symbol_path_to_object_name, write_file_if_changed

if TYPE_CHECKING:
    from schema_resolution import SchemaGraph
    from typed_models import BaseSchema


def resource_symbol(path: str, resources: dict[str, BaseSchema]) -> str | None:
    """The symbol a pack file is, from its path in its namespace without the .json, e.g. ::java::data::recipe::Recipe
    for recipe/stone, or None if it isn't a resource type. resources is the minecraft:resource dispatcher."""
    from typed_models import ReferenceSchema, UnionSchema

    if path.startswith("tags/"):
        return "::java::data::tag::Tag"
    # The type it's in the folder (or is the file) of, the deepest if there's more than one, e.g. lang/deprecated, not lang
    category = max((category for category in resources if path.startswith(f"{category}/") or path == category), key=len, default=None)
    if category is None:
        return None
    branch = resources[category]
    if isinstance(branch, UnionSchema) and len(branch.members) == 1:  # e.g. chat_type, whose other member is for older versions
        branch = branch.members[0]
    assert isinstance(branch, ReferenceSchema), f"{path} isn't one named type"
    return branch.path


def registry_import(registry: str) -> tuple[str, str]:
    """Returns the module and identifier for a given registry name.
    e.g. for the registry "minecraft:biome", this returns:
        ("vanilla_mcdoc.registry.KnownMinecraftBiomeId", "KnownMinecraftBiomeId"). """
    identifier = f"Known{''.join(word.capitalize() for word in re.findall(r"[A-Za-z0-9]+", registry))}Id"
    return f"{GENERATED_SYMBOLS_DIRECTORY.name}.registry.{identifier}", identifier


def known_registry_alias(ctx: SingleSymbolContext, id_spec: IdSpec) -> str | None:
    """Returns the known registry alias for a given IdSpec, if applicable.
    If the IdSpec does not reference a known registry, or if the registry is excluded, this returns None.
    e.g. for the IdSpec with registry="biome", this returns "KnownMinecraftBiomeId". """
    if id_spec.registry is None or id_spec.exclude:
        return None
    registry = ctx.schema_graph.dispatchers.get(f"minecraft:{id_spec.registry}", {})
    if not registry or not any(not key.startswith("%") for key in registry):
        # Reject empty registries or those containing only fallback entries like %unknown.
        # Only registries with concrete (non-%) IDs get a type alias generated.
        return None
    module, identifier = registry_import(id_spec.registry)
    ctx.required_imports.add(Import(module, identifier, not ctx.require_runtime_imports))
    return identifier


def make_registry_id_file_content(registry: str, keys: Iterable[str]) -> str:
    """Creates the content of vanilla_mcdoc/registry/<x>.py for a given registry name and its known keys."""
    _, identifier = registry_import(registry)
    values = sorted(f"minecraft:{key}" for key in keys if not key.startswith("%"))
    return "\n".join([
        '"""Known built-in IDs for a generated registry."""',
        "from typing import Literal",
        "",
        f"type {identifier} = Literal[",
        *(f"    {value!r}," for value in values),
        "]",
        "",
    ])


def used_registry_names(schema_graph: SchemaGraph) -> set[str]:
    """Returns a set of all registry *names/keys* used in the schema graph."""
    from typed_models import StringSchema

    registries: set[str] = set()

    def collect(schema: BaseSchema) -> None:
        if isinstance(schema, StringSchema):
            registries.update(
                spec.registry
                for attribute in schema.attributes
                if (spec := attribute.to_id_spec()) is not None and spec.registry is not None
            )
        for child in schema.child_schemas():
            collect(child)

    for schema in schema_graph.symbols.values():
        collect(schema)
    return registries


def make_registry_id_files(schema_graph: SchemaGraph) -> None:
    """Makes all the vanilla_mcdoc/registry/<x>.py files for all known registries used in the schema graph."""
    manage_directory_and_inits(GENERATED_SYMBOLS_DIRECTORY / "registry")
    for registry in sorted(used_registry_names(schema_graph)):
        entries = schema_graph.dispatchers.get(f"minecraft:{registry}")
        if not entries or not any(not key.startswith("%") for key in entries):
            # Reject empty registries or those containing only fallback entries like %unknown.
            # Only registries with concrete (non-%) IDs get a type alias generated.
            continue
        write_file_if_changed(
            GENERATED_SYMBOLS_DIRECTORY / "registry" / f"{registry_import(registry)[1]}.py",
            make_registry_id_file_content(registry, entries),
        )


def make_root_resource_registry_content(symbol_paths: Iterable[str]) -> str:
    """Makes the root instance so that things using this library can check if it's a root resource,
    or if it's a "fragment", e.g. a FoodPredicate is a fragment, but the Predicate is the root resource."""
    root_paths = sorted(set(symbol_paths) & get_resource_lookup_map().keys())
    datapack_paths = [symbol_path for symbol_path in root_paths if symbol_path.startswith("::java::data::")]
    pack_paths     = [symbol_path for symbol_path in root_paths if symbol_path.startswith("::java::assets::")]  # fmt: skip

    lines = [
        '"""Generated root-resource registry for datapack and resource-pack classes."""',
        "",
        "\n".join(
            f"from {symbol_path_to_import_string_and_name(symbol_path)[0]} import {symbol_path_to_object_name(symbol_path)}"
            for symbol_path in datapack_paths + pack_paths
        ),
        "",
        "ROOT_DATAPACK_CLASSES = (",
            "\n".join(f"    {symbol_path_to_object_name(symbol_path)}," for symbol_path in datapack_paths),  # noqa: E131
        ")",
        "",
        "ROOT_RESOURCE_PACK_CLASSES = (",
            "\n".join(f"    {symbol_path_to_object_name(symbol_path)}," for symbol_path in pack_paths),
        ")",
        "",
        "",
    ]
    return "\n".join(lines)


def make_root_resource_registry_file(symbol_paths: Iterable[str]) -> None:
    """Simple helper function, makes the vanilla_mcdoc/root_resource_registry.py
    file for the symbol paths"""
    write_file_if_changed(
        GENERATED_SYMBOLS_DIRECTORY / "root_resource_registry.py",
        make_root_resource_registry_content(symbol_paths),
    )


@cache
def get_resource_lookup_map() -> dict[str, str]:
    """Build and cache the root-resource lookup once, shared across the project."""
    from schema_resolution import get_schema_graph
    from typed_models import DispatcherSpread, ReferenceSchema, StructSchema, TemplateSchema

    schema_graph = get_schema_graph()  # The same one the rest of generation uses
    template_paths = {path for path, schema in schema_graph.symbols.items() if isinstance(schema, TemplateSchema)}
    base_map: dict[str, str] = {}

    # Only the resources that exist in the version we're generating for (the graph drops the others)
    for resource_key, model_value in schema_graph.dispatchers["minecraft:resource"].items():
        for reference_path in ReferenceSchema.collect_reference_paths(model_value, template_paths):
            base_map[reference_path] = resource_key

        if not isinstance(model_value, ReferenceSchema):
            continue
        root_schema = schema_graph.symbols.get(model_value.path)
        spread = DispatcherSpread.of(root_schema, schema_graph) if isinstance(root_schema, StructSchema) else None
        if spread is None or spread.field is not None:  # Only a spread's branches are part of the resource itself
            continue

        for branch_schema in schema_graph.dispatchers[spread.dispatcher.registry].values():
            if isinstance(branch_schema, ReferenceSchema):
                base_map[branch_schema.path] = resource_key
            for reference_path in ReferenceSchema.collect_reference_paths(branch_schema, template_paths):
                base_map[reference_path] = resource_key

    return base_map
