from typing import Any

from typed_models import (
    BaseSchema, ConcreteSchema, ConcreteSchemaTypeArgTypes, DispatcherSchema, DynamicIndexSchema, IndexedSchema,
    KIND_TO_MODEL, PairSchema, ReferenceSchema, SpreadFieldSchema, StructSchema, TemplateSchema,
)


class SchemaGraph:
    def __init__(self, symbols: dict[str, BaseSchema], dispatchers: dict[str, dict[str, BaseSchema]]) -> None:
        self.symbols = symbols
        self.dispatchers = dispatchers

    @classmethod
    def from_symbol_maps(cls, symbol_maps: dict[str, dict[str, Any]]) -> SchemaGraph:
        symbols = {
            path: KIND_TO_MODEL[data["kind"]](**data).remove_version_data()
            for path, data in symbol_maps.get("mcdoc", {}).items()
        }
        dispatchers: dict[str, dict[str, BaseSchema]] = {}
        for name, data in symbol_maps.get("mcdoc/dispatcher", {}).items():
            dispatchers[name] = {
                key: KIND_TO_MODEL[branch["kind"]](**branch)
                for key, branch in data.items()
                if key != "attribute"
            }
        return cls(symbols, dispatchers)

    def resolve(self, schema: BaseSchema) -> BaseSchema:
        """Resolve references and instantiate concrete template applications."""
        if isinstance(schema, ReferenceSchema):
            return self.resolve(schema=self.symbols[schema.path])
        if isinstance(schema, ConcreteSchema):
            if isinstance(schema.child, ReferenceSchema):
                target: TemplateSchema = self.symbols[schema.child.path]  # type: ignore[assignment]
                arguments = dict(zip(
                    (parameter.path for parameter in target.type_params),
                    schema.type_args,
                ))
                return self.resolve(self._substitute(target.child, arguments))
            return self.resolve(schema.child)
        return schema

    def is_runtime_class(self, schema: BaseSchema) -> bool:
        """Whether a schema renders as one class that can be inherited."""
        if isinstance(schema, ConcreteSchema):
            return self.is_runtime_class(self.resolve(schema))
        if isinstance(schema, ReferenceSchema):
            target = self.symbols.get(schema.path)
            return target is None or self.is_runtime_class(target)
        if not isinstance(schema, StructSchema):
            return False
        if schema._mapping_pair() is not None or schema._spread_dispatcher() is not None:
            return False
        return all(
            not isinstance(field, SpreadFieldSchema) or self.is_runtime_class(field.type)
            for field in schema.fields
        )

    def annotation_candidates(self, schema: DispatcherSchema | IndexedSchema) -> tuple[BaseSchema, ...]:
        """Return every schema that a dispatcher or index can select statically."""
        if isinstance(schema, DispatcherSchema):
            return self._dispatcher_candidates(schema)
        return self._indexed_candidates(schema)

    def instantiate(self, schema: TemplateSchema, arguments: list[ConcreteSchemaTypeArgTypes]) -> BaseSchema:
        mapping = dict(zip((parameter.path for parameter in schema.type_params), arguments, strict=False))
        return self._substitute(schema.child, mapping)

    def _dispatcher_candidates(self, schema: DispatcherSchema) -> tuple[BaseSchema, ...]:
        registry = self.dispatchers.get(schema.registry, {})
        assert isinstance(schema.parallel_indices[0], DynamicIndexSchema) or schema.parallel_indices[0].value == "%fallback"
        return self._deduplicate(list(registry.values()))

    def _indexed_candidates(self, schema: IndexedSchema) -> tuple[BaseSchema, ...]:
        candidates: list[BaseSchema] = []
        for branch in self.annotation_candidates(schema.child):
            resolved = self.resolve(branch)
            assert isinstance(resolved, StructSchema)
            fields = (
                [field for field in resolved.fields if isinstance(field, PairSchema)]
                if isinstance(schema.parallel_indices[0], DynamicIndexSchema)
                else [self._find_struct_field(resolved, schema.parallel_indices[0].value.removeprefix("minecraft:"))]
            )
            candidates.extend(field.type for field in fields)
        return self._deduplicate(candidates)

    @staticmethod
    def _find_struct_field(schema: StructSchema, key: str) -> PairSchema:
        return next(field for field in schema.fields if isinstance(field, PairSchema) and field.key == key)

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
    def _substitute(schema: BaseSchema, mapping: dict[str, ConcreteSchemaTypeArgTypes]) -> BaseSchema:
        """Recursively replace references to type parameters with concrete types."""
        def replace(value: object) -> object:
            if isinstance(value, dict):
                if value.get("kind") == "reference" and value.get("path") in mapping:
                    replacement = mapping[value["path"]]
                    return replacement.model_dump(by_alias=True)
                return {key: replace(child) for key, child in value.items()}
            if isinstance(value, list):
                return [replace(child) for child in value]
            return value

        data: dict[str, Any] = replace(schema.model_dump(by_alias=True))  # type: ignore[assignment]
        return KIND_TO_MODEL[data["kind"]](**data)
