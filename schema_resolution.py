from collections.abc import Mapping
from typing import Any

from typed_models import (
    BaseSchema, ConcreteSchema, DispatcherSchema, DynamicIndexSchema, IndexedSchema,
    KIND_TO_MODEL, PairSchema, ReferenceSchema, StringSchema, StructSchema, TemplateSchema,
)


class SchemaGraph:
    def __init__(self, symbols: Mapping[str, BaseSchema], dispatchers: Mapping[str, Mapping[str, BaseSchema]]) -> None:
        self.symbols = dict(symbols)
        self.dispatchers = {name: dict(branches) for name, branches in dispatchers.items()}

    @classmethod
    def from_symbol_maps(cls, symbol_maps: Mapping[str, Mapping[str, Any]]) -> SchemaGraph:
        symbols = {
            path: KIND_TO_MODEL[data["kind"]](**data).remove_version_data()
            for path, data in symbol_maps.get("mcdoc", {}).items()
        }
        dispatchers: dict[str, dict[str, BaseSchema]] = {}
        for name, data in symbol_maps.get("mcdoc/dispatcher", {}).items():
            dispatchers[name] = {
                key: KIND_TO_MODEL[branch["kind"]](**branch).remove_version_data()
                for key, branch in data.items()
                if key != "attribute"
            }
        return cls(symbols, dispatchers)

    def resolve(self, schema: BaseSchema) -> tuple[BaseSchema, ...]:
        """Resolve references and instantiate concrete template applications."""
        if isinstance(schema, ReferenceSchema):
            target = self.symbols.get(schema.path)
            return () if target is None else self.resolve(target)
        if isinstance(schema, ConcreteSchema):
            if isinstance(schema.child, ReferenceSchema):
                target = self.symbols.get(schema.child.path)
                if isinstance(target, TemplateSchema):
                    arguments = dict(zip(
                        (parameter.path for parameter in target.type_params),
                        schema.type_args,
                        strict=False,
                    ))
                    return self.resolve(self._substitute(target.child, arguments))
            return self.resolve(schema.child)
        if isinstance(schema, TemplateSchema):
            return self.resolve(schema.child)
        return (schema,)

    def annotation_candidates(self, schema: DispatcherSchema | IndexedSchema) -> tuple[BaseSchema, ...]:
        """Return every schema that a dispatcher or index can select statically."""
        if isinstance(schema, DispatcherSchema):
            return self._dispatcher_candidates(schema)
        return self._indexed_candidates(schema)

    def _dispatcher_candidates(self, schema: DispatcherSchema) -> tuple[BaseSchema, ...]:
        registry = self.dispatchers.get(schema.registry, {})
        candidates: list[BaseSchema] = []
        for index in schema.parallel_indices:
            if isinstance(index, DynamicIndexSchema) or index.value == "%fallback":
                candidates.extend(registry.values())
                continue
            branch = registry.get(self._normalize_key(index.value), registry.get("%unknown"))
            if branch is not None:
                candidates.append(branch)
        return self._deduplicate(candidates)

    def _indexed_candidates(self, schema: IndexedSchema) -> tuple[BaseSchema, ...]:
        candidates: list[BaseSchema] = []
        for branch in self.annotation_candidates(schema.child):
            for resolved in self.resolve(branch):
                if not isinstance(resolved, StructSchema):
                    continue
                for index in schema.parallelIndices:
                    fields = (
                        [field for field in resolved.fields if isinstance(field, PairSchema)]
                        if isinstance(index, DynamicIndexSchema)
                        else [self._find_struct_field(resolved, self._normalize_key(index.value))]  # type: ignore[list-item]
                    )
                    candidates.extend(field.type for field in fields if field is not None)
        return self._deduplicate(candidates)

    @staticmethod
    def _find_struct_field(schema: StructSchema, key: str) -> PairSchema | None:
        return next(
            (
                field for field in schema.fields
                if isinstance(field, PairSchema)
                and (
                    isinstance(field.key, str) and field.key == key
                    or isinstance(field.key, StringSchema) and (field.key.value is None or field.key.value == key)
                )
            ),
            None,
        )

    @staticmethod
    def _normalize_key(key: str) -> str:
        return key.removeprefix("minecraft:")

    @staticmethod
    def _deduplicate(schemas: list[BaseSchema]) -> tuple[BaseSchema, ...]:
        unique: list[BaseSchema] = []
        seen: set[str] = set()
        for schema in schemas:
            fingerprint = schema.model_dump_json(by_alias=True)
            if fingerprint not in seen:
                seen.add(fingerprint)
                unique.append(schema)
        return tuple(unique)

    @staticmethod
    def _substitute(schema: BaseSchema, mapping: Mapping[str, BaseSchema]) -> BaseSchema:
        def replace(value: object) -> object:
            if isinstance(value, dict):
                if value.get("kind") == "reference" and value.get("path") in mapping:
                    replacement = mapping[str(value["path"])]
                    return replacement.model_dump(by_alias=True)
                return {key: replace(child) for key, child in value.items()}
            if isinstance(value, list):
                return [replace(child) for child in value]
            return value

        data = replace(schema.model_dump(by_alias=True))
        assert isinstance(data, dict)
        return KIND_TO_MODEL[data["kind"]](**data)
