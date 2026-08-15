from typing import Annotated, ClassVar, Literal, Self

from pydantic import BaseModel, Field, RootModel, model_validator

from context import Import, SingleSymbolContext
from minecraft_registry import IdSpec, known_registry_alias
from utils import ROOT_SYMBOLS_KEYS, SAFE_GUARD_JAVA_NUMBERS, symbol_path_to_import_string_and_name, symbol_path_to_object_name, is_valid_with_attributes, iter_child_schemas


class BaseSchema(BaseModel):
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def contains_inline_struct(self) -> bool:
        """Return whether this schema needs a generated name for an inline struct."""
        return False

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        """Render an annotation, using a nested declaration name when supported."""
        return self.to_annotation(ctx)

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        """Generate the actual Python, for most things, this is just the alias to the annotation"""
        return [f"type {class_name} = {self.to_annotation(ctx)}"]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        raise NotImplementedError(f"This should never get called directly on a {self.__class__.__name__}")

    def remove_version_data(self) -> BaseSchema:
        self.attributes = [x for x in self.attributes if x.name not in {"since", "until", "deprecated"}]
        for field_name in type(self).model_fields:
            for child in iter_child_schemas(getattr(self, field_name)):
                child.remove_version_data()
        return self


class Attribute(BaseModel):
    """Represents a single attribute with a name and a structured value."""
    name: str
    value: Annotated[LiteralSchema | TreeSchema | DispatcherSchema | ReferenceSchema, Field(discriminator="kind")] | None = None

    def to_id_spec(self) -> IdSpec | None:
        if self.name != "id":
            return None
        value: str | dict | None = self._attribute_value(self.value)  # type: ignore[assignment, type-arg]
        return IdSpec.from_value(value)

    @classmethod
    def _attribute_value(cls, schema: LiteralSchema | TreeSchema | DispatcherSchema | ReferenceSchema | None) -> object:
        if schema is None:
            return None
        if isinstance(schema, LiteralSchema):
            return schema.value.value
        # TreeSchemas:
        assert not isinstance(schema, (DispatcherSchema, ReferenceSchema))
        values = {key: cls._attribute_value(value) for key, value in schema.values.root.items()}
        return tuple(values[key] for key in sorted(values, key=int)) if values and all(key.isdigit() for key in values) else values


class ValueRange(BaseModel):
    """Represents a numeric range, used in `int`, `float`, and array lengths."""
    kind: Literal[0, 2] = Field(default = 0, repr=False)
    min: float | int  # Min is *always* set
    max: float | int | None = None

    def to_annotation(self, ctx: SingleSymbolContext, value_range_type: Literal["int", "float"], attributes: list[Attribute]) -> str:
        if self.max is not None:
            parts = ["Range", f"`{self.min or '0'}`-`{self.max or '0'}`", "both inclusive"]
        else:
            parts = ["Range", f"Min `{self.min or '0'}` and above", "inclusive"]
        if self.extract_divisible_by_value(attributes):
            parts.append(f"divisible by {self.extract_divisible_by_value(attributes)}")
        ctx.require_annotated()
        return f"Annotated[{value_range_type}, '{' | '.join(parts)}']"

    def extract_divisible_by_value(self, attributes: list[Attribute]) -> str | None:
        attribute = next((attr for attr in attributes if attr.name == "divisible_by"), None)
        if attribute is None:
            return None
        value = Attribute._attribute_value(attribute.value)
        return None if value is None else str(value)


class LengthRange(BaseModel):
    kind: Literal[0] = Field(default=0, repr=False)  # Not sure what other values this can be?
    min: int | None = None  # Only like one of these has a max but no min...
    max: int | None = None

    def to_annotation_suffix(self) -> str:
        if self.min is not None and self.max is not None:
            if self.min == self.max:
                return f"Length = {self.min}"
            return f"Length = {self.min}-{self.max} (both inclusive)"
        if self.min is not None:
            return f"Length = {self.min} (inclusive) and above"
        if self.max is not None:
            return f"Length = up to {self.max} (inclusive)"
        raise TypeError("Min and Max are None! LengthRange.to_annotation_suffix error")


class EnumValue(BaseModel):
    identifier: str
    value: str | int | float | bool
    description: str = Field(default="", repr=False, alias="desc")

    def to_annotation(self) -> str:
        return f"{repr(self.value).replace('\'', '\"')}"  # This fixes it so strings are handled properly

    @property
    def description_comment_or_empty(self) -> str:
        return f"  # {self.description.replace('\\\n', '\n').replace('\n', ' ').strip()}" if self.description else ""


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


class LiteralSchema(BaseSchema):
    """Represents a literal value, often found inside an Attribute's value.
    Also normally used to just set until/since version (80% + of cases)
    """
    kind: Literal["literal"] = Field(repr=False)
    value: Annotated[StringSchema | IntSchema | BooleanSchema | FloatSchema, Field(discriminator="kind")]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        ctx.required_imports.add(Import("typing", "Literal", False, True))
        return f"Literal[{self.value.value!r}]"


# ==================================================================================================================================
# Primitive Schemas (string, int, float, boolean, etc.)


class IntSchema(BaseSchema):
    """A signed 32-bit integer, ranging from -2,147,483,648 to 2,147,483,647 (inclusive)"""
    kind: Literal["int"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: Literal[-1, 0, 1, 3, 16, 20, 90, 180, 270, 32500] | None = None  # This is for speed, but should probably go back to int.

    min_value_internally: int = -2_147_483_648
    max_value_internally: int = 2_147_483_647

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.value_range:
            return self.value_range.to_annotation(ctx, "int", self.attributes)
        if SAFE_GUARD_JAVA_NUMBERS:
            copied_schema = self.model_copy(update={
                "value_range": ValueRange(min=self.min_value_internally, max=self.max_value_internally),
            })
            return copied_schema.to_annotation(ctx)
        return "int"

    @classmethod
    def _to_annotation_with_bounds(
        cls, ctx: SingleSymbolContext, original_object: ByteSchema | ShortSchema | LongSchema,
        min_value: int, max_value: int
    ) -> str:
        """Purpose of this is so other things like bytes, shorts, longs, etc can call it to get a easier method"""
        int_schema = cls(
            kind="int",
            attributes=original_object.attributes,
            valueRange=original_object.value_range,
            min_value_internally=min_value,
            max_value_internally=max_value,
        )
        return int_schema.to_annotation(ctx)


class StringSchema(BaseSchema):
    kind: Literal["string"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value: str | None = None  # For literal strings

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        id_spec = next((spec for attribute in self.attributes if (spec := attribute.to_id_spec()) is not None), None)
        metadata: list[str] = []
        if id_spec is not None:
            ctx.required_imports.add(Import("minecraft_registry", "IdSpec", False, False))
            metadata.append(id_spec.to_python_code())

        # Return Annotated[str, <x>] if length range present:
        if self.length_range is not None:
            if self.length_range.min == 0 and self.length_range.max == 0:
                # Edge case, because of this stuff:
                # https://github.com/SpyglassMC/vanilla-mcdoc/blob/main/java/assets/credits.mcdoc#L5
                # https://github.com/misode/mcmeta/blob/assets/assets/minecraft/texts/credits.json#L1998
                # Literally only one thing - ::java::assets::credits::CreditsDiscipline
                ctx.required_imports.add(Import("typing", "Literal", False, True))
                return 'Literal[""]'
            ctx.require_annotated()
            metadata.insert(0, repr(self.length_range.to_annotation_suffix()))

        if not metadata:
            return "str"
        ctx.require_annotated()
        annotation = f"Annotated[str, {', '.join(metadata)}]"
        known_id_alias = known_registry_alias(ctx, id_spec) if id_spec is not None else None
        return f"{annotation} | {known_id_alias}" if known_id_alias is not None else annotation


class FloatSchema(BaseSchema):
    """
    Float - A 32-bit, single-precision floating-point number, ranging from -3.4E38 to +3.4E38.
    Double - A 64-bit, double-precision floating-point, ranging from -1.79E308 to +1.79E308.
    """
    kind: Literal["float", "double"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: float | None = None  # For literal floats (not used in the symbols yet)

    min_value_internally: tuple[float, float] = (-3.4E38, -1.79E308)
    max_value_internally: tuple[float, float] = (3.4E38, 1.79E308)

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.value_range:
            return self.value_range.to_annotation(ctx, "float", self.attributes)
        if SAFE_GUARD_JAVA_NUMBERS:
            fake_value_range = ValueRange(
                min=self.min_value_internally[0 if self.kind == "float" else 1],
                max=self.max_value_internally[0 if self.kind == "float" else 1],
            )
            return FloatSchema(kind=self.kind, attributes=self.attributes, valueRange=fake_value_range).to_annotation(ctx)
        return "float"


class BooleanSchema(BaseSchema):
    kind: Literal["boolean"] = Field(repr=False)
    value: bool | None = None

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return "bool"


class ShortSchema(BaseSchema):
    """A signed 16-bit integer, ranging from -32,768 to 32,767 (inclusive)."""
    kind: Literal["short"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: int | None = None  # For literal shorts (not used in the symbols yet)

    min_value_internally: int = -32_768
    max_value_internally: int = 32_767

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self, self.min_value_internally, self.max_value_internally)


class LongSchema(BaseSchema):
    """A signed 64-bit integer, ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (inclusive)."""
    kind: Literal["long"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: int | None = None  # For literal longs (not used in the symbols yet)

    min_value_internally: int = -9_223_372_036_854_775_808
    max_value_internally: int = 9_223_372_036_854_775_807

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self, self.min_value_internally, self.max_value_internally)


class ByteSchema(BaseSchema):
    """A signed 8-bit integer, ranging from -128 to 127 (inclusive)."""
    kind: Literal["byte"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: bool | int | None = None  # For literal bytes (not used in the symbols yet)

    min_value_internally: int = -128
    max_value_internally: int = 127

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self, self.min_value_internally, self.max_value_internally)


class AnySchema(BaseSchema):
    kind: Literal["any"] = Field(repr=False)

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        ctx.required_imports.add(Import("typing", "Any", type_checking_only=False, is_builtin=True))
        return "Any"


# ==================================================================================================================================
# Iterable Schemas (list, tuple, array, etc.)

type ListSchemaItemTypes = (
    IntSchema | StringSchema | FloatSchema |  ByteSchema | BooleanSchema | ConcreteSchema | DispatcherSchema
    | DynamicIndexSchema | IntArraySchema | ListSchema | LiteralSchema | PairSchema | ReferenceSchema
    | SpreadFieldSchema | StaticIndexSchema | StructSchema | TreeSchema | UnionSchema
)


class ListSchema(BaseSchema):
    """List of type"""
    kind: Literal["list"] = Field(repr=False)
    item: Annotated[ListSchemaItemTypes, Field(discriminator="kind")]
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")

    def contains_inline_struct(self) -> bool:
        return self.item.contains_inline_struct()

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def _calculated_item_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        """Either points directly to the normal annotation (e.g. list[>>>`int`<<<])
        Or, for locally generated structs, points to them (and creates their code)"""
        if isinstance(self.item, StructSchema) and nested_struct_name is not None:
            return self.item.to_materialized_annotation(nested_struct_name, ctx)
        return self.item.to_nested_annotation(ctx, nested_struct_name)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        item_annotation = self._calculated_item_annotation(ctx, nested_struct_name)
        if self.length_range is None:
            return f"list[{item_annotation}]"
        if self.length_range.min is not None and self.length_range.min == self.length_range.max:
            return f"tuple[{', '.join(item_annotation for _ in range(self.length_range.min))}]"
        ctx.require_annotated()
        return f"Annotated[list[{item_annotation}], '{self.length_range.to_annotation_suffix()}']"

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        type_param_names = sorted({symbol_path_to_object_name(path) for path in ctx.local_type_params})
        type_params = f"[{', '.join(type_param_names)}]" if type_param_names else ""
        return [f"type {class_name}{type_params} = {self.to_annotation(ctx, PairSchema.nested_struct_name(class_name))}"]


class TupleSchema(BaseSchema):
    """Tuples aren't used that much, there's only 2 cases of them:
    - ::java::data::timeline::CubicBezierEase
    - ::java::pack::PackFormat
    Length is either 2 or 4.
    """
    kind: Literal["tuple"] = Field(repr=False)
    items: list[IntSchema] | list[FloatSchema]
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return f"tuple[{', '.join(item.to_annotation(ctx) for item in self.items)}]"


class IntArraySchema(BaseSchema):
    """An ordered list of 32-bit integers. Note that [I;1,2,3] and [1,2,3] are considered different types: the second one is a [NBT List / JSON Array] list."""
    kind: Literal["int_array"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value_range: ValueRange | None = Field(default=None, alias="valueRange")

    array_marker: ClassVar[str] = "I"  # For other array types, like Longs, it's "L"

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        array_type_annotation = IntSchema(kind="int", attributes=self.attributes, valueRange=self.value_range)
        list_schema_proxy = ListSchema(kind="list", attributes=self.attributes, item=array_type_annotation, lengthRange=self.length_range)
        return list_schema_proxy.to_annotation(ctx)


class EnumSchema(BaseSchema):
    kind: Literal["enum"] = Field(repr=False)
    enum_kind: Literal["byte", "int", "string"] = Field(alias="enumKind")
    values: list[EnumValue]

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        ctx.required_imports.add(Import("enum", "Enum", False, True))
        return [f"class {class_name}(Enum):"] + [
            f"    {value.identifier.upper()} = {value.to_annotation()}{value.description_comment_or_empty}"
            for value in self.values
        ]


# ==================================================================================================================================
# Meta types


type ConcreteSchemaTypeArgTypes = (
    AnySchema | BooleanSchema | ByteSchema | ConcreteSchema | DispatcherSchema | FloatSchema | IndexedSchema
    | IntArraySchema | IntSchema | ListSchema | LiteralSchema | LongSchema | ReferenceSchema | ShortSchema
    | StringSchema | StructSchema | TupleSchema | UnionSchema
)

class ConcreteSchema(BaseSchema):
    """The purpose of this is it's essentially a class but *with* type_args, i.e. annotated args/extras.
    e.g.
    {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::worldgen::IntProvider"
        },
        "typeArgs": [
            {
                "kind": "int",
                "valueRange": {
                    "kind": 0,
                    "min": 0
                }
            }
        ]
    }
    IntProvider[0, ]
    (Must be 0 or above)
    """
    kind: Literal["concrete"]
    child: ReferenceSchema | DispatcherSchema
    type_args: list[Annotated[ConcreteSchemaTypeArgTypes, Field(discriminator="kind")]] = Field(default_factory=list, alias="typeArgs")

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        # We ommit the "type" so we can bind them, and then other things can inherit this binding.
        runtime_ctx = ctx.with_rendering_options(require_runtime_imports=True)
        return [f"{class_name} = {self.to_annotation(runtime_ctx, class_name)}"]

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        dispatcher_type_args: list[BaseSchema] = list(self.type_args)
        child_annotation = (
            self.child.to_annotation(ctx, type_args=dispatcher_type_args)
            if isinstance(self.child, DispatcherSchema)
            else self.child.to_annotation(ctx)
        )
        child_is_template = isinstance(self.child, ReferenceSchema) and (
            ctx.schema_graph is None
            or isinstance(ctx.schema_graph.symbols.get(self.child.path), TemplateSchema)
        )
        owner_name = nested_struct_name or (
            symbol_path_to_object_name(ctx.current_symbol_path)
            if ctx.current_symbol_path is not None
            else "Concrete"
        )
        struct_count = sum(isinstance(type_arg, StructSchema) for type_arg in self.type_args)
        struct_index = 0
        type_arg_annotations: list[str] = []
        for type_arg in self.type_args:
            if isinstance(type_arg, StructSchema):
                struct_index += 1
                suffix = str(struct_index) if struct_count > 1 else ""
                type_arg_annotations.append(type_arg.to_materialized_annotation(f"{owner_name}TypeArg{suffix}", ctx))
            else:
                type_arg_annotations.append(type_arg.to_annotation(ctx))
        concrete_annotation = (
            f"{child_annotation}[{', '.join(type_arg_annotations)}]"
            if child_is_template
            else child_annotation
        )
        if not self.type_args or not ctx.allow_numeric_type_arg_shortcuts:
            return concrete_annotation

        # Optionally allow passing numeric primitive kind(s) directly alongside the concrete wrapper.
        # There's also some weird other stuff, like this:
        # "kind": "concrete",
        # "child": {
        #     "kind": "reference",
        #     "path": "::java::util::Filterable"
        # },
        # "typeArgs": [{"kind": "string"}]
        shortcut_annotations = [
            type_arg.to_annotation(ctx) for type_arg in self.type_args if isinstance(type_arg, (IntSchema, FloatSchema))
        ]
        if not shortcut_annotations:
            return concrete_annotation

        # This allows you to omit "MinMaxBounds" and such, which generates `MinMaxBounds[int] | int`, QoL
        return " | ".join(dict.fromkeys([concrete_annotation] + shortcut_annotations))


class IndexedSchema(BaseSchema):
    """Not even particularly sure, always has a child Dispatcher, and the weird parallelIndices?
    "mcdoc:block_state_keys": {
        "%none": {
            "kind": "string"
        },
        "%unknown": {
            "kind": "string"
        }
    }
    This is like a custom implementation?
    "registry": "mcdoc:block_state_keys"
    It seems like it just indexes somewhere else?
    Anyway, there's only 7 instances of it in the symbols, so we can "meh" for now.
    """
    kind: Literal["indexed"] = Field(repr=False)
    child: DispatcherSchema
    parallelIndices: list[StaticIndexSchema | DynamicIndexSchema]

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        candidates = ctx.schema_graph.annotation_candidates(self) if ctx.schema_graph is not None else ()
        base_name = nested_struct_name or "IndexedValue"
        return " | ".join(dict.fromkeys(
            DispatcherSchema._branch_annotation(candidate, f"{base_name}{index}", ctx)
            for index, candidate in enumerate(candidates, 1)
        ))


class ReferenceSchema(BaseSchema):
    """References another model/schema by path."""
    kind: Literal["reference"] = Field(repr=False)
    path: str
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        path, name = symbol_path_to_import_string_and_name(self.path)
        maybe_aliased_name = f"{name}_alias" if class_name == name else name
        import_identifier = f"{name} as {maybe_aliased_name}" if class_name == name else name
        ctx.required_imports.add(Import(path, f"{import_identifier}", type_checking_only=False, is_builtin=False))
        return [f"type {class_name} = {maybe_aliased_name}"]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        # Make sure we import the referenced symbol
        return ctx.add_import_by_symbol_path(self.path)


type UnionSchemaMemberTypes = (
    PairSchema | ListSchema | StringSchema | ReferenceSchema | DispatcherSchema | ConcreteSchema | BooleanSchema | StructSchema
    | UnionSchema | LiteralSchema | IntSchema | IndexedSchema | FloatSchema | IntArraySchema | TupleSchema | ByteSchema | ShortSchema
)


class UnionSchema(BaseSchema):
    """Allows x OR y type schemas/definitions"""
    kind: Literal["union"] = Field(repr=False)
    members: list[Annotated[UnionSchemaMemberTypes, Field(discriminator="kind")]]

    @model_validator(mode="after")
    def prune_members_on_version(self) -> Self:
        # Remove members that are invalid for the current CURRENT_VERSION or are empty wrappers
        self.members = [
            member for member in self.members
            # If member has attributes controlling versioning, respect them
            if is_valid_with_attributes(member.attributes)
        ]
        return self

    @staticmethod
    def _render_member(
        member: UnionSchemaMemberTypes,
        nested_name: str | None,
        ctx: SingleSymbolContext,
        declare_struct: bool,
    ) -> tuple[list[str], str]:
        """Render one union member and any sibling declaration it requires."""
        if isinstance(member, StructSchema) and nested_name is not None:
            if declare_struct:
                return member.to_python_code(nested_name, ctx) + [""], nested_name
            return [], member.to_materialized_annotation(nested_name, ctx)
        return [], member.to_nested_annotation(ctx, nested_name)

    def _render_members(
        self, nested_name: str | None, ctx: SingleSymbolContext, declare_structs: bool = False,
    ) -> tuple[list[str], list[str]]:
        """Render union annotations and any required sibling struct declarations."""
        declarations: list[str] = []
        annotations: list[str] = []
        nested_member_count = sum(member.contains_inline_struct() for member in self.members)
        nested_member_index = 0

        for member in self.members:
            member_name = nested_name
            if member.contains_inline_struct():
                nested_member_index += 1
                if nested_name is not None and nested_member_count > 1:
                    member_name = f"{nested_name}{nested_member_index}"
            member_declarations, annotation = self._render_member(member, member_name, ctx, declare_structs)
            declarations.extend(member_declarations)
            annotations.append(annotation)

        return declarations, list(dict.fromkeys(annotations)) or ["None"]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        _, annotations = self._render_members(nested_struct_name, ctx)
        return " | ".join(annotations)

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        if len(self.members) == 1:  # Some objects are (since, A) | (until, B) - collapse into just A
            return self.members[0].to_python_code(class_name, ctx)

        # Materialize struct members as concrete sibling symbols so the union alias can reference them.
        declarations, annotations = self._render_members(f"{class_name}Struct", ctx, declare_structs=True)
        return declarations + [f"type {class_name} = {' | '.join(annotations)}"]


type PairSchemaTypes = (
    IntSchema | FloatSchema | ConcreteSchema | ListSchema | UnionSchema | ReferenceSchema | BooleanSchema | AnySchema | TupleSchema
    | IndexedSchema | StringSchema | StructSchema | ByteSchema | DispatcherSchema | IntArraySchema | ShortSchema | LongSchema
    | LiteralSchema | ShortSchema
)


class PairSchema(BaseSchema):
    """Encapsulates a key-value pair, essentially a basic attribute with description and such."""
    kind: Literal["pair"] = Field(repr=False)
    key: str | StringSchema | ReferenceSchema | DispatcherSchema | UnionSchema
    type: Annotated[PairSchemaTypes, Field(discriminator="kind")]
    description: str = Field(default="", repr=False, alias="desc")
    optional: bool = False

    @property
    def description_or_empty(self) -> str:
        return f"  # {self.description.replace('\\\n', '\n').replace('\n', ' ').strip()}" if self.description else ""

    @property
    def optional_string_or_empty(self) -> str:
        return " | None = None" if self.optional else ""

    @staticmethod
    def clean_key(key: str | StringSchema | ReferenceSchema) -> str:
        # These two isinstance checks aren't perfect, but there's only 3 tiny cases in the whole of symbols.json
        if isinstance(key, ReferenceSchema):
            return symbol_path_to_object_name(key.path)
        if isinstance(key, StringSchema):
            return "key_name"
        return key if key not in {"from", "with"} else f"{key}_"

    @staticmethod
    def nested_struct_name(key: str) -> str:
        """For structs attributes that are also structs, we need to figure out the name of the new struct.
        For now, we append Struct, but if it's snake_case, we make it camel case and then add Struct."""
        if "_" in key or key.islower():
            key = "".join(part[:1].upper() + part[1:] for part in key.split("_") if part)
        return f"{key}Struct"


class SpreadFieldSchema(BaseSchema):
    """An inliner, for spread (inheritence).
    E.g. Suspicious stew has attributes {
        "kind": "spread", "type": {"kind": "reference", "path": "::java::world::item::ItemBase"}
    }
    So they get inlined (suspicious stew now gets all the attributes from ItemBase).
    """
    kind: Literal["spread"] = Field(repr=False)
    type: Annotated[
        ReferenceSchema | ConcreteSchema | DispatcherSchema | StructSchema | UnionSchema | PairSchema,
        Field(discriminator="kind"),
    ]

    def _unravel_reference(self) -> ReferenceSchema | None:
        """Returns a reference, or a concrete schema's reference, or None"""
        if isinstance(self.type, ReferenceSchema):
            return self.type
        if isinstance(self.type, ConcreteSchema):
            if isinstance(self.type.child, ReferenceSchema):
                return self.type.child
            # if isinstance(self.type.child, DispatcherSchema):  # TODO: Eventually inherit from these
            #     return None
            # raise TypeError("Invalid SpreadField + ConcreteSchema")
        return None

    @classmethod
    def collect_runtime_symbol_imports(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema], ctx: SingleSymbolContext) -> None:
        """Adds all the necessary classes to the required imports list"""
        for spread_field_schema in [fld for fld in fields if isinstance(fld, SpreadFieldSchema)]:
            reference = spread_field_schema._unravel_reference()
            runtime_import = (
                Import(*symbol_path_to_import_string_and_name(reference.path), False, False)
                if reference and reference.path not in ctx.local_type_params
                else None
            )
            # if runtime_import is None and isinstance(spread_field_schema.type, ConcreteSchema) and isinstance(spread_field_schema.type.child, DispatcherSchema):
            #     runtime_import = Import(*symbol_path_to_import_string_and_name(spread_field_schema.type.child.registry), False, False)
            if runtime_import is not None:
                ctx.required_imports.add(runtime_import)
            if isinstance(spread_field_schema.type, StructSchema):
                SpreadFieldSchema.collect_runtime_symbol_imports(spread_field_schema.type.fields, ctx)

    @classmethod
    def collect_inherited_base_names(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema], ctx: SingleSymbolContext) -> list[str]:
        """Return a list of strings representing inherited classes, e.g. class MyClass(`<x>`, `<y>`) """
        base_names: set[str] = set()
        for spread_field_schema in [fld for fld in fields if isinstance(fld, SpreadFieldSchema)]:
            # Keep concrete spread type arguments in inheritance, e.g. UniformIntProvider[T].
            strict_ctx = ctx.with_rendering_options(
                allow_numeric_type_arg_shortcuts=False,
                require_runtime_imports=True,
            )  # Don't allow inherited | float, for example.
            reference: ReferenceSchema | None = spread_field_schema._unravel_reference()
            if reference is not None and reference.path not in ctx.local_type_params:
                base_names.add(spread_field_schema.type.to_annotation(strict_ctx))
            if isinstance(spread_field_schema.type, StructSchema):
                base_names = base_names.union(SpreadFieldSchema.collect_inherited_base_names(spread_field_schema.type.fields, ctx))
        return sorted(base_names)

    @classmethod
    def filter_fields_to_pair_schemas_only(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema]) -> list[PairSchema]:
        """For all the fields, return only those that are `PairSchema`. \n
        If it's a struct, return **ITS** `PairSchema`s"""
        inlined_fields: list[PairSchema] = []
        for pair_field in fields:
            if isinstance(pair_field, PairSchema):
                inlined_fields.append(pair_field)
            if isinstance(pair_field, cls) and isinstance(pair_field.type, StructSchema):
                inlined_fields.extend(SpreadFieldSchema.filter_fields_to_pair_schemas_only(pair_field.type.fields))
        return inlined_fields


class TemplateTypeParam(BaseModel):
    """Represents a template type parameter path (e.g. ::java::world::item::T)."""
    path: str


type TemplateChildTypes = (
    AnySchema | BooleanSchema | ByteSchema | ConcreteSchema | DispatcherSchema | FloatSchema | IndexedSchema
    | IntArraySchema | IntSchema | ListSchema | LiteralSchema | LongSchema | ReferenceSchema | ShortSchema
    | StringSchema | StructSchema | TupleSchema | UnionSchema
)

class TemplateSchema(BaseSchema):
    """"
    Built-in types, e.g. `::java::data::worldgen::UniformInt`
    They always take a type, e.g. ClampedIntProvider[T]
    Essentially, these are Generics of type (normally T)
    """
    kind: Literal["template"] = Field(repr=False)
    child: Annotated[TemplateChildTypes, Field(discriminator="kind")]
    type_params: list[TemplateTypeParam] = Field(default_factory=list, alias="typeParams")

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        ctx.local_type_params.update(type_param.path for type_param in self.type_params)
        if isinstance(self.child, UnionSchema):
            struct_member = next(member for member in self.child.members if isinstance(member, StructSchema))  # Always exactly 1
            return struct_member.to_python_code(class_name, ctx) 
        return self.child.to_python_code(class_name, ctx)


class StructSchema(BaseSchema):
    kind: Literal["struct"]
    fields: list[Annotated[PairSchema | SpreadFieldSchema | UnionSchema, Field(discriminator="kind")]]

    def contains_inline_struct(self) -> bool:
        return True

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    @model_validator(mode="after")
    def prune_fields_on_version(self) -> Self:
        # All the PairSchema and SpreadFieldSchema fields have attributes, so we can filter them based on the current version.
        filtered_fields: list[PairSchema | SpreadFieldSchema | UnionSchema] = [
            field for field in self.fields
            if isinstance(field, (PairSchema, SpreadFieldSchema)) and is_valid_with_attributes(field.attributes)
        ]
        self.fields = filtered_fields
        return self

    def _mapping_pair(self) -> PairSchema | None:
        """Recognize mcdoc's struct representation of a mapping.

        A pair whose key is itself a schema describes *arbitrary* entries, such as
        `string -> string`, rather than a *fixed object* field. A struct is therefore
        rendered as `dict[key_type, value_type]` ONLY when it contains exactly one
        schema-keyed pair and no named string-keyed pairs. For example, Lang's sole
        `StringSchema` key becomes `dict[str, str]`

        Multiple schema-keyed pairs are slightly ambiguous, and the presence of a named
        pair means the struct also describes fixed fields, so neither shape is collapsed
        into a mapping alias.
        """
        plain_pairs =      [field for field in self.fields if isinstance(field, PairSchema) and isinstance(field.key, str)]  # fmt: skip
        schema_key_pairs = [field for field in self.fields if isinstance(field, PairSchema) and not isinstance(field.key, str)]
        return schema_key_pairs[0] if len(schema_key_pairs) == 1 and not plain_pairs else None

    def _dispatcher_spread(self) -> tuple[SpreadFieldSchema, DispatcherSchema, str] | None:
        """Return the supported selector-based union spread, if this struct has one.

        mcdoc represents some unions as *shared struct fields* plus a
        dispatcher spread. The dispatcher's single string accessor names the shared
        field that selects a registry branch. We expand that shape into one dataclass
        per branch so each selector value stays correlated with its fields.

        Distribution is only unambiguous when there is exactly one dispatcher spread,
        structs with zero or multiple such spreads continue through normal rendering
        """
        dispatcher_spreads: list[SpreadFieldSchema] = [
            field for field in self.fields
            if isinstance(field, SpreadFieldSchema) and isinstance(field.type, DispatcherSchema)
        ]
        if len(dispatcher_spreads) != 1:  # Ambiguous, either 0 or > 1
            return None
        spread = dispatcher_spreads[0]
        assert isinstance(spread.type, DispatcherSchema)
        return spread, spread.type, spread.type.dynamic_selector_field

    def _dispatcher_variant(
        self, dispatcher_spread: SpreadFieldSchema, branch_struct: StructSchema, selector_field: str, registry_key: str,
    ) -> StructSchema:
        """Build the struct for one entry in the dispatcher's registry.

        Start with deep copies of the original struct's shared fields, omitting the
        dispatcher spread because this registry branch replaces it. For a normal key,
        narrow the selector field to its namespaced literal value; for example, the
        `ore_drops` branch changes `formula: ApplyBonusFormula` to
        `formula: Literal["minecraft:ore_drops"]`. This keeps the selector value and
        the branch-specific fields linked in the generated union.

        Keys beginning with `%` are fallback entries rather than concrete selector
        values, so their selector field is left unchanged. Finally, append the fields
        resolved from the selected branch. Schema-keyed pairs describe arbitrary map
        entries and cannot become named dataclass fields, so only ordinary string-keyed
        pairs are copied from the branch.
        """
        fields: list[PairSchema | SpreadFieldSchema | UnionSchema] = []
        selector_found = registry_key.startswith("%")
        for field in [fld for fld in self.fields if fld is not dispatcher_spread]:
            copied_field = field.model_copy(deep=True)
            if (
                not registry_key.startswith("%")
                and isinstance(copied_field, PairSchema)
                and copied_field.key == selector_field
            ):
                copied_field.type = LiteralSchema(
                    kind="literal",
                    value=StringSchema(kind="string", value=f"minecraft:{registry_key}"),
                )
                selector_found = True
            fields.append(copied_field)

        assert selector_found
        fields.extend(
            field.model_copy(deep=True)
            for field in branch_struct.fields
            if not isinstance(field, PairSchema) or isinstance(field.key, str)
        )
        return StructSchema(kind="struct", fields=fields)

    def _dispatcher_variants(
        self, class_name: str, dispatcher_spread: SpreadFieldSchema, dispatcher: DispatcherSchema,
        selector_field: str, ctx: SingleSymbolContext,
    ) -> list[tuple[str, StructSchema]]:
        """Resolve every registry entry into a uniquely named specialized struct."""
        assert ctx.schema_graph is not None

        variants: list[tuple[str, StructSchema]] = []
        for key, branch in ctx.schema_graph.dispatchers[dispatcher.registry].items():
            branch_structs = [schema for schema in ctx.schema_graph.resolve(branch) if isinstance(schema, StructSchema)]
            branch_structs = branch_structs or [StructSchema(kind="struct", fields=[])]
            suffix = PairSchema.nested_struct_name(key.lstrip("%").replace("/", "_")).removesuffix("Struct") or "Fallback"
            for index, branch_struct in enumerate(branch_structs, 1):
                preferred = f"{class_name}{suffix}{index if len(branch_structs) > 1 else ''}"
                variant_name = ctx.allocate_name(preferred, branch_struct.model_dump_json(by_alias=True))
                variants.append((
                    variant_name,
                    self._dispatcher_variant(dispatcher_spread, branch_struct, selector_field, key),
                ))
        return variants

    def _render_dispatcher_spread(self, class_name: str, ctx: SingleSymbolContext) -> list[str] | None:
        """Render distributed branch dataclasses followed by their union alias."""
        dispatcher_spread = self._dispatcher_spread()
        if dispatcher_spread is None or ctx.schema_graph is None:
            return None
        spread_field, dispatcher, selector_field = dispatcher_spread
        variants = self._dispatcher_variants(class_name, spread_field, dispatcher, selector_field, ctx)
        rendered: list[str] = []
        for variant_name, variant in variants:
            rendered.extend(variant.to_python_code(variant_name, ctx) + [""])
        return rendered + [f"type {class_name} = {' | '.join(name for name, _ in variants)}"]

    def _render_alias_spread(self, class_name: str, ctx: SingleSymbolContext) -> list[str] | None:
        assert ctx.schema_graph is not None
        for spread in (field for field in self.fields if isinstance(field, SpreadFieldSchema)):
            if ctx.schema_graph.is_runtime_class(spread.type):
                continue
            resolved = ctx.schema_graph.resolve(spread.type)
            candidates = resolved[0].members if len(resolved) == 1 and isinstance(resolved[0], UnionSchema) else resolved
            structs = [candidate for candidate in candidates if isinstance(candidate, StructSchema)]
            if len(structs) != len(candidates):
                continue
            variants = [
                self.model_copy(update={"fields": [
                    *(field.model_copy(deep=True) for field in self.fields if field is not spread),
                    *(field.model_copy(deep=True) for field in struct.fields),
                ]})
                for struct in structs
            ]
            if len(variants) == 1:
                return variants[0].to_python_code(class_name, ctx)
            names = [f"{class_name}Struct{index}" for index in range(1, len(variants) + 1)]
            rendered = [line for name, variant in zip(names, variants, strict=True) for line in variant.to_python_code(name, ctx) + [""]]
            return rendered + [f"type {class_name} = {' | '.join(names)}"]
        return None

    def _mapping_alias_annotation(self, ctx: SingleSymbolContext, value_struct_name: str | None = None) -> str | None:
        """Returns the mapping alias dict (i.e. dict[<x>, <x>]) for a struct, or None if it's not that kind of struct."""
        field = self._mapping_pair()
        if field is None:
            return None

        assert not isinstance(field.key, str)
        if value_struct_name is not None and isinstance(field.type, StructSchema):
            value_annotation = field.type.to_materialized_annotation(value_struct_name, ctx)
        else:
            value_annotation = field.type.to_nested_annotation(ctx, value_struct_name)
        return f"dict[{field.key.to_annotation(ctx)}, {value_annotation}]"

    def to_materialized_annotation(self, class_name: str, ctx: SingleSymbolContext) -> str:
        """Both adds itself to the list of created dataclasses, plus returns the annotation materialized."""
        class_name = ctx.allocate_name(class_name, self.model_dump_json(by_alias=True))
        ctx.add_dataclass(self.to_python_code(class_name, ctx))
        type_param_names = sorted({symbol_path_to_object_name(path) for path in ctx.local_type_params})
        type_args = f"[{', '.join(type_param_names)}]" if type_param_names else ""
        return f"{class_name}{type_args}"

    def _render_dataclass(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        # Collects Structs' inherrited children, e.g. class MyClass(PredicateOffset)
        inherited_names = SpreadFieldSchema.collect_inherited_base_names(self.fields, ctx)
        template_type_names = sorted({symbol_path_to_object_name(path) for path in ctx.local_type_params})
        if template_type_names:
            ctx.required_imports.add(Import("typing", "Generic", False, True))
            inherited_names.append(f"Generic[{', '.join(template_type_names)}]")
    
        ctx.required_imports.add(Import("dataclasses", "dataclass", False, True))
        lines: list[str] = ["@dataclass(kw_only=True)"]
        lines.append(
            f"class {class_name}:"
            if not inherited_names else
            f"class {class_name}({', '.join(inherited_names)}):"
        )

        used_keys: set[str] = set()

        assert all(isinstance(field, (PairSchema, SpreadFieldSchema)) for field in self.fields)  # It's never UnionSchema here
        pair_fields = SpreadFieldSchema.filter_fields_to_pair_schemas_only(self.fields)
        if not pair_fields:
            lines.append("    pass")

        for pair_field in pair_fields:
            key = PairSchema.clean_key(pair_field.key)  # type: ignore[arg-type]
            preferred = key
            suffix = 2
            while key in used_keys:
                key = f"{preferred}_{suffix}"
                suffix += 1
            used_keys.add(key)
            if isinstance(pair_field.type, StructSchema) and pair_field.type._mapping_pair() is None:
                nested_struct_name = PairSchema.nested_struct_name(key)
                annotation = pair_field.type.to_materialized_annotation(nested_struct_name, ctx)
            else:
                annotation = pair_field.type.to_nested_annotation(ctx, PairSchema.nested_struct_name(key))
            if not annotation.strip() or annotation == "None":
                continue  # Empty unions represent weird stuff - skip so parent members can remain authoritative.

            line = f"    {key}: {annotation}{pair_field.optional_string_or_empty}{pair_field.description_or_empty}"
            lines.append(line)
        return lines + [""]

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        alias_spread = self._render_alias_spread(class_name, ctx)
        if alias_spread is not None:
            return alias_spread

        dispatcher_union = self._render_dispatcher_spread(class_name, ctx)
        if dispatcher_union is not None:
            return dispatcher_union

        mapping_alias = self._mapping_alias_annotation(ctx, f"{class_name}ValueStruct")
        if mapping_alias is not None:
            # This is exclusively type <x>[type?] = dict[<key>, <value>]
            template_type_names = sorted({symbol_path_to_object_name(path) for path in ctx.local_type_params})
            template_type_names_string = f"[{', '.join(template_type_names)}]" if template_type_names else ""
            return [f"type {class_name}{template_type_names_string} = {mapping_alias}\n"]

        SpreadFieldSchema.collect_runtime_symbol_imports(self.fields, ctx)  # Attaches inherited classes to ctx

        # Discover unresolved symbolic refs before rendering the Generic[...] base.
        for field in SpreadFieldSchema.filter_fields_to_pair_schemas_only(self.fields):
            for child in iter_child_schemas(field.type):
                if isinstance(child, ReferenceSchema) and child.path not in ROOT_SYMBOLS_KEYS["mcdoc"]:
                    ctx.local_type_params.add(child.path)

        return self._render_dataclass(class_name, ctx)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        value_struct_name = f"{nested_struct_name}ValueStruct" if nested_struct_name is not None else None
        mapping_alias: str = self._mapping_alias_annotation(ctx, value_struct_name)  # type: ignore[assignment]
        return mapping_alias


# ==================================================================================================================================
# Grossness


class DynamicIndexAccessorItem(BaseModel):
    """Represents an item in the accessor list of a DynamicIndexSchema.  \n
    It's a keyword mapping to parent or key, e.g. {"keyword": "parent"} or {"keyword": "key"}."""
    keyword: Literal["key", "parent"]


class DynamicIndexSchema(BaseSchema):
    kind: Literal["dynamic"] = Field(repr=False)
    accessor: list[str | DynamicIndexAccessorItem]  # "accessor": [{"keyword": "parent"}, "blocks"] | "accessor": [{"keyword": "key"}] | "accessor": ["type"]


class StaticIndexSchema(BaseSchema):
    kind: Literal["static"] = Field(repr=False)
    value: str


class DispatcherSchema(BaseSchema):
    """Selects a schema from a registry using one or more parallel indices."""
    kind: Literal["dispatcher"] = Field(repr=False)
    parallel_indices: list[StaticIndexSchema | DynamicIndexSchema] = Field(alias="parallelIndices")
    registry: str

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    @property
    def dynamic_selector_field(self) -> str:
        """Return the field selected by the supported single direct accessor."""
        accessors = [index.accessor for index in self.parallel_indices if isinstance(index, DynamicIndexSchema)]
        assert len(accessors) == 1 and len(accessors[0]) == 1 and isinstance(accessors[0][0], str)
        return accessors[0][0]

    def to_annotation(
        self, ctx: SingleSymbolContext, nested_struct_name: str | None = None, type_args: list[BaseSchema] | None = None,
    ) -> str:
        assert ctx.schema_graph is not None
        registry = ctx.schema_graph.dispatchers[self.registry]
        candidates: list[tuple[str, BaseSchema]] = []
        for index in self.parallel_indices:
            if isinstance(index, DynamicIndexSchema) or index.value == "%fallback":
                candidates.extend(registry.items())
            else:
                key = index.value.removeprefix("minecraft:")
                branch = registry.get(key) or registry["%unknown"]
                candidates.append((key, branch))

        registry_name = PairSchema.nested_struct_name(self.registry.split(":")[-1]).removesuffix("Struct")
        base_name = f"{nested_struct_name}{registry_name}" if nested_struct_name else f"{registry_name}Struct"
        annotations: list[str] = []
        seen: set[str] = set()
        for key, branch in candidates:
            if type_args is not None:
                branch = ctx.schema_graph.instantiate(branch, type_args)  # type: ignore[arg-type]
            fingerprint = branch.model_dump_json(by_alias=True)
            if fingerprint in seen:
                continue
            seen.add(fingerprint)
            clean_key = "".join(character if character.isalnum() else "_" for character in key.lstrip("%"))
            branch_name = f"{base_name}{PairSchema.nested_struct_name(clean_key).removesuffix('Struct')}"
            annotations.append(self._branch_annotation(branch, branch_name, ctx))

        return " | ".join(dict.fromkeys(annotations))

    @classmethod
    def _branch_annotation(cls, branch: BaseSchema, branch_name: str, ctx: SingleSymbolContext) -> str:
        if isinstance(branch, StructSchema):
            return branch.to_materialized_annotation(branch_name, ctx)
        return branch.to_nested_annotation(ctx, branch_name)


class TreeSchema(BaseSchema):
    """Represents a 'tree' structure, found inside an Attribute's value.
    Example: ::java::data::worldgen::attribute::PositionalEnvironmentAttribute """
    kind: Literal["tree"] = Field(repr=False)
    values: TreeValueSchema


class TreeValueSchema(RootModel[dict[str, TreeSchema | LiteralSchema]]):
    """Represents the 'values' part of a TreeSchema. It's a flexible dictionary."""
    root: dict[str, TreeSchema | LiteralSchema]


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================

type KindOption = Literal[
    "int", "string", "float", "double", "boolean", "short", "long", "byte", "literal", "any",
    "list", "tuple", "int_array", "enum",
    "concrete", "indexed", "reference", "union", "pair", "spread",
    "template", "struct", "dynamic", "static", "dispatcher", "tree",
]

KIND_TO_MODEL: dict[KindOption, type[BaseSchema]] = {
    "struct": StructSchema,
    "enum": EnumSchema,
    "union": UnionSchema,
    "template": TemplateSchema, "reference": ReferenceSchema, "literal": LiteralSchema, "pair": PairSchema, "concrete": ConcreteSchema, "string": StringSchema,
    "float": FloatSchema, "list": ListSchema, "tuple": TupleSchema, "int": IntSchema, "short": ShortSchema, "long": LongSchema, "boolean": BooleanSchema,
    "byte": ByteSchema, "int_array": IntArraySchema,
    "dispatcher": DispatcherSchema, "any": AnySchema, "indexed": IndexedSchema, "dynamic": DynamicIndexSchema,
    "tree": TreeSchema,
    "spread": SpreadFieldSchema,
    "static": StaticIndexSchema, "double": FloatSchema,
}
