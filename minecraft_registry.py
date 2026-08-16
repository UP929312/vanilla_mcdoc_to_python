import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, Self

from context import Import, SingleSymbolContext
from utils import GENERATED_SYMBOLS_DIRECTORY, SYMBOLS_MAP, iter_child_schemas, manage_directory_and_inits, symbol_path_to_import_string_and_name, symbol_path_to_object_name, write_file_if_changed

if TYPE_CHECKING:
    from schema_resolution import SchemaGraph
    from typed_models import BaseSchema


@dataclass(frozen=True, slots=True)
class IdSpec:
    registry: str | None = None
    tags: Literal["allowed", "implicit", "required"] | None = None
    definition: bool = False
    prefix: Literal["!"] | None = None
    path: str | None = None
    empty: Literal["allowed"] | None = None
    exclude: tuple[str, ...] = ()

    @classmethod
    def from_value(cls, value: str | Mapping[str, Any] | None) -> Self:
        if value is None:
            return cls()
        if isinstance(value, str):
            return cls(registry=value)
        options = dict(value)
        if exclude := options.get("exclude"):
            options["exclude"] = (exclude,) if isinstance(exclude, str) else tuple(exclude)
        return cls(**options)

    def to_annotation(self) -> str:
        values: list[tuple[str, object]] = [
            ("registry", self.registry),
            ("tags", self.tags),
            ("definition", self.definition if self.definition else None),
            ("prefix", self.prefix),
            ("path", self.path),
            ("empty", self.empty),
            ("exclude", self.exclude if self.exclude else None),
        ]
        arguments = ", ".join(f"{name}={value!r}" for name, value in values if value is not None)
        return f"IdSpec({arguments})"


def registry_import(registry: str) -> tuple[str, str]:
    """Returns the module and identifier for a given registry name.
    e.g. for the registry "minecraft:biome", this returns:
        ("generated_symbols.registry.KnownMinecraftBiomeId", "KnownMinecraftBiomeId"). """
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
    ctx.required_imports.add(Import(module, identifier, not ctx.require_runtime_imports, False))
    return identifier


def make_registry_id_file_content(registry: str, keys: Iterable[str]) -> str:
    """Creates the content of generated_symbols/registry/<x>.py for a given registry name and its known keys."""
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
        for field_name in type(schema).model_fields:
            for child in iter_child_schemas(getattr(schema, field_name)):
                collect(child)

    for schema in schema_graph.symbols.values():
        collect(schema)
    return registries


def make_registry_id_files(schema_graph: SchemaGraph) -> None:
    """Makes all the generated_symbols/registry/<x>.py files for all known registries used in the schema graph."""
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
    datapack_paths = sorted({
        symbol_path for symbol_path in symbol_paths
        if get_resource_lookup_map().get(symbol_path) is not None and symbol_path.startswith("::java::data::")
    })
    pack_paths = sorted({
        symbol_path for symbol_path in symbol_paths
        if get_resource_lookup_map().get(symbol_path) is not None and symbol_path.startswith("::java::assets::")
    })

    lines = [
        '"""Generated root-resource registry for datapack and resource-pack classes."""',
        "",
        "\n".join(
            f"from {symbol_path_to_import_string_and_name(symbol_path)[0]} import {symbol_path_to_object_name(symbol_path)}"
            for symbol_path in datapack_paths + pack_paths
        ),
        "",
        "root_datapack_classes = (",
            "\n".join(f"    {symbol_path_to_import_string_and_name(symbol_path)[1]}," for symbol_path in datapack_paths),
        ")",
        "",
        "root_resource_pack_classes = (",
            "\n".join(f"    {symbol_path_to_import_string_and_name(symbol_path)[1]}," for symbol_path in pack_paths),
        ")",
        "",
        "",
    ]
    return "\n".join(lines)


def make_root_resource_registry_file(symbol_paths: Iterable[str]) -> None:
    """Simple helper function, makes the generated_symbols/root_resource_registry.py
    file for the symbol paths"""
    write_file_if_changed(
        GENERATED_SYMBOLS_DIRECTORY / "root_resource_registry.py",
        make_root_resource_registry_content(symbol_paths),
    )


_RESOURCE_LOOKUP_MAP: dict[str, str] | None = None


def get_resource_lookup_map() -> dict[str, str]:
    """Build and cache the root-resource lookup once, shared across the project."""
    global _RESOURCE_LOOKUP_MAP
    if _RESOURCE_LOOKUP_MAP is None:
        from schema_resolution import SchemaGraph
        from typed_models import KIND_TO_MODEL, ReferenceSchema, StructSchema, TemplateSchema

        schema_graph = SchemaGraph.from_symbol_maps(SYMBOLS_MAP)
        template_paths = {path for path, schema in schema_graph.symbols.items() if isinstance(schema, TemplateSchema)}
        base_map: dict[str, str] = {}

        for resource_key, raw_value in SYMBOLS_MAP["mcdoc/dispatcher"]["minecraft:resource"].items():
            model_value = KIND_TO_MODEL[raw_value["kind"]](**raw_value)
            for reference_path in ReferenceSchema.collect_reference_paths(model_value, template_paths):
                base_map[reference_path] = resource_key

            if "path" not in raw_value:
                continue
            root_schema = schema_graph.symbols.get(raw_value["path"])
            dispatcher_spread = root_schema._dispatcher_spread() if isinstance(root_schema, StructSchema) else None
            if dispatcher_spread is None or dispatcher_spread[2] != "type":
                continue

            for branch_schema in schema_graph.dispatchers[dispatcher_spread[1].registry].values():
                if isinstance(branch_schema, ReferenceSchema):
                    base_map[branch_schema.path] = resource_key
                for reference_path in ReferenceSchema.collect_reference_paths(branch_schema, template_paths):
                    base_map[reference_path] = resource_key

        _RESOURCE_LOOKUP_MAP = base_map
    return _RESOURCE_LOOKUP_MAP

