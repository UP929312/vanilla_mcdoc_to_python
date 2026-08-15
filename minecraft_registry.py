import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, Self, cast

from context import Import, SingleSymbolContext
from utils import GENERATED_SYMBOLS_DIRECTORY, iter_child_schemas, manage_directory_and_inits, write_file_if_changed

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
        options = cast(dict[str, Any], dict(value))
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
    words = re.findall(r"[A-Za-z0-9]+", registry)
    identifier = f"Known{''.join(word.capitalize() for word in words)}Id"
    return f"{GENERATED_SYMBOLS_DIRECTORY.name}.registry.{identifier}", identifier


def known_registry_alias(ctx: SingleSymbolContext, id_spec: IdSpec) -> str | None:
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
    output_directory = GENERATED_SYMBOLS_DIRECTORY / "registry"
    manage_directory_and_inits(output_directory)
    for registry in sorted(used_registry_names(schema_graph)):
        entries = schema_graph.dispatchers.get(f"minecraft:{registry}", {})
        if not any(not key.startswith("%") for key in entries):
            continue
        _, identifier = registry_import(registry)
        write_file_if_changed(output_directory / f"{identifier}.py", make_registry_id_file_content(registry, entries))
