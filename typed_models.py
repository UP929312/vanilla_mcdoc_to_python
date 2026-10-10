from typing import Annotated, Literal, Self, get_args

from pydantic import BaseModel, Field, model_validator

from context import Import, SingleSymbolContext
from minecraft_registry import known_registry_alias
from static_symbols.minecraft_types import IdSpec
from utils import GENERATED_SYMBOLS_DIRECTORY, ROOT_SYMBOLS_KEYS, SAFE_GUARD_JAVA_NUMBERS, symbol_path_to_import_string_and_name, symbol_path_to_object_name, is_valid_with_attributes, iter_child_schemas


class BaseSchema(BaseModel):
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def contains_inline_struct(self) -> bool:
        """Return whether this schema needs a generated name for an inline struct."""
        return False

    def has_attribute(self, name: str) -> bool:
        return any(attribute.name == name for attribute in self.attributes)

    @staticmethod
    def _minecraft_type(name: str, ctx: SingleSymbolContext) -> str:
        """Use one of the hand-written types from static_symbols/minecraft_types.py (copied into the package), e.g. MinecraftUUID"""
        ctx.required_imports.add(Import(f"{GENERATED_SYMBOLS_DIRECTORY.name}.minecraft_types", name, False))
        return name

    def to_nested_annotation(self, ctx: SingleSymbolContext, _nested_struct_name: str | None) -> str:
        """Render an annotation, using a nested declaration name when supported."""
        return self.to_annotation(ctx)

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        """Generate the actual Python, for most things, this is just the alias to the annotation"""
        return [f"type {class_name} = {self.to_annotation(ctx)}"]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        raise NotImplementedError(f"This should never get called directly on a {self.__class__.__name__}")  # pragma: no cover

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

    def to_string_pattern(self) -> str | None:
        """The regex a string with this attribute must contain, matching how Spyglass validates them, e.g.
        #[match_regex="^[A-Za-z0-9_]*$"], #[integer] (a string of digits) or #[color="hex_rgb"] (starts with a #)"""
        if self.name == "match_regex":
            return str(self._attribute_value(self.value))
        if self.name == "integer":
            return r"^-?\d+$"
        if self.name == "color" and self._attribute_value(self.value) == "hex_rgb":
            return "^#"
        return None

    @classmethod
    def _attribute_value(cls, schema: LiteralSchema | TreeSchema | DispatcherSchema | ReferenceSchema | None) -> object:
        if schema is None:
            return None
        if isinstance(schema, LiteralSchema):
            return schema.value.value
        # TreeSchemas:
        assert not isinstance(schema, (DispatcherSchema, ReferenceSchema))
        values = {key: cls._attribute_value(value) for key, value in schema.values.items()}
        return tuple(values[key] for key in sorted(values, key=int)) if all(key.isdigit() for key in values) else values


class ValueRange(BaseModel):
    """Represents a numeric range, used in `int`, `float`, and array lengths.
    Kind:
    0 = min inclusive, max inclusive
    1 = min inclusive, max exclusive (currently not used)
    2 = min exclusive, max inclusive
    3 = min exclusive, max exclusive (currently not used)
    """
    kind: Literal[0, 1, 2, 3] = Field(default=0, repr=False)
    min: float | int  # Min is *always* set
    max: float | int | None = None

    def to_annotation(self, ctx: SingleSymbolContext, value_range_type: Literal["int", "float"], attributes: list[Attribute]) -> str:
        ctx.required_imports.add(Import("pydantic", "Field", False))
        if self.max is not None:
            greater_than = "ge" if self.kind in {0, 1} else "gt"
            less_than    = "le" if self.kind in {0, 2} else "lt"  # fmt: skip
            parts = [f"Field({greater_than}={self.min}, {less_than}={self.max})"]
        # In cases where self.max _IS_ None:
        elif self.kind in {0, 1}:  # Min is inclusive
            parts = [f"Field(ge={self.min})"]
        else:  # Kind in 2, 3 - Min is exclusive
            parts = [f"Field(gt={self.min})"]
        if self.extract_divisible_by_value(attributes):
            parts.append(f"Field(multiple_of={self.extract_divisible_by_value(attributes)})")
        ctx.require_annotated()
        return f"Annotated[{value_range_type}, {', '.join(parts)}]"

    def extract_divisible_by_value(self, attributes: list[Attribute]) -> str | None:
        attribute = next((attr for attr in attributes if attr.name == "divisible_by"), None)
        if attribute is None:
            return None
        value = str(Attribute._attribute_value(attribute.value))
        return value


class LengthRange(BaseModel):
    kind: Literal[0] = Field(default=0, repr=False)  # Not sure what other values this can be?
    min: int | None = None  # Only like one of these has a max but no min...
    max: int | None = None

    def to_annotation_suffix(self, ctx: SingleSymbolContext) -> str:
        ctx.required_imports.add(Import("pydantic", "Field", False))
        if self.min is not None and self.max is not None:
            return f"Field(min_length={self.min}, max_length={self.max})"
        if self.min is not None:
            return f"Field(min_length={self.min})"
        if self.max is not None:
            return f"Field(max_length={self.max})"
        raise TypeError("Min and Max are None! LengthRange.to_annotation_suffix error")  # pragma: no cover


class EnumValue(BaseModel):
    identifier: str
    value: str | int | float | bool
    description: str = Field(default="", repr=False, alias="desc")
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

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
    value: Annotated[StringSchema | IntSchema | BooleanSchema | DoubleSchema, Field(discriminator="kind")]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        ctx.required_imports.add(Import("typing", "Literal", False))
        value = self.value.value
        if isinstance(value, str) and value.startswith("minecraft:"):  # Resource locations work with or without the namespace
            return f"Literal[{value!r}, {value.removeprefix('minecraft:')!r}]"
        return f"Literal[{value!r}]"


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
        if SAFE_GUARD_JAVA_NUMBERS:  # pragma: no cover
            copied_schema = self.model_copy(update={
                "value_range": ValueRange(min=self.min_value_internally, max=self.max_value_internally),
            })
            return copied_schema.to_annotation(ctx)
        return "int"

    @classmethod
    def _to_annotation_with_bounds(cls, ctx: SingleSymbolContext, original_object: ByteSchema | ShortSchema | LongSchema) -> str:
        """Purpose of this is so other things like bytes, shorts, longs, etc can call it to get a easier method"""
        int_schema = cls(
            kind="int",
            attributes=original_object.attributes,
            valueRange=original_object.value_range,
            min_value_internally=original_object.min_value_internally,
            max_value_internally=original_object.max_value_internally,
        )
        return int_schema.to_annotation(ctx)


class StringSchema(BaseSchema):
    kind: Literal["string"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value: str | None = None  # For literal strings

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.has_attribute("uuid"):
            return self._minecraft_type("MinecraftUUIDString", ctx)
        if self.has_attribute("url"):
            return self._minecraft_type("MinecraftURL", ctx)
        id_spec = next((attribute.to_id_spec() for attribute in self.attributes if attribute.to_id_spec() is not None), None)
        metadata: list[str] = []
        if id_spec is not None:
            self._minecraft_type("IdSpec", ctx)  # Imports it
            metadata.append(id_spec.to_annotation())  # Adds IdSpec(registry=...), for example
        # For regex patterns, we add a Field(pattern=...) to the Annotated[str, ...] type, so that pydantic can validate it.
        for attribute in [attribute for attribute in self.attributes if attribute.to_string_pattern() is not None]:
            ctx.required_imports.add(Import("pydantic", "Field", False))
            metadata.append(f"Field(pattern={attribute.to_string_pattern()!r})")

        # Return Annotated[str, <x>] if length range present:
        if self.length_range is not None:
            if self.length_range.min == 0 and self.length_range.max == 0:
                # Edge case, because of this one instance:
                # https://github.com/SpyglassMC/vanilla-mcdoc/blob/main/java/assets/credits.mcdoc#L5
                # https://github.com/misode/mcmeta/blob/assets/assets/minecraft/texts/credits.json#L1998
                # Literally only one thing - ::java::assets::credits::CreditsDiscipline
                ctx.required_imports.add(Import("typing", "Literal", False))
                return 'Literal[""]'
            metadata.insert(0, self.length_range.to_annotation_suffix(ctx))

        if not metadata:
            return "str"
        ctx.require_annotated()
        annotation = f"Annotated[str, {', '.join(metadata)}]"
        known_id_alias = known_registry_alias(ctx, id_spec) if id_spec is not None else None
        return f"{annotation} | {known_id_alias}" if known_id_alias is not None else annotation


class FloatSchema(BaseSchema):
    """A 32-bit, single-precision floating-point number, ranging from -3.4E38 to +3.4E38."""
    kind: Literal["float"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: float | None = None  # For literal floats (not used in the symbols yet)

    min_value_internally: float = -3.4E38
    max_value_internally: float = 3.4E38

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.value_range:
            return self.value_range.to_annotation(ctx, "float", self.attributes)
        if SAFE_GUARD_JAVA_NUMBERS:  # pragma: no cover
            return self.model_copy(update={"value_range": ValueRange(min=self.min_value_internally, max=self.max_value_internally)}).to_annotation(ctx)
        return "float"


class DoubleSchema(BaseSchema):
    """A 64-bit, double-precision floating-point, ranging from -1.79E308 to +1.79E308."""
    kind: Literal["double"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: float | None = None  # For literal doubles

    min_value_internally: float = -1.79E308
    max_value_internally: float = 1.79E308

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.value_range:
            return self.value_range.to_annotation(ctx, "float", self.attributes)
        if SAFE_GUARD_JAVA_NUMBERS:  # pragma: no cover
            return self.model_copy(update={"value_range": ValueRange(min=self.min_value_internally, max=self.max_value_internally)}).to_annotation(ctx)
        return "float"


class BooleanSchema(BaseSchema):
    kind: Literal["boolean"] = Field(repr=False)
    value: bool | None = None

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return "bool"


class ByteSchema(BaseSchema):
    """A signed 8-bit integer, ranging from -128 to 127 (inclusive)."""
    kind: Literal["byte"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: bool | int | None = None  # For literal bytes (not used in the symbols yet)

    min_value_internally: int = -128
    max_value_internally: int = 127

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self)


class ShortSchema(BaseSchema):
    """A signed 16-bit integer, ranging from -32,768 to 32,767 (inclusive)."""
    kind: Literal["short"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: int | None = None  # For literal shorts (not used in the symbols yet)

    min_value_internally: int = -32_768
    max_value_internally: int = 32_767

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self)


class LongSchema(BaseSchema):
    """A signed 64-bit integer, ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (inclusive)."""
    kind: Literal["long"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: int | None = None  # For literal longs (not used in the symbols yet)

    min_value_internally: int = -9_223_372_036_854_775_808
    max_value_internally: int = 9_223_372_036_854_775_807

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return IntSchema._to_annotation_with_bounds(ctx, self)


class AnySchema(BaseSchema):
    kind: Literal["any"] = Field(repr=False)

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        ctx.required_imports.add(Import("typing", "Any", type_checking_only=False))
        return "Any"


# ==================================================================================================================================
# Iterable Schemas (list, tuple, array, etc.)

type ListSchemaItemTypes = (
    IntSchema | StringSchema | FloatSchema | DoubleSchema | BooleanSchema | ConcreteSchema | DispatcherSchema
    | IntArraySchema | ListSchema | ReferenceSchema | StructSchema | UnionSchema
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

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        if self.has_attribute("uuid"):  # A list of 4 ints
            return self._minecraft_type("MinecraftUUID", ctx)
        item_annotation = self.item.to_nested_annotation(ctx, nested_struct_name)
        if self.length_range is None:
            return f"list[{item_annotation}]"
        if self.length_range.min is not None and self.length_range.min == self.length_range.max:
            return f"tuple[{', '.join(item_annotation for _ in range(self.length_range.min))}]"
        ctx.require_annotated()
        return f"Annotated[list[{item_annotation}], {self.length_range.to_annotation_suffix(ctx)}]"

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        return [f"type {class_name}{ctx.type_params_suffix()} = {self.to_annotation(ctx, PairSchema.nested_struct_name(class_name))}"]


class TupleSchema(BaseSchema):
    """Tuples aren't used that much, there's only 2 cases of them:
    - ::java::data::timeline::CubicBezierEase
    - ::java::pack::PackFormat
    Length is either 2 or 4.
    """
    kind: Literal["tuple"] = Field(repr=False)
    items: list[IntSchema] | list[FloatSchema]  # Make this use discriminator="kind".

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return f"tuple[{', '.join(item.to_annotation(ctx) for item in self.items)}]"


class IntArraySchema(BaseSchema):
    """An ordered list of 32-bit integers. Note that [I;1,2,3] and [1,2,3] are considered different types: the second one is a [NBT List / JSON Array] list."""
    kind: Literal["int_array"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value_range: ValueRange | None = Field(default=None, alias="valueRange")

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        if self.has_attribute("uuid"):  # [I; a, b, c, d]
            return self._minecraft_type("MinecraftUUID", ctx)
        array_type_annotation = IntSchema(kind="int", attributes=self.attributes, valueRange=self.value_range)
        list_schema_proxy = ListSchema(kind="list", attributes=self.attributes, item=array_type_annotation, lengthRange=self.length_range)
        return list_schema_proxy.to_annotation(ctx)


class EnumSchema(BaseSchema):
    kind: Literal["enum"] = Field(repr=False)
    enum_kind: Literal["byte", "int", "string"] = Field(alias="enumKind")
    values: list[EnumValue]

    @model_validator(mode="after")
    def prune_values_on_version(self) -> Self:
        self.values = [value for value in self.values if is_valid_with_attributes(value.attributes)]
        return self

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        enum_kind = "StrEnum" if self.enum_kind == "string" else "IntEnum"
        ctx.required_imports.add(Import("enum", enum_kind, False))
        lines = [f"class {class_name}({enum_kind}):"] + [
            f"    {value.identifier.upper()} = {value.to_annotation()}{value.description_comment_or_empty}"
            for value in self.values
        ]
        return lines if self.values else lines + ["    pass"]


# ==================================================================================================================================
# Meta types

type ConcreteSchemaTypeArgTypes = (
    AnySchema | ByteSchema | ConcreteSchema | DispatcherSchema | FloatSchema | DoubleSchema | IndexedSchema
    | IntSchema | ListSchema | ReferenceSchema | StringSchema | StructSchema | UnionSchema
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
    (Must be 0 or above)
    """
    kind: Literal["concrete"]
    child: ReferenceSchema | DispatcherSchema
    type_args: list[Annotated[ConcreteSchemaTypeArgTypes, Field(discriminator="kind")]] = Field(default_factory=list, alias="typeArgs")

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        runtime_ctx = ctx.copy()
        runtime_ctx.allow_numeric_type_arg_shortcuts = True
        runtime_ctx.require_runtime_imports = True
        # We ommit the "type" so we can bind them, and then other things can inherit this binding.
        return [f"{class_name} = {self.to_annotation(runtime_ctx, class_name)}"]

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        child_annotation = (
            self.child.to_annotation(ctx, type_args=self.type_args)
            if isinstance(self.child, DispatcherSchema)
            else self.child.to_annotation(ctx)
        )
        type_arg_annotations: list[str] = []
        for type_arg in self.type_args:
            if isinstance(type_arg, StructSchema):
                type_arg_annotations.append(type_arg.to_materialized_annotation(f"{nested_struct_name}TypeArg", ctx))
            else:
                type_arg_annotations.append(type_arg.to_annotation(ctx))
        concrete_annotation = (
            f"{child_annotation}[{', '.join(type_arg_annotations)}]"
            if isinstance(self.child, ReferenceSchema)
            else child_annotation
        )
        # Optionally allow passing numeric primitive kind(s) directly alongside the concrete wrapper.
        shortcut_annotations = [
            type_arg.to_annotation(ctx) for type_arg in self.type_args if isinstance(type_arg, (IntSchema, FloatSchema, DoubleSchema))
        ] if ctx.allow_numeric_type_arg_shortcuts else []
        # This allows you to omit "MinMaxBounds" and such, which generates `MinMaxBounds[int] | int`, QoL
        return " | ".join([concrete_annotation] + shortcut_annotations)


class IndexedSchema(BaseSchema):
    """Is an index into a registry, with presets for defaults, fallbacks, etc."""
    kind: Literal["indexed"] = Field(repr=False)
    child: DispatcherSchema
    parallel_indices: list[StaticIndexSchema | DynamicIndexSchema] = Field(default_factory=list, alias="parallelIndices")

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        return " | ".join(
            candidate.to_nested_annotation(ctx, f"{nested_struct_name}{index}")
            for index, candidate in enumerate(ctx.schema_graph.annotation_candidates(self), 1)
        )


class ReferenceSchema(BaseSchema):
    """References another model/schema by path."""
    kind: Literal["reference"] = Field(repr=False)
    path: str

    @staticmethod
    def collect_reference_paths(value: BaseSchema, template_paths: set[str]) -> set[str]:
        """Collect valid reference paths, ignoring template roots."""
        if isinstance(value, ReferenceSchema):
            if not is_valid_with_attributes(value.attributes) or value.path in template_paths:
                return set()
            return {value.path}

        refs: set[str] = set()
        for field in type(value).model_fields:
            child = getattr(value, field)
            if isinstance(child, BaseSchema):
                refs |= ReferenceSchema.collect_reference_paths(child, template_paths)
            elif isinstance(child, list):
                for item in child:
                    refs |= ReferenceSchema.collect_reference_paths(item, template_paths)
        return refs

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        path, name = symbol_path_to_import_string_and_name(self.path)
        maybe_aliased_name = f"{name}_alias" if class_name == name else name
        import_identifier = f"{name} as {maybe_aliased_name}" if class_name == name else name
        ctx.required_imports.add(Import(path, f"{import_identifier}", type_checking_only=False))
        return [f"type {class_name} = {maybe_aliased_name}"]

    def to_annotation(self, ctx: SingleSymbolContext) -> str:
        return ctx.add_import_by_symbol_path(self.path)  # Make sure we import the referenced symbol


type UnionSchemaMemberTypes = (
    ListSchema | StringSchema | ReferenceSchema | DispatcherSchema | ConcreteSchema | BooleanSchema | StructSchema
    | UnionSchema | LiteralSchema | IntSchema | IndexedSchema | FloatSchema | DoubleSchema | IntArraySchema | TupleSchema | ByteSchema | ShortSchema
    | LongSchema
)


class UnionSchema(BaseSchema):
    """Allows x OR y type schemas/definitions"""
    kind: Literal["union"] = Field(repr=False)
    members: list[Annotated[UnionSchemaMemberTypes, Field(discriminator="kind")]]

    @model_validator(mode="after")
    def prune_members_on_version(self) -> Self:
        # Remove members that aren't valid for the current version
        self.members = [member for member in self.members if is_valid_with_attributes(member.attributes)]
        return self

    @model_validator(mode="after")
    def give_members_uuid_attribute(self) -> Self:
        # e.g. #[uuid] (int[] @ 4 | string) - every member is a form of the UUID, so render them as such
        if self.has_attribute("uuid"):
            for member in self.members:
                if not member.has_attribute("uuid"):
                    member.attributes.append(Attribute(name="uuid"))
        return self

    def _render_members(self, nested_name: str | None, ctx: SingleSymbolContext, declare_structs: bool) -> tuple[list[str], list[str]]:
        """Render union annotations and any required sibling struct declarations.
        With `declare_structs`, struct members are declared as their own sibling classes (for the union alias to name)."""
        declarations: list[str] = []
        annotations: list[str] = []
        nested_member_count = sum(member.contains_inline_struct() for member in self.members)
        nested_member_index = 0

        for member in self.members:
            member_name = nested_name
            if member.contains_inline_struct():
                nested_member_index += 1
                if nested_member_count > 1:
                    member_name = f"{nested_name}{nested_member_index}"
            if declare_structs and isinstance(member, StructSchema):
                assert member_name is not None
                declarations.extend(member.to_python_code(member_name, ctx) + [""])
                annotations.append(member_name)
            else:
                annotations.append(member.to_nested_annotation(ctx, member_name))

        return declarations, list(dict.fromkeys(annotations)) or ["None"]  # De-duplicated, and an empty union is just None

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        _, annotations = self._render_members(nested_struct_name, ctx, declare_structs=False)
        return " | ".join(annotations)

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        return self.to_annotation(ctx, nested_struct_name)

    @staticmethod
    def _render_union_alias(class_name: str, annotations: list[str], discriminator: str | None, ctx: SingleSymbolContext) -> str:
        """`type <class_name> = A | B`, wrapped in `Annotated[..., Field(discriminator=...)]` when there's a discriminator."""
        union_annotation = " | ".join(annotations)
        if discriminator is None:
            return f"type {class_name} = {union_annotation}"

        ctx.require_annotated()
        ctx.required_imports.add(Import("pydantic", "Field", False))
        return (
            f"type {class_name} = Annotated[\n"
            f"    {union_annotation},\n"
            f"    Field(discriminator={discriminator!r}),\n"
            "]"
        )

    @staticmethod
    def _literal_discriminator_field(schemas: list[StructSchema]) -> str | None:
        """Find a shared string-literal field whose value uniquely identifies each model."""
        if len(schemas) < 2:
            return None

        string_literals_per_schema = [
            {
                PairSchema.clean_key(field.key): field.type.value.value
                for field in schema.fields
                if isinstance(field, PairSchema)  # For mypy
                and isinstance(field.key, str)
                and isinstance(field.type, LiteralSchema)
                and isinstance(field.type.value.value, str)
            }
            for schema in schemas
        ]
        for field_name in string_literals_per_schema[0]:
            values = [string_literals[field_name] for string_literals in string_literals_per_schema]
            if len(set(values)) == len(values):  # They're all unique
                return field_name
        return None

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        if len(self.members) == 1:  # Some objects are (since, A) | (until, B) - collapse into just A
            return self.members[0].to_python_code(class_name, ctx)

        # Materialize struct members as concrete sibling symbols so the union alias can reference them.
        declarations, annotations = self._render_members(f"{class_name}Struct", ctx, declare_structs=True)
        try:
            resolved_members = [ctx.schema_graph.resolve(member) for member in self.members]
        except KeyError:  # A member is an unresolved type param (e.g. T), so it can't be a struct
            resolved_members = []
        struct_members = [resolved for resolved in resolved_members if isinstance(resolved, StructSchema)]
        # Only discriminate when every member is a struct, and none of them got merged as duplicates
        all_distinct_structs = len(struct_members) == len(self.members) == len(annotations)
        discriminator = self._literal_discriminator_field(struct_members) if all_distinct_structs else None
        return declarations + [self._render_union_alias(class_name, annotations, discriminator, ctx)]


type PairSchemaTypes = (
    IntSchema | FloatSchema | DoubleSchema | ConcreteSchema | ListSchema | UnionSchema | ReferenceSchema | BooleanSchema | AnySchema | TupleSchema
    | IndexedSchema | StringSchema | StructSchema | ByteSchema | DispatcherSchema | IntArraySchema | ShortSchema | LongSchema
    | LiteralSchema
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

    @staticmethod
    def clean_key(key: str | StringSchema | ReferenceSchema) -> str:
        # These two isinstance checks aren't perfect, but there's only 3 tiny cases in the whole of symbols.json
        if isinstance(key, ReferenceSchema):
            return symbol_path_to_object_name(key.path)
        if isinstance(key, StringSchema):
            return "key_name"
        return key if key not in {"from", "with"} else f"{key}_"

    @staticmethod
    def pascal_case(key: str) -> str:
        """snake_case and lowercase keys become PascalCase, anything else (e.g. camelCase) is left alone."""
        if "_" in key or key.islower():
            return "".join(part[:1].upper() + part[1:] for part in key.split("_") if part)
        return key

    @staticmethod
    def nested_struct_name(key: str) -> str:
        """For structs attributes that are also structs, we need to figure out the name of the new struct, e.g. BlockStateStruct"""
        return f"{PairSchema.pascal_case(key)}Struct"

    @property
    def formatted_default_value(self) -> str | None:
        """Return a string representing the default value for this field, or None if there is no default."""
        if isinstance(self.type, LiteralSchema):
            return repr(self.type.value.value)
        if self.optional:
            return "None"
        return None

    def to_field_line(self, ctx: SingleSymbolContext) -> str | None:
        """Render this pair as a class field, e.g. `    count: int | None = None  # How many`.
        Returns None for empty unions, which represent weird stuff - skip so parent members can remain authoritative."""
        name = PairSchema.clean_key(self.key)  # type: ignore[arg-type]
        annotation = self.type.to_nested_annotation(ctx, PairSchema.nested_struct_name(name))
        if annotation == "None":
            # This is a weird case where the union is empty, only for CustomName and CustomNameVisible, it's weird.
            return None

        default: str | None = self.formatted_default_value
        # === A field named after a type in this file (e.g. `BlockState: BlockState`) would shadow that type, so rename it.
        if name in ctx.allocated_name_by_identity.values():
            name += "_"
        if isinstance(self.key, str) and name != self.key:  # Renamed (e.g. `from_`), so alias it back to the real JSON key
            ctx.required_imports.add(Import("pydantic", "Field", False))
            default = f"Field({'' if default is None else f'default={default}, '}alias={self.key!r})"
        # ===
        return f"    {name}: {annotation if not self.optional else annotation + ' | None'}{'' if default is None else f' = {default}'}{self.description_or_empty}"


class SpreadFieldSchema(BaseSchema):
    """An inliner, for spread (inheritence).
    E.g. Suspicious stew has attributes {
        "kind": "spread", "type": {"kind": "reference", "path": "::java::world::item::ItemBase"}
    }
    So they get inlined (suspicious stew now gets all the attributes from ItemBase).
    """
    kind: Literal["spread"] = Field(repr=False)
    type: Annotated[
        ReferenceSchema | ConcreteSchema | DispatcherSchema | StructSchema | UnionSchema,
        Field(discriminator="kind"),
    ]

    def _unravel_reference(self) -> ReferenceSchema | None:
        """Returns a reference, or a concrete schema's reference, or None"""
        if isinstance(self.type, ReferenceSchema):
            return self.type
        if isinstance(self.type, ConcreteSchema) and isinstance(self.type.child, ReferenceSchema):
            return self.type.child
        # A concrete dispatcher never references one schema (it's a list of them), so we return None for those too.
        # e.g. parallel_indices=[DynamicIndexSchema(accessor=['type'])] registry='minecraft:int_provider'
        return None

    @classmethod
    def collect_inherited_base_names(cls, fields: list[PairSchema | SpreadFieldSchema], ctx: SingleSymbolContext) -> list[str]:
        """Return a list of strings representing inherited classes, e.g. class MyClass(`<x>`, `<y>`) """
        base_names: set[str] = set()
        for spread_field_schema in [fld for fld in fields if isinstance(fld, SpreadFieldSchema)]:
            strict_ctx = ctx.copy()
            strict_ctx.allow_numeric_type_arg_shortcuts = False  # Don't allow inherited | float, for example.
            strict_ctx.require_runtime_imports = True
            # Keep concrete spread type arguments in inheritance, e.g. UniformIntProvider[T].
            reference: ReferenceSchema | None = spread_field_schema._unravel_reference()
            if reference is not None and reference.path not in ctx.local_type_params:
                base_names.add(spread_field_schema.type.to_annotation(strict_ctx))
            if isinstance(spread_field_schema.type, StructSchema):
                base_names = base_names.union(SpreadFieldSchema.collect_inherited_base_names(spread_field_schema.type.fields, ctx))
        return sorted(base_names)

    @classmethod
    def filter_fields_to_pair_schemas_only(cls, fields: list[PairSchema | SpreadFieldSchema]) -> list[PairSchema]:
        """For all the fields, return only those that are `PairSchema`. \n
        If it's a struct, return **ITS** `PairSchema`s"""
        inlined_fields: list[PairSchema] = []
        for pair_field in fields:
            if isinstance(pair_field, PairSchema):
                inlined_fields.append(pair_field)
            if isinstance(pair_field, SpreadFieldSchema) and isinstance(pair_field.type, StructSchema):
                inlined_fields.extend(SpreadFieldSchema.filter_fields_to_pair_schemas_only(pair_field.type.fields))
        return inlined_fields


class TemplateTypeParam(BaseModel):
    """Represents a template type parameter path (e.g. ::java::world::item::T)."""
    path: str


class TemplateSchema(BaseSchema):
    """"
    Built-in types, e.g. `::java::data::worldgen::UniformInt`
    They always take a type, e.g. ClampedIntProvider[T]
    Essentially, these are Generics of type (normally T)
    """
    kind: Literal["template"] = Field(repr=False)
    child: Annotated[
        ConcreteSchema | FloatSchema | ListSchema | ReferenceSchema | StructSchema | UnionSchema,
        Field(discriminator="kind")
    ]
    type_params: list[TemplateTypeParam] = Field(default_factory=list, alias="typeParams")

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        ctx.local_type_params.update(type_param.path for type_param in self.type_params)
        # If it's a Union (with a struct), just return the struct's code, because the union is just a wrapper for it.
        # Otherwise, return the child schema's code.
        if isinstance(self.child, UnionSchema):
            struct_member = next(member for member in self.child.members if isinstance(member, StructSchema))  # Always exactly 1
            return struct_member.to_python_code(class_name, ctx)
        return self.child.to_python_code(class_name, ctx)


class StructSchema(BaseSchema):
    kind: Literal["struct"]
    fields: list[Annotated[PairSchema | SpreadFieldSchema, Field(discriminator="kind")]]

    def contains_inline_struct(self) -> bool:
        return True

    def to_nested_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None) -> str:
        """Structs used inline (e.g. as a field's type) get generated as their own class, named `nested_struct_name`."""
        assert nested_struct_name is not None, "Inline structs need a name to be generated with"
        return self.to_materialized_annotation(nested_struct_name, ctx)

    @model_validator(mode="after")
    def prune_fields_on_version(self) -> Self:
        # All the PairSchema and SpreadFieldSchema fields have attributes, so we can filter them based on the current version.
        self.fields = [field for field in self.fields if is_valid_with_attributes(field.attributes)]
        return self  # Has to return self

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
        plain_pairs      = [field for field in self.fields if isinstance(field, PairSchema) and isinstance(field.key, str)]  # fmt: skip
        schema_key_pairs = [field for field in self.fields if isinstance(field, PairSchema) and not isinstance(field.key, str)]
        return schema_key_pairs[0] if len(schema_key_pairs) == 1 and not plain_pairs else None

    def _spread_dispatcher(self) -> DispatcherSchema | None:
        """Return the dispatcher of the supported selector-based union spread, if this struct has one.

        mcdoc represents some unions as *shared struct fields* plus a
        dispatcher spread. The dispatcher's single string accessor names the shared
        field that selects a registry branch. We expand that shape into one dataclass
        per branch so each selector value stays correlated with its fields.

        Distribution is only unambiguous when there is exactly one dispatcher spread,
        structs with zero or multiple such spreads continue through normal rendering
        """
        dispatchers = [
            field.type for field in self.fields
            if isinstance(field, SpreadFieldSchema) and isinstance(field.type, DispatcherSchema)
        ]
        if len(dispatchers) != 1:  # Ambiguous, either 0 or > 1
            return None
        if dispatchers[0].dynamic_selector_field is None:  # Not selected by one of our own fields
            return None
        return dispatchers[0]

    def _dispatcher_variant(
        self, dispatcher: DispatcherSchema, branch_struct: StructSchema, registry_key: str, branch_reference: ReferenceSchema | None,
    ) -> StructSchema:
        """Build the struct for one entry in the dispatcher's registry.

        Start with deep copies of the original struct's shared fields (minus the dispatcher spread, which this
        branch replaces). For a normal key, narrow the selector field to its namespaced literal value, e.g. the
        `ore_drops` branch changes `formula: ApplyBonusFormula` to `formula: Literal["minecraft:ore_drops"]`.
        Keys beginning with `%` are fallback entries rather than real selector values, so they're left unchanged.

        Then add the branch's own fields: either by inheriting the branch (if it's a class), or by copying its
        string-keyed pairs (schema-keyed pairs are arbitrary map entries, so can't become named fields).
        """
        fields = [field.model_copy(deep=True) for field in self.fields if field.type is not dispatcher]  # i.e. not the spread
        if not registry_key.startswith("%"):
            for field in fields:
                if isinstance(field, PairSchema) and field.key == dispatcher.dynamic_selector_field:
                    field.type = LiteralSchema(kind="literal", value=StringSchema(kind="string", value=f"minecraft:{registry_key}"))

        if branch_reference is not None:
            fields.append(SpreadFieldSchema(kind="spread", type=branch_reference.model_copy(deep=True)))
        else:
            fields.extend(
                field.model_copy(deep=True)
                for field in branch_struct.fields
                if not isinstance(field, PairSchema) or isinstance(field.key, str)
            )
        return StructSchema(kind="struct", fields=fields)

    def _dispatcher_variants(self, class_name: str, dispatcher: DispatcherSchema, ctx: SingleSymbolContext) -> list[tuple[str, StructSchema]]:
        """Resolve every registry entry into a uniquely named specialized struct."""
        variants: list[tuple[str, StructSchema]] = []
        for key, branch in ctx.schema_graph.dispatchers[dispatcher.registry].items():  # Already filtered to the current version
            resolved = ctx.schema_graph.resolve(branch)
            branch_struct = resolved if isinstance(resolved, StructSchema) else StructSchema(kind="struct", fields=[])
            variant_name = ctx.allocate_name(f"{class_name}{DispatcherSchema.branch_name_suffix(key)}", branch_struct.model_dump_json(by_alias=True))
            # Branches that are classes get inherited, rather than having their fields copied in.
            branch_reference = branch if isinstance(branch, ReferenceSchema) and ctx.schema_graph.is_runtime_class(branch) else None
            variant = self._dispatcher_variant(dispatcher, branch_struct, key, branch_reference)
            variants.append((variant_name, variant))
        return variants

    @staticmethod
    def _render_variants(class_name: str, variants: list[tuple[str, StructSchema]], discriminator: str | None, ctx: SingleSymbolContext) -> list[str]:
        """Render each (name, struct) variant, followed by `type <class_name> = <variant1> | <variant2> | ...`"""
        rendered = [line for name, variant in variants for line in variant.to_python_code(name, ctx) + [""]]
        # Ends with a blank line like classes do, so nested variant unions get two blank lines after them too
        return rendered + [UnionSchema._render_union_alias(class_name, [name for name, _ in variants], discriminator, ctx), ""]

    def _render_dispatcher_spread(self, class_name: str, ctx: SingleSymbolContext) -> list[str] | None:
        """Render distributed branch dataclasses followed by their union alias."""
        if (dispatcher := self._spread_dispatcher()) is None:
            return None
        variants = self._dispatcher_variants(class_name, dispatcher, ctx)
        # Only when each variant is one class: a variant that's itself a union (e.g. each Dialog type splits again by its
        # after_action) has several classes with the same selector value, which pydantic rejects as a discriminator.
        all_classes = all(ctx.schema_graph.is_runtime_class(variant) for _, variant in variants)
        discriminator = UnionSchema._literal_discriminator_field([variant for _, variant in variants]) if all_classes else None
        return self._render_variants(class_name, variants, discriminator, ctx)

    def _render_alias_spread(self, class_name: str, ctx: SingleSymbolContext) -> list[str] | None:
        """Spreads of things that aren't classes (e.g. an alias to a union of structs) can't be inherited, so instead,
        copy each struct's fields into its own variant of this struct, and union them."""
        for spread in (field for field in self.fields if isinstance(field, SpreadFieldSchema)):
            if ctx.schema_graph.is_runtime_class(spread.type):
                continue
            resolved = ctx.schema_graph.resolve(spread.type)
            candidates: list[BaseSchema] = list(resolved.members) if isinstance(resolved, UnionSchema) else [resolved]
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
            named_variants: list[tuple[str, StructSchema]] = [(f"{class_name}Struct{index}", variant) for index, variant in enumerate(variants, 1)]
            return self._render_variants(class_name, named_variants, None, ctx)
        return None

    def _mapping_alias_annotation(self, ctx: SingleSymbolContext, value_struct_name: str) -> str | None:
        """Returns the mapping alias dict (i.e. dict[<x>, <x>]) for a struct, or None if it's not that kind of struct."""
        field = self._mapping_pair()
        if field is None:
            return None
        value_annotation = field.type.to_nested_annotation(ctx, value_struct_name)
        assert not isinstance(field.key, str)
        if isinstance(field.key, DispatcherSchema):  # Annotate the registry (TODO: Make this better.)
            ctx.require_annotated()  # vanilla_mcdoc\data\advancement\predicate\BlockPredicateState.py
            return f"dict[Annotated[str, 'Registry(\"{field.key.registry.removeprefix('mcdoc:')}\")'], {value_annotation}]"
        return f"dict[{field.key.to_annotation(ctx)}, {value_annotation}]"

    def to_materialized_annotation(self, class_name: str, ctx: SingleSymbolContext) -> str:
        """Both adds itself to the list of created dataclasses, plus returns the annotation materialized."""
        mapping_alias = self._mapping_alias_annotation(ctx, f"{class_name}ValueStruct")
        if mapping_alias is not None:  # Mappings are just dict[<x>, <x>], so inline them rather than making a type alias.
            return mapping_alias
        class_name = ctx.allocate_name(class_name, self.model_dump_json(by_alias=True))
        helper_ctx = ctx.copy()
        helper_ctx.resource_dir = None  # Helper structs (e.g. a field's struct) aren't the resource itself
        ctx.add_dataclass(self.to_python_code(class_name, helper_ctx))
        return f"{class_name}{ctx.type_params_suffix()}"

    def _render_model(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        # Structs' inherited children, e.g. class MyClass(PredicateOffset), or GeneratedModel if there's none.
        base_names = SpreadFieldSchema.collect_inherited_base_names(self.fields, ctx)
        if not base_names:
            ctx.required_imports.add(Import(f"{GENERATED_SYMBOLS_DIRECTORY.name}.base", "GeneratedModel", False))
            base_names = ["GeneratedModel"]
        if type_params := ctx.type_params_suffix():
            ctx.required_imports.add(Import("typing", "Generic", False))
            base_names.append(f"Generic{type_params}")

        lines = [f"class {class_name}({', '.join(base_names)}):"]
        if ctx.resource_dir is not None:  # A root resource (or one of its variants), e.g. a recipe, knows its pack directory
            ctx.required_imports.add(Import("typing", "ClassVar", False))
            lines.append(f"    __resource_dir__: ClassVar[str] = {ctx.resource_dir!r}\n")
        pair_fields = SpreadFieldSchema.filter_fields_to_pair_schemas_only(self.fields)
        if not pair_fields:
            lines.append("    pass")
        lines.extend(line for pair_field in pair_fields if (line := pair_field.to_field_line(ctx)) is not None)
        return lines + [""]

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        """A struct renders as the first of these that applies:
        1. A spread of a non-class alias  -> one class per struct it could be, plus their union
        2. A spread of a dispatcher       -> one class per registry entry, plus their (discriminated) union
        3. A mapping                      -> `type <class_name> = dict[<key>, <value>]`
        4. Anything else                  -> a normal class
        """
        if (alias_spread := self._render_alias_spread(class_name, ctx)) is not None:
            return alias_spread
        if (dispatcher_union := self._render_dispatcher_spread(class_name, ctx)) is not None:
            return dispatcher_union
        if (mapping_alias := self._mapping_alias_annotation(ctx, f"{class_name}ValueStruct")) is not None:
            return [f"type {class_name}{ctx.type_params_suffix()} = {mapping_alias}\n"]

        # Discover unresolved symbolic refs before rendering the Generic[...] base.
        for field in SpreadFieldSchema.filter_fields_to_pair_schemas_only(self.fields):
            if isinstance(field.type, ReferenceSchema) and field.type.path not in ROOT_SYMBOLS_KEYS["mcdoc"]:
                ctx.local_type_params.add(field.type.path)

        return self._render_model(class_name, ctx)


# ==================================================================================================================================
# Grossness


class DynamicIndexAccessorItem(BaseModel):
    """Represents an item in the accessor list of a DynamicIndexSchema.  \n
    It's a keyword mapping to parent or key, e.g. {"keyword": "parent"} or {"keyword": "key"}."""
    keyword: Literal["key", "parent"]


class DynamicIndexSchema(BaseSchema):
    kind: Literal["dynamic"] = Field(repr=False)
    accessor: list[str | DynamicIndexAccessorItem]


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
    def dynamic_selector_field(self) -> str | None:
        """Return the sibling field that selects the branch (e.g. `type`), or None if it's selected some other way,
        e.g. via the parent (`[%parent, "BlockState"]`) or a nested field (`["output_state", "id"]`)."""
        index = self.parallel_indices[0]
        if not isinstance(index, DynamicIndexSchema):
            return None
        return index.accessor[0] if len(index.accessor) == 1 and isinstance(index.accessor[0], str) else None

    @staticmethod
    def branch_name_suffix(key: str) -> str:
        """The part of a branch's class name that comes from its registry key, e.g. "ore_drops" -> "OreDrops".
        `%none` is the branch for when the selector field isn't given at all, so it's the Default (no registry has a real
        "default" key), not "None", which would clash with real "none" keys (e.g. a dialog's after_action)."""
        if key == "%none":
            return "Default"
        return PairSchema.pascal_case("".join(character if character.isalnum() else "_" for character in key.lstrip("%")))

    def to_annotation(
        self, ctx: SingleSymbolContext, nested_struct_name: str | None = None, type_args: list[ConcreteSchemaTypeArgTypes] | None = None,
    ) -> str:
        registry = ctx.schema_graph.dispatchers[self.registry]
        index = self.parallel_indices[0]  # Always 1
        if isinstance(index, DynamicIndexSchema) or index.value == "%fallback":
            candidates = list(registry.items())
        else:
            key = index.value.removeprefix("minecraft:")
            candidates = [(key, registry[key])]

        registry_name = PairSchema.pascal_case(self.registry.split(":")[-1])
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
            branch_name = f"{base_name}{self.branch_name_suffix(key)}"
            annotations.append(branch.to_nested_annotation(ctx, branch_name))

        return " | ".join(dict.fromkeys(annotations))


class TreeSchema(BaseSchema):
    """Represents a 'tree' structure, found inside an Attribute's value.
    Example: ::java::data::worldgen::attribute::PositionalEnvironmentAttribute """
    kind: Literal["tree"] = Field(repr=False)
    values: dict[str, TreeSchema | LiteralSchema]


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================

SCHEMA_MODELS: list[type[BaseSchema]] = [
    LiteralSchema, IntSchema, StringSchema, FloatSchema, DoubleSchema, BooleanSchema, ShortSchema, LongSchema, ByteSchema, AnySchema,
    ListSchema, TupleSchema, IntArraySchema, EnumSchema,
    ConcreteSchema, IndexedSchema, ReferenceSchema, UnionSchema, PairSchema, SpreadFieldSchema, TemplateSchema, StructSchema,
    DynamicIndexSchema, StaticIndexSchema, DispatcherSchema, TreeSchema,
]

# Each model's `kind` is a single Literal (e.g. Literal["int"]), so get_args gives us ("int",).
# e.g. {"literal": LiteralSchema, "int": IntSchema, ...}
KIND_TO_MODEL: dict[str, type[BaseSchema]] = {get_args(model.model_fields["kind"].annotation)[0]: model for model in SCHEMA_MODELS}
