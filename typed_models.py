import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal, Self, get_args

from pydantic import BaseModel, Field, model_validator

from context import Import, SingleSymbolContext
from minecraft_registry import known_registry_alias
from static_symbols.minecraft_types import IdSpec
from utils import GENERATED_SYMBOLS_DIRECTORY, REGISTRIES, ROOT_SYMBOLS_KEYS, SAFE_GUARD_JAVA_NUMBERS, is_valid_with_attributes, symbol_path_to_import_string_and_name

if TYPE_CHECKING:
    from schema_resolution import SchemaGraph


def description_comment(description: str) -> str:
    """A description as a comment for the end of the line, e.g. "  # How many", or "" if there isn't one"""
    return f"  # {description.replace('\\\n', '\n').replace('\n', ' ').strip()}" if description else ""


class BaseSchema(BaseModel):
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    @property
    def contains_inline_struct(self) -> bool:
        """Return whether this schema needs a generated name for an inline struct."""
        return False

    def has_attribute(self, name: str) -> bool:
        return any(attribute.name == name for attribute in self.attributes)

    def child_schemas(self) -> Iterator[BaseSchema]:
        """The schemas directly inside this one, e.g. a list's item, or each of a struct's fields"""
        for field_name in type(self).model_fields:
            value = getattr(self, field_name)
            for child in value if isinstance(value, list) else [value]:
                if isinstance(child, BaseSchema):
                    yield child

    @staticmethod
    def _minecraft_type(name: str, ctx: SingleSymbolContext) -> str:
        """Use one of the hand-written types from static_symbols/minecraft_types.py (copied into the package), e.g. MinecraftUUID"""
        ctx.required_imports.add(Import(f"{GENERATED_SYMBOLS_DIRECTORY.name}.minecraft_types", name))
        return name

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        """Generate the actual Python, for most things, this is just the alias to the annotation"""
        return [f"type {class_name} = {self.to_annotation(ctx)}"]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        """The annotation for a value of this schema, e.g. `list[int]`. A struct written inline in it becomes its own class,
        named nested_struct_name (or something based on it), so schemas that can't have one just ignore it."""
        raise NotImplementedError(f"This should never get called directly on a {self.__class__.__name__}")  # pragma: no cover

    def remove_version_data(self) -> BaseSchema:
        self.attributes = [x for x in self.attributes if x.name not in {"since", "until", "deprecated"}]
        for child in self.child_schemas():
            child.remove_version_data()
        return self


class Attribute(BaseModel):
    """Represents a single attribute with a name and a structured value."""
    name: str
    value: Annotated[LiteralSchema | TreeSchema | DispatcherSchema | ReferenceSchema, Field(discriminator="kind")] | None = None

    @property
    def plain_value(self) -> object:
        """The value as plain Python, e.g. "hex_rgb" for #[color="hex_rgb"], or {"registry": "item"} for #[id(registry="item")]"""
        return self._plain_value(self.value)

    @classmethod
    def _plain_value(cls, schema: BaseSchema | None) -> object:
        if schema is None:
            return None
        if isinstance(schema, LiteralSchema):
            return schema.value.value
        assert isinstance(schema, TreeSchema)  # Dispatchers and references are never used as values
        values = {key: cls._plain_value(value) for key, value in schema.values.items()}
        return tuple(values[key] for key in sorted(values, key=int)) if all(key.isdigit() for key in values) else values

    def to_id_spec(self) -> IdSpec | None:
        if self.name != "id":
            return None
        return IdSpec.from_value(self.plain_value)  # type: ignore[arg-type]

    def to_string_pattern(self) -> str | None:
        """The regex a string with this attribute must contain, matching how Spyglass validates them, e.g.
        #[match_regex="^[A-Za-z0-9_]*$"], #[integer] (a string of digits) or #[color="hex_rgb"] (starts with a #)"""
        if self.name == "match_regex":
            return str(self.plain_value)
        if self.name == "integer":
            return r"^-?\d+$"
        if self.name == "color" and self.plain_value == "hex_rgb":
            return "^#"
        return None


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

    def to_field(self, ctx: SingleSymbolContext) -> str:
        """e.g. Field(ge=0, lt=10), for the metadata of an Annotated[int, ...]"""
        ctx.required_imports.add(Import("pydantic", "Field"))
        greater_than = "ge" if self.kind in {0, 1} else "gt"
        less_than    = "le" if self.kind in {0, 2} else "lt"  # fmt: skip
        return f"Field({greater_than}={self.min}{'' if self.max is None else f', {less_than}={self.max}'})"


class LengthRange(BaseModel):
    kind: Literal[0] = Field(default=0, repr=False)  # Not sure what other values this can be?
    min: int | None = None  # Only like one of these has a max but no min...
    max: int | None = None

    def to_field(self, ctx: SingleSymbolContext) -> str:
        """e.g. Field(min_length=1, max_length=16), for the metadata of an Annotated[str, ...] or Annotated[list[...], ...]"""
        ctx.required_imports.add(Import("pydantic", "Field"))
        lengths = {"min_length": self.min, "max_length": self.max}
        return f"Field({', '.join(f'{name}={length}' for name, length in lengths.items() if length is not None)})"


class EnumValue(BaseModel):
    identifier: str
    value: str | int | float | bool
    description: str = Field(default="", repr=False, alias="desc")
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def to_annotation(self) -> str:
        return repr(self.value).replace("'", '"')  # This fixes it so strings are handled properly


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


class LiteralSchema(BaseSchema):
    """Represents a literal value, often found inside an Attribute's value.
    Also normally used to just set until/since version (80% + of cases)
    """
    kind: Literal["literal"] = Field(repr=False)
    value: Annotated[StringSchema | IntSchema | BooleanSchema | DoubleSchema, Field(discriminator="kind")]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        ctx.required_imports.add(Import("typing", "Literal"))
        value = self.value.value
        if isinstance(value, str) and value.startswith("minecraft:"):  # Resource locations work with or without the namespace
            return f"Literal[{value!r}, {value.removeprefix('minecraft:')!r}]"
        return f"Literal[{value!r}]"


# ==================================================================================================================================
# Primitive Schemas (string, int, float, boolean, etc.)


class NumericSchema(BaseSchema):
    """What all the number types have in common, e.g. `int @ 0..10` is an IntSchema with a value_range"""
    value_range: ValueRange | None = Field(default=None, alias="valueRange")

    python_type: ClassVar[Literal["int", "float"]]
    min_value_internally: ClassVar[float]  # The range Java can store it in, for SAFE_GUARD_JAVA_NUMBERS
    max_value_internally: ClassVar[float]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        value_range = self.value_range
        if value_range is None and SAFE_GUARD_JAVA_NUMBERS:  # pragma: no cover
            value_range = ValueRange(min=self.min_value_internally, max=self.max_value_internally)
        if value_range is None:
            return self.python_type
        metadata = [value_range.to_field(ctx)]
        divisible_by = next((attribute.plain_value for attribute in self.attributes if attribute.name == "divisible_by"), None)
        if divisible_by is not None:
            metadata.append(f"Field(multiple_of={divisible_by})")
        ctx.require_annotated()
        return f"Annotated[{self.python_type}, {', '.join(metadata)}]"


class IntSchema(NumericSchema):
    """A signed 32-bit integer, ranging from -2,147,483,648 to 2,147,483,647 (inclusive)"""
    kind: Literal["int"] = Field(repr=False)
    value: int | None = None  # For literal ints

    python_type = "int"
    min_value_internally = -2_147_483_648
    max_value_internally = 2_147_483_647


class ByteSchema(NumericSchema):
    """A signed 8-bit integer, ranging from -128 to 127 (inclusive)."""
    kind: Literal["byte"] = Field(repr=False)

    python_type = "int"
    min_value_internally = -128
    max_value_internally = 127


class ShortSchema(NumericSchema):
    """A signed 16-bit integer, ranging from -32,768 to 32,767 (inclusive)."""
    kind: Literal["short"] = Field(repr=False)

    python_type = "int"
    min_value_internally = -32_768
    max_value_internally = 32_767


class LongSchema(NumericSchema):
    """A signed 64-bit integer, ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (inclusive)."""
    kind: Literal["long"] = Field(repr=False)

    python_type = "int"
    min_value_internally = -9_223_372_036_854_775_808
    max_value_internally = 9_223_372_036_854_775_807


class FloatSchema(NumericSchema):
    """A 32-bit, single-precision floating-point number, ranging from -3.4E38 to +3.4E38."""
    kind: Literal["float"] = Field(repr=False)

    python_type = "float"
    min_value_internally = -3.4E38
    max_value_internally = 3.4E38


class DoubleSchema(NumericSchema):
    """A 64-bit, double-precision floating-point, ranging from -1.79E308 to +1.79E308."""
    kind: Literal["double"] = Field(repr=False)
    value: float | None = None  # For literal doubles

    python_type = "float"
    min_value_internally = -1.79E308
    max_value_internally = 1.79E308


class StringSchema(BaseSchema):
    kind: Literal["string"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value: str | None = None  # For literal strings

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        if self.has_attribute("uuid"):
            return self._minecraft_type("MinecraftUUIDString", ctx)
        if self.has_attribute("url"):
            return self._minecraft_type("MinecraftURL", ctx)
        if self.length_range is not None and self.length_range.min == self.length_range.max == 0:
            # Edge case, because of this one instance:
            # https://github.com/SpyglassMC/vanilla-mcdoc/blob/main/java/assets/credits.mcdoc#L5
            # https://github.com/misode/mcmeta/blob/assets/assets/minecraft/texts/credits.json#L1998
            # Literally only one thing - ::java::assets::credits::CreditsDiscipline
            ctx.required_imports.add(Import("typing", "Literal"))
            return 'Literal[""]'

        metadata = [self.length_range.to_field(ctx)] if self.length_range is not None else []
        if (id_spec := self.id_spec()) is not None:
            self._minecraft_type("IdSpec", ctx)  # Imports it
            metadata.append(id_spec.to_annotation())  # Adds IdSpec(registry=...), for example
        # For regex patterns, we add a Field(pattern=...) to the Annotated[str, ...] type, so that pydantic can validate it.
        for pattern in (attribute.to_string_pattern() for attribute in self.attributes):
            if pattern is not None:
                ctx.required_imports.add(Import("pydantic", "Field"))
                metadata.append(f"Field(pattern={pattern!r})")

        if not metadata:
            return "str"
        ctx.require_annotated()
        annotation = f"Annotated[str, {', '.join(metadata)}]"
        known_id_alias = known_registry_alias(ctx, id_spec) if id_spec is not None else None
        return f"{annotation} | {known_id_alias}" if known_id_alias is not None else annotation

    def id_spec(self) -> IdSpec | None:
        """What its #[id] attribute says, if it has one, e.g. IdSpec(registry='item')"""
        return next((id_spec for attribute in self.attributes if (id_spec := attribute.to_id_spec()) is not None), None)


class BooleanSchema(BaseSchema):
    kind: Literal["boolean"] = Field(repr=False)
    value: bool | None = None

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        return "bool"


class AnySchema(BaseSchema):
    kind: Literal["any"] = Field(repr=False)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        ctx.required_imports.add(Import("typing", "Any"))
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

    @property
    def contains_inline_struct(self) -> bool:
        return self.item.contains_inline_struct

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        if self.has_attribute("uuid"):  # A list of 4 ints
            return self._minecraft_type("MinecraftUUID", ctx)
        item_annotation = self.item.to_annotation(ctx, nested_struct_name)
        if self.length_range is None:
            return f"list[{item_annotation}]"
        if self.length_range.min is not None and self.length_range.min == self.length_range.max:
            return f"tuple[{', '.join([item_annotation] * self.length_range.min)}]"
        ctx.require_annotated()
        return f"Annotated[list[{item_annotation}], {self.length_range.to_field(ctx)}]"

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        return [f"type {class_name}{ctx.type_params_suffix()} = {self.to_annotation(ctx, PairSchema.nested_struct_name(class_name))}"]


class TupleSchema(BaseSchema):
    """Tuples aren't used that much, there's only 2 cases of them:
    - ::java::data::timeline::CubicBezierEase
    - ::java::pack::PackFormat
    Length is either 2 or 4.
    """
    kind: Literal["tuple"] = Field(repr=False)
    items: list[Annotated[IntSchema | FloatSchema, Field(discriminator="kind")]]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        return f"tuple[{', '.join(item.to_annotation(ctx) for item in self.items)}]"


class IntArraySchema(BaseSchema):
    """An ordered list of 32-bit integers. Note that [I;1,2,3] and [1,2,3] are considered different types: the second one is a [NBT List / JSON Array] list."""
    kind: Literal["int_array"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value_range: ValueRange | None = Field(default=None, alias="valueRange")

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
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
        ctx.required_imports.add(Import("enum", enum_kind))
        lines = [f"class {class_name}({enum_kind}):"] + [
            f"    {value.identifier.upper()} = {value.to_annotation()}{description_comment(value.description)}"
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
    kind: Literal["concrete"] = Field(repr=False)
    child: ReferenceSchema | DispatcherSchema
    type_args: list[Annotated[ConcreteSchemaTypeArgTypes, Field(discriminator="kind")]] = Field(default_factory=list, alias="typeArgs")

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        runtime_ctx = ctx.copy()
        runtime_ctx.allow_template_shortcuts = True
        runtime_ctx.require_runtime_imports = True
        # We omit the "type" so we can bind them, and then other things can inherit this binding.
        return [f"{class_name} = {self.to_annotation(runtime_ctx, class_name)}"]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        if isinstance(self.child, DispatcherSchema):  # Its branches get the type args filled in
            concrete_annotation = self.child.to_annotation(ctx, type_args=self.type_args)
        else:
            child_annotation = self.child.to_annotation(ctx)
            type_arg_annotations = [  # Only ones with a struct written in them get a name, as the struct becomes a class
                type_arg.to_annotation(ctx, f"{nested_struct_name}TypeArg" if type_arg.contains_inline_struct else None)
                for type_arg in self.type_args
            ]
            concrete_annotation = f"{child_annotation}[{', '.join(type_arg_annotations)}]"
        # Not for base classes, which can't be unions
        other_members = self._other_template_members(ctx) if ctx.allow_template_shortcuts else []
        return " | ".join([concrete_annotation] + other_members)

    def _other_template_members(self, ctx: SingleSymbolContext) -> list[str]:
        """A template that's a union, e.g. MinMaxBounds<T> = `T | struct { min?: T, max?: T }`, is a class for its struct,
        so the rest of it goes wherever it's used, with the type arguments filled in, e.g. `MinMaxBounds[str] | str`."""
        template = ctx.schema_graph.symbols.get(self.child.path) if isinstance(self.child, ReferenceSchema) else None
        if not isinstance(template, TemplateSchema) or not isinstance(template.child, UnionSchema):
            return []
        arguments = dict(zip((parameter.path for parameter in template.type_params), self.type_args))
        members = [ctx.schema_graph.substitute(member, arguments) for member in template.child.members]
        return [member.to_annotation(ctx) for member in members if not isinstance(member, StructSchema)]  # The struct is the class


class IndexedSchema(BaseSchema):
    """Is an index into a registry, with presets for defaults, fallbacks, etc."""
    kind: Literal["indexed"] = Field(repr=False)
    child: DispatcherSchema
    parallel_indices: list[StaticIndexSchema | DynamicIndexSchema] = Field(default_factory=list, alias="parallelIndices")

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        return " | ".join(
            candidate.to_annotation(ctx, f"{nested_struct_name}{index}")
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
        return {path for child in value.child_schemas() for path in ReferenceSchema.collect_reference_paths(child, template_paths)}

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        if self.path in ctx.local_type_params:  # A template that's just its type param, e.g. TagEntry<E> before 1.16.2
            return [f"type {class_name}{ctx.type_params_suffix()} = {self.to_annotation(ctx)}"]
        module, name = symbol_path_to_import_string_and_name(self.path)
        local_name = f"{name}_alias" if class_name == name else name  # It can't have the same name as this alias
        ctx.required_imports.add(Import(module, name if local_name == name else f"{name} as {local_name}"))
        return [f"type {class_name} = {local_name}"]

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        annotation = ctx.add_import_by_symbol_path(self.path)  # Make sure we import the referenced symbol
        if self.has_attribute("id") and isinstance(ctx.schema_graph.symbols.get(self.path), EnumSchema):
            # An enum of ids, e.g. a loot table's `type: #[id] LootContextParamSets`, which can be written with "minecraft:" too
            return f"{self._minecraft_type('NamespacedId', ctx)}[{annotation}]"
        return annotation


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

    @property
    def contains_inline_struct(self) -> bool:
        return any(member.contains_inline_struct for member in self.members)

    @model_validator(mode="after")
    def give_members_uuid_attribute(self) -> Self:
        # e.g. #[uuid] (int[] @ 4 | string) - every member is a form of the UUID, so render them as such
        if self.has_attribute("uuid"):
            for member in self.members:
                member.attributes.append(Attribute(name="uuid"))
        return self

    def _render_members(self, nested_name: str | None, ctx: SingleSymbolContext, declare_structs: bool) -> tuple[list[str], list[str]]:
        """Render union annotations and any required sibling struct declarations.
        With `declare_structs`, struct members are declared as their own sibling classes (for the union alias to name)."""
        declarations: list[str] = []
        annotations: list[str] = []
        nested_member_count = sum(member.contains_inline_struct for member in self.members)
        nested_member_index = 0

        for member in self.members:
            member_name = nested_name
            if member.contains_inline_struct:
                nested_member_index += 1
                if nested_member_count > 1:
                    member_name = f"{nested_name}{nested_member_index}"
            if declare_structs and isinstance(member, StructSchema):
                assert member_name is not None
                declarations.extend(member.to_python_code(member_name, ctx) + [""])
                annotations.append(member_name)
            else:
                annotations.append(member.to_annotation(ctx, member_name))

        return declarations, list(dict.fromkeys(annotations)) or ["None"]  # De-duplicated, and an empty union is just None

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        _, annotations = self._render_members(nested_struct_name, ctx, declare_structs=False)
        return " | ".join(annotations)

    @staticmethod
    def render_struct_variants(class_name: str, variants: list[tuple[str, StructSchema]], discriminator: tuple[str, list[str]] | None, ctx: SingleSymbolContext) -> list[str]:
        """Render each (name, struct) variant as a class, followed by `type <class_name> = <variant1> | <variant2> | ...`"""
        rendered = [line for name, variant in variants for line in variant.to_python_code(name, ctx) + [""]]
        # Ends with a blank line like classes do, so nested variant unions get two blank lines after them too
        return rendered + [UnionSchema._render_union_alias(class_name, [name for name, _ in variants], discriminator, ctx), ""]

    @staticmethod
    def _render_union_alias(class_name: str, annotations: list[str], discriminator: tuple[str, list[str]] | None, ctx: SingleSymbolContext) -> str:
        """`type <class_name> = A | B`, or when there's a discriminator (a field, and each member's value of it),
        `Annotated[Annotated[A, Tag(...)] | ..., Discriminator(...)]`. The tags are given, rather than pydantic finding
        them in the models, as base.py has models use each other's validators, so pydantic can't see inside them."""
        if discriminator is None:
            return f"type {class_name}{ctx.type_params_suffix()} = {' | '.join(annotations)}"

        field_name, tags = discriminator
        ctx.require_annotated()
        ctx.required_imports |= {
            Import("pydantic", "Discriminator"),
            Import("pydantic", "Tag"),
            Import(f"{GENERATED_SYMBOLS_DIRECTORY.name}.base", "tag_of"),
        }
        tagged_annotations = "\n    | ".join(f"Annotated[{annotation}, Tag({tag!r})]" for annotation, tag in zip(annotations, tags, strict=True))
        return (
            f"type {class_name}{ctx.type_params_suffix()} = Annotated[\n"
            f"    {tagged_annotations},\n"
            f"    Discriminator(tag_of({field_name!r})),\n"
            "]"
        )

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        if len(self.members) == 1:  # Some objects are (since, A) | (until, B) - collapse into just A
            return self.members[0].to_python_code(class_name, ctx)

        # Materialize struct members as concrete sibling symbols so the union alias can reference them.
        declarations, annotations = self._render_members(f"{class_name}Struct", ctx, declare_structs=True)
        return declarations + [self._render_union_alias(class_name, annotations, None, ctx)]


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

    @staticmethod
    def clean_key(key: str) -> str:
        key = re.sub(r"\W", "_", key.removeprefix("minecraft:"))  # e.g. the data component minecraft:axolotl/variant (aliased back to it)
        return key if key not in {"from", "with"} else f"{key}_"

    @property
    def key_schema(self) -> BaseSchema:
        """What the keys of a pair with a schema for a key (so any key of it, e.g. `[string]: int`) have to be."""
        assert not isinstance(self.key, str), "Pairs with a name are fields, see to_field_line"
        return self.key

    def any_key_annotations(self, ctx: SingleSymbolContext, value_struct_name: str) -> tuple[str, str]:
        """For a pair with a schema for a key: its keys' annotation and its values', e.g. ("str", "int")."""
        return self.key_schema.to_annotation(ctx), self.type.to_annotation(ctx, value_struct_name)

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
        assert isinstance(self.key, str), "Pairs with a schema for a key are extra keys, see StructSchema._render_model"
        name = PairSchema.clean_key(self.key)
        annotation = self.type.to_annotation(ctx, PairSchema.nested_struct_name(name))
        if annotation == "None":
            # This is a weird case where the union is empty, only for CustomName and CustomNameVisible, it's weird.
            return None

        default: str | None = self.formatted_default_value
        # === A field named after a type in this file (e.g. `BlockState: BlockState`) would shadow that type, so rename it.
        if name in ctx.allocated_name_by_identity.values():
            name += "_"
        if isinstance(self.key, str) and name != self.key:  # Renamed (e.g. `from_`), so alias it back to the real JSON key
            # Not alias=, as type checkers then want the JSON key as the keyword (e.g. minecraft:custom_name), not the field's name
            ctx.required_imports.add(Import("pydantic", "Field"))
            default = f"Field({'' if default is None else f'default={default}, '}validation_alias={self.key!r}, serialization_alias={self.key!r})"
        # ===
        annotation_string = annotation if not self.optional else annotation + ' | None'
        default_string = '' if default is None else f' = {default}'
        return f"    {name}: {annotation_string}{default_string}{description_comment(self.description)}"


class SpreadFieldSchema(BaseSchema):
    """An inliner, for spread (inheritance).
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

    def reference(self) -> ReferenceSchema | None:
        """Returns a reference, or a concrete schema's reference, or None"""
        if isinstance(self.type, ReferenceSchema):
            return self.type
        if isinstance(self.type, ConcreteSchema) and isinstance(self.type.child, ReferenceSchema):
            return self.type.child
        # A concrete dispatcher never references one schema (it's a list of them), so we return None for those too.
        # e.g. parallel_indices=[DynamicIndexSchema(accessor=['type'])] registry='minecraft:int_provider'
        return None


class TemplateTypeParam(BaseModel):
    """Represents a template type parameter path (e.g. ::java::world::item::T)."""
    path: str


class TemplateSchema(BaseSchema):
    """
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
            struct_member = next((member for member in self.child.members if isinstance(member, StructSchema)), self.child)  # Older versions' have none
            return struct_member.to_python_code(class_name, ctx)
        return self.child.to_python_code(class_name, ctx)


class StructSchema(BaseSchema):
    kind: Literal["struct"] = Field(repr=False)
    fields: list[Annotated[PairSchema | SpreadFieldSchema, Field(discriminator="kind")]]

    @model_validator(mode="after")
    def prune_fields_on_version(self) -> Self:
        # All the PairSchema and SpreadFieldSchema fields have attributes, so we can filter them based on the current version.
        self.fields = [field for field in self.fields if is_valid_with_attributes(field.attributes)]
        return self  # Has to return self

    @property
    def contains_inline_struct(self) -> bool:
        return True

    def flattened_pairs(self) -> list[PairSchema]:
        """The pairs that become its class's fields: its own, plus those of any inline structs it spreads (spreads of
        classes get inherited instead, see inherited_base_names)"""
        pairs: list[PairSchema] = []
        for field in self.fields:
            if isinstance(field, PairSchema):
                pairs.append(field)
            elif isinstance(field.type, StructSchema):
                pairs.extend(field.type.flattened_pairs())
        return pairs

    def inherited_base_names(self, ctx: SingleSymbolContext) -> list[str]:
        """The classes its class inherits from (the ones it spreads), e.g. class MyClass(`<x>`, `<y>`)"""
        strict_ctx = ctx.copy()
        strict_ctx.allow_template_shortcuts = False  # Don't allow inherited | float, for example.
        strict_ctx.require_runtime_imports = True
        base_names: set[str] = set()
        for spread in (field for field in self.fields if isinstance(field, SpreadFieldSchema)):
            # Keep concrete spread type arguments in inheritance, e.g. UniformIntProvider[T].
            reference = spread.reference()
            if reference is not None and reference.path not in ctx.local_type_params:
                base_names.add(spread.type.to_annotation(strict_ctx))
            if isinstance(spread.type, StructSchema):
                base_names.update(spread.type.inherited_base_names(ctx))
        return sorted(base_names)

    def to_annotation(self, ctx: SingleSymbolContext, nested_struct_name: str | None = None) -> str:
        """Structs used inline (e.g. as a field's type) get generated as their own class, named `nested_struct_name`."""
        assert nested_struct_name is not None, "Inline structs need a name to be generated with"
        if (with_fields := self._with_registry_map_fields(ctx)) is not self:
            return with_fields.to_annotation(ctx, nested_struct_name)
        mapping_alias = self._mapping_alias_annotation(ctx, f"{nested_struct_name}ValueStruct")
        if mapping_alias is not None:  # Mappings are just dict[<x>, <x>], so inline them rather than making a type alias.
            return mapping_alias
        class_name = ctx.allocate_name(nested_struct_name, self.model_dump_json(by_alias=True), avoid_symbol_names=True)
        helper_ctx = ctx.copy()
        helper_ctx.resource_dir = None  # Helper structs (e.g. a field's struct) aren't the resource itself
        ctx.add_dataclass(self.to_python_code(class_name, helper_ctx))
        return f"{class_name}{ctx.type_params_suffix()}"

    def _with_registry_map_fields(self, ctx: SingleSymbolContext) -> StructSchema:
        """Maps from a registry's ids to what each one's value is, e.g. data components: `[#[id] string]: minecraft:data_component[[%key]]`,
        get a field for each, e.g. `potion_contents: PotionContents | None` (aliased to minecraft:potion_contents), so each
        value is its own type. Its other any-key pairs, e.g. for "!minecraft:potion_contents" (which removes it), stay, as
        the class's extra keys. Only minecraft: registries, as the mcdoc: ones (e.g. custom data) have any keys, so stay a dict."""
        registry_map = next((
            field.type for field in self.fields
            if isinstance(field, PairSchema) and not isinstance(field.key, str) and isinstance(field.type, DispatcherSchema)
            and field.type.selected_by_key and field.type.registry.startswith("minecraft:")
        ), None)
        if registry_map is None:
            return self
        fields = [field for field in self.fields if field.type is not registry_map]  # Without the map
        fields += [
            PairSchema(kind="pair", key=f"minecraft:{key}", type=branch.model_copy(deep=True), optional=True)  # type: ignore[arg-type]
            for key, branch in ctx.schema_graph.dispatchers[registry_map.registry].items() if not key.startswith("%")
        ]
        return self.model_copy(update={"fields": fields})

    def any_key_pairs(self) -> list[PairSchema]:
        """Its pairs with a schema for a key (so any key of it, e.g. `[string]: int`), rather than a name."""
        return [field for field in self.fields if isinstance(field, PairSchema) and not isinstance(field.key, str)]

    @property
    def is_mapping(self) -> bool:
        """Whether it's really a dict, e.g. Lang is `[string]: string`, so dict[str, str]: all it has is any-key pairs. With
        named pairs or a spread too, it's a class, whose other keys are the any-key pairs (see _render_model)."""
        return bool(self.fields) and len(self.any_key_pairs()) == len(self.fields)

    @staticmethod
    def _any_keys_annotation(pairs: list[PairSchema], ctx: SingleSymbolContext, value_struct_name: str) -> str:
        """dict[<key>, <value>] for any-key pairs, e.g. dict[str, int] for `[string]: int`. With more than one, its keys
        can be any of theirs, and so can its values."""
        annotations = [pair.any_key_annotations(ctx, value_struct_name) for pair in pairs]
        keys = " | ".join(dict.fromkeys(key for key, _ in annotations))
        values = " | ".join(dict.fromkeys(value for _, value in annotations))
        return f"dict[{keys}, {values}]"

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
            return UnionSchema.render_struct_variants(class_name, named_variants, None, ctx)
        return None

    def _mapping_alias_annotation(self, ctx: SingleSymbolContext, value_struct_name: str) -> str | None:
        """Returns the mapping alias dict (i.e. dict[<x>, <x>]) for a struct, or None if it's not that kind of struct."""
        return self._any_keys_annotation(self.any_key_pairs(), ctx, value_struct_name) if self.is_mapping else None

    def _render_model(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        pairs = self.flattened_pairs()
        # Discover unresolved symbolic refs before rendering the Generic[...] base.
        for pair in pairs:
            if isinstance(pair.type, ReferenceSchema) and pair.type.path not in ROOT_SYMBOLS_KEYS["mcdoc"]:
                ctx.local_type_params.add(pair.type.path)
        # Structs' inherited children, e.g. class MyClass(PredicateOffset), or GeneratedModel if there's none.
        base_names = self.inherited_base_names(ctx)
        if not base_names:
            ctx.required_imports.add(Import(f"{GENERATED_SYMBOLS_DIRECTORY.name}.base", "GeneratedModel"))
            base_names = ["GeneratedModel"]
        if type_params := ctx.type_params_suffix():
            ctx.required_imports.add(Import("typing", "Generic"))
            base_names.append(f"Generic{type_params}")

        lines = [f"class {class_name}({', '.join(base_names)}):"]
        if ctx.resource_dir is not None:  # A root resource (or one of its variants), e.g. a recipe, knows its pack directory
            ctx.required_imports.add(Import("typing", "ClassVar"))
            lines.append(f"    __resource_dir__: ClassVar[str] = {ctx.resource_dir!r}\n")
        if not pairs and ctx.resource_dir is None:  # A class needs something in it
            lines.append("    pass")
        lines.extend(line for pair in pairs if isinstance(pair.key, str) and (line := pair.to_field_line(ctx)) is not None)
        if any_keys := [pair for pair in pairs if not isinstance(pair.key, str)]:
            # Any other keys it has, e.g. ItemBase's custom NBT, which pydantic checks against this (init=False is for type
            # checkers, which would otherwise think it's a field you have to give)
            ctx.required_imports.add(Import("pydantic", "Field"))
            extra = self._any_keys_annotation(any_keys, ctx, f"{class_name}ValueStruct")
            # Type checkers only allow string keys (BaseModel has dict[str, Any]), but pydantic checks others too, e.g. axes
            string_keys = all(isinstance(ctx.schema_graph.resolve(pair.key_schema), StringSchema) for pair in any_keys)
            ignore = "" if string_keys else "  # type: ignore[assignment]"
            description = next((pair.description for pair in any_keys if pair.description), "")
            lines.append(f"    __pydantic_extra__: {extra} = Field(init=False){ignore}{description_comment(description)}")
        return lines + [""]

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        """A struct renders as the first of these that applies:
        1. A spread of a non-class alias  -> one class per struct it could be, plus their union
        2. A spread of a dispatcher       -> one class per registry entry, plus their (discriminated) union, see DispatcherSpread
        3. A mapping                      -> `type <class_name> = dict[<key>, <value>]`
        4. Anything else                  -> a normal class
        """
        if (with_fields := self._with_registry_map_fields(ctx)) is not self:
            return with_fields.to_python_code(class_name, ctx)
        if (alias_spread := self._render_alias_spread(class_name, ctx)) is not None:
            return alias_spread
        if (dispatcher_spread := DispatcherSpread.of(self, ctx.schema_graph)) is not None:
            return dispatcher_spread.to_python_code(class_name, ctx)
        if (mapping_alias := self._mapping_alias_annotation(ctx, f"{class_name}ValueStruct")) is not None:
            return [f"type {class_name}{ctx.type_params_suffix()} = {mapping_alias}\n"]
        return self._render_model(class_name, ctx)


@dataclass(frozen=True)
class DispatcherSpread:
    """A struct with a dispatcher that one of the struct's own fields (the selector, e.g. `type`) picks the branch of,
    which it either spreads, or is the type of one of its fields (`field`, e.g. ComponentFlags' value, picked by its
    predicate). Each registry entry gets its own class, with the selector narrowed to its id, and the struct is their union."""
    struct: StructSchema
    dispatcher: DispatcherSchema
    selector: str
    field: PairSchema | None = None  # The field it's the type of, or None if it's spread

    @classmethod
    def of(cls, struct: StructSchema, schema_graph: SchemaGraph) -> DispatcherSpread | None:
        """The struct's dispatcher spread, or if it has none, its field that's a dispatcher picked by another field. Not if
        there's more than one, as it's not clear which picks what. And not a field's dispatcher that only has %none and
        %unknown, e.g. an advancement's display (root or not), as then the selector's value doesn't matter, just whether it's there."""
        dispatchers = [field.type for field in struct.fields if isinstance(field, SpreadFieldSchema) and isinstance(field.type, DispatcherSchema)]
        if dispatchers:
            if len(dispatchers) != 1 or (selector := dispatchers[0].dynamic_selector_field) is None:
                return None
            return cls(struct, dispatchers[0], selector)
        names = {field.key for field in struct.fields if isinstance(field, PairSchema) and isinstance(field.key, str)}
        fields = [
            (field, field.type, selector) for field in struct.fields
            if isinstance(field, PairSchema) and isinstance(field.type, DispatcherSchema) and (selector := field.type.dynamic_selector_field) in names
        ]
        if len(fields) != 1 or all(key.startswith("%") for key in schema_graph.dispatchers.get(fields[0][1].registry, {})):
            return None
        field, dispatcher, selector = fields[0]
        return cls(struct, dispatcher, selector, field)

    def _selector_registry(self) -> str | None:
        """Which registry the selector is an id from, e.g. `type: #[id="loot_condition_type"] string`"""
        selector = next((field.type for field in self.struct.fields if isinstance(field, PairSchema) and field.key == self.selector), None)
        if isinstance(selector, UnionSchema) and len(selector.members) == 1:  # e.g. the other members are for older versions
            selector = selector.members[0]
        id_spec = selector.id_spec() if isinstance(selector, StringSchema) else None
        if id_spec is None or id_spec.registry is None:
            return None
        registry = id_spec.registry.removeprefix("minecraft:")
        return registry if registry in REGISTRIES else f"{registry}_type"  # mcmeta calls some e.g. rule_test_type

    def _variant(self, registry_key: str, branch: BaseSchema, branch_struct: StructSchema, branch_reference: ReferenceSchema | None) -> StructSchema:
        """The struct for one registry entry: copies of the struct's fields (without the spread), with the selector narrowed
        to the entry's id, e.g. the `ore_drops` branch has `formula: Literal["minecraft:ore_drops"]`, not `formula: ApplyBonusFormula`
        (but not for % keys like %unknown, which aren't real ids). Then, for a field, the branch is its type. For a spread,
        the branch's own fields, by inheriting it if it's a class, or copying its named pairs (pairs with a schema for a key
        are any key, so can't be named fields)."""
        fields = [
            field.model_copy(update={"type": branch.model_copy(deep=True)}) if field is self.field else field.model_copy(deep=True)
            for field in self.struct.fields if field is self.field or field.type is not self.dispatcher  # i.e. not the spread
        ]
        if not registry_key.startswith("%"):
            for field in fields:
                if isinstance(field, PairSchema) and field.key == self.selector:
                    field.type = LiteralSchema(kind="literal", value=StringSchema(kind="string", value=f"minecraft:{registry_key}"))

        if self.field is not None:
            return StructSchema(kind="struct", fields=fields)
        if branch_reference is not None:
            fields.append(SpreadFieldSchema(kind="spread", type=branch_reference.model_copy(deep=True)))
        else:
            fields.extend(
                field.model_copy(deep=True)
                for field in branch_struct.fields
                if not isinstance(field, PairSchema) or isinstance(field.key, str)
            )
        return StructSchema(kind="struct", fields=fields)

    def _variants(self, class_name: str, ctx: SingleSymbolContext) -> dict[str, tuple[str, StructSchema]]:
        """Every registry entry's (uniquely named) struct, by its registry key."""
        branches: dict[str, BaseSchema] = dict(ctx.schema_graph.dispatchers[self.dispatcher.registry])  # Already filtered to the current version
        if (registry := self._selector_registry()) in REGISTRIES:
            # vanilla-mcdoc only has the entries with fields of their own, so the rest of the registry (e.g. the loot condition
            # minecraft:survives_explosion) get what mcdoc gives a missing entry: %unknown's fields (or type), or none (or
            # anything). Then each has its own tag (so the union can be discriminated), and %unknown isn't needed.
            fallback = branches.pop(r"%unknown", StructSchema(kind="struct", fields=[]) if self.field is None else AnySchema(kind="any"))
            branches |= {key: fallback for key in REGISTRIES[registry] if key not in branches}
        variants: dict[str, tuple[str, StructSchema]] = {}
        for key, branch in branches.items():
            resolved = ctx.schema_graph.resolve(branch)
            if isinstance(resolved, UnionSchema) and not resolved.members:  # mcdoc's "nothing's allowed", e.g. a %none of
                continue  # `union {}` means the selector can't be left out, so there's no variant for it (it'd allow anything)
            branch_struct = resolved if isinstance(resolved, StructSchema) else StructSchema(kind="struct", fields=[])
            variant_name = ctx.allocate_name(f"{class_name}{DispatcherSchema.branch_name_suffix(key)}", branch_struct.model_dump_json(by_alias=True), avoid_symbol_names=True)
            # Branches that are classes get inherited, rather than having their fields copied in.
            branch_reference = branch if isinstance(branch, ReferenceSchema) and ctx.schema_graph.is_runtime_class(branch) else None
            variants[key] = (variant_name, self._variant(key, branch, branch_struct, branch_reference))
        return variants

    def to_python_code(self, class_name: str, ctx: SingleSymbolContext) -> list[str]:
        variants = self._variants(class_name, ctx)
        # Each variant's tag is its registry key, even if it's a union itself (e.g. apply_bonus splits again by formula).
        # Not when there's a %none (for when there's no selector) or %unknown (any other value), which have no tag.
        discriminator = None if any(key.startswith(r"%") for key in variants) else (self.selector, [f"minecraft:{key}" for key in variants])
        return UnionSchema.render_struct_variants(class_name, list(variants.values()), discriminator, ctx)


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

    @property
    def dynamic_selector_field(self) -> str | None:
        """Return the sibling field that selects the branch (e.g. `type`), or None if it's selected some other way,
        e.g. via the parent (`[%parent, "BlockState"]`) or a nested field (`["output_state", "id"]`)."""
        index = self.parallel_indices[0]
        if not isinstance(index, DynamicIndexSchema):
            return None
        return index.accessor[0] if len(index.accessor) == 1 and isinstance(index.accessor[0], str) else None

    @property
    def selected_by_key(self) -> bool:
        """Whether it's selected by the key it's the value of, e.g. data components: `[#[id] string]: minecraft:data_component[[%key]]`"""
        index = self.parallel_indices[0]
        return isinstance(index, DynamicIndexSchema) and index.accessor == [DynamicIndexAccessorItem(keyword="key")]

    @property
    def static_key(self) -> str | None:
        """The one entry it always picks, e.g. "trial_spawner" for `minecraft:block_entity[trial_spawner]`, or None if it can be any"""
        index = self.parallel_indices[0]
        if isinstance(index, DynamicIndexSchema) or index.value == "%fallback":
            return None
        return index.value.removeprefix("minecraft:")

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
        registry = ctx.schema_graph.dispatchers.get(self.registry, {})  # Not in symbols.json at all if Spyglass fills it from the game, e.g. mcdoc:fluid_state_keys
        candidates = list(registry.items()) if self.static_key is None else [(self.static_key, registry[self.static_key])]

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
            annotations.append(branch.to_annotation(ctx, branch_name))

        if not annotations:  # Its registry has nothing in it (yet, or in this version), which like a missing entry, isn't checked
            ctx.required_imports.add(Import("typing", "Any"))
            return "Any"
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
