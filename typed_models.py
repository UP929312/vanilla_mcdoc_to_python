from dataclasses import dataclass, field
from typing import Annotated, Literal, Self

from pydantic import BaseModel, Field, RootModel, model_validator

from utils import ROOT_SYMBOLS_KEYS, symbol_path_to_import_string_and_name, symbol_path_to_object_name, is_valid_with_attributes, iter_child_schemas


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


@dataclass(frozen=True)
class Import:
    relative_module: str
    identifier: str
    type_checking_only: bool
    is_builtin: bool


@dataclass
class RenderContext:
    required_imports: set[Import] = field(default_factory=set)
    local_type_params: set[str] = field(default_factory=set)
    additional_dataclasses: list[str] = field(default_factory=list)
    current_symbol_path: str | None = None
    indent: int = 0
    allow_type_args_kind_shortcut: bool = True

    def require_annotated(self) -> None:
        self.required_imports.add(Import("typing", "Annotated", type_checking_only=False, is_builtin=True))

    def add_dataclass(self, lines: list[str]) -> None:
        self.additional_dataclasses.extend(lines + [""])

    def add_import_by_symbol_path(self, path: str) -> str:
        """For child references, take the path and add it as an import"""
        module, name = symbol_path_to_import_string_and_name(path)
        if path == self.current_symbol_path:
            return name
        if path in self.local_type_params:
            return name
        if path not in ROOT_SYMBOLS_KEYS["mcdoc"]:
            # This is a weird edgecase for tag::E
            # I might figure out a better solution later, but for now, it's fine.
            self.local_type_params.add(path)
            return name
        self.required_imports.add(Import(module, name, type_checking_only=True, is_builtin=False))
        return name

    def nested(self, extra_indent: int = 0, allow_type_args_kind_shortcut: bool = True) -> RenderContext:
        """Return a child context with increased indentation while sharing imports."""
        return RenderContext(
            required_imports=self.required_imports,
            local_type_params=self.local_type_params,
            additional_dataclasses=self.additional_dataclasses,
            current_symbol_path=self.current_symbol_path,
            indent=self.indent + extra_indent,
            allow_type_args_kind_shortcut=allow_type_args_kind_shortcut,
        )

    def imports_to_python_code(self) -> list[str]:
        runtime_import_keys = {
            (import_statement.relative_module, import_statement.identifier)
            for import_statement in self.required_imports
            if not import_statement.type_checking_only
        }
        symbol_imports_filtered = {
            import_statement
            for import_statement in self.required_imports
            # If an import is required at runtime, don't keep a duplicate TYPE_CHECKING-only entry.
            if not (import_statement.type_checking_only and (import_statement.relative_module, import_statement.identifier) in runtime_import_keys)
        }

        def build_lines(entries: set[Import]) -> list[str]:
            grouped: dict[str, list[str]] = {
                import_statement.relative_module: [x.identifier for x in entries if x.relative_module == import_statement.relative_module]
                for import_statement in entries
            }
            return [
                f"from {relative_module} import {', '.join(sorted(set(identifiers), key=lambda x: (not x.isupper(), x)))}"
                for relative_module, identifiers in sorted(grouped.items())
            ]

        built_ins = {t for t in symbol_imports_filtered if t.is_builtin and not t.type_checking_only}
        regular = {t for t in symbol_imports_filtered if not t.is_builtin and not t.type_checking_only}
        type_checking = {t for t in symbol_imports_filtered if t.type_checking_only}

        if type_checking:
            built_ins.add(Import("typing", "TYPE_CHECKING", False, True))

        built_in_lines = build_lines(built_ins)
        regular_lines = build_lines(regular)
        lines: list[str] = built_in_lines
        if built_in_lines and regular_lines:
            lines.append("")
        lines.extend(regular_lines)

        if type_checking:
            lines.append("\nif TYPE_CHECKING:")
            lines.extend(f"    {line}" for line in build_lines(type_checking))

        return lines + ["\n"]


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================
# HELPERS AND PARTS


class BaseSchema(BaseModel):
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        """Generate the actual Python, for most things, this is just the alias to the annotation"""
        return [f"type {class_name} = {self.to_annotation(ctx)}"]

    def to_annotation(self, ctx: RenderContext) -> str:
        raise NotImplementedError("This should never get called directly.")

    def remove_version_data(self) -> BaseSchema:
        self.attributes = [x for x in self.attributes if not x.is_undesirable_attribute]
        for field_name in type(self).model_fields:
            for child in iter_child_schemas(getattr(self, field_name)):
                if child is not self:
                    child.remove_version_data()
        return self


class Attribute(BaseModel):
    """Represents a single attribute with a name and a structured value."""
    name: str
    value: Annotated[LiteralSchema | TreeSchema | DispatcherSchema | ReferenceSchema, Field(discriminator="kind")] | None = None

    @property
    def is_version_attribute(self) -> bool:
        return self.name in {"since", "until"}

    @property
    def is_undesirable_attribute(self) -> bool:
        return self.is_version_attribute or self.name == "deprecated"


class ValueRange(BaseModel):
    """Represents a numeric range, used in `int`, `float`, and array lengths."""
    kind: Literal[0, 2] = Field(default = 0, repr=False)
    min: float | int  # Min is *always* set
    max: float | int | None = None

    def to_annotation(self, ctx: RenderContext, value_range_type: Literal["int", "float"], attributes: list[Attribute]) -> str:
        if self.min is not None and self.max is not None:
            parts = ["Range", f"`{self.min or '0'}`-`{self.max or '0'}`", "both inclusive"]
        else:
            parts = ["Range", f"Min `{self.min or '0'}` and above", "inclusive"]
        if self.extract_divisible_by_value(attributes):
            parts.append(f"divisible by {self.extract_divisible_by_value(attributes)}")
        ctx.require_annotated()
        return f"Annotated[{value_range_type}, '{' | '.join(parts)}']"

    def extract_divisible_by_value(self, attributes: list[Attribute]) -> str | None:
        divisible_by_attr_value: str | None = next(
            (attr.value.value.value for attr in attributes or [] if attr.name == "divisible_by"),  # type: ignore
            None
        )
        return divisible_by_attr_value


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

    def description_text(self) -> str:
        return self.description.replace("\\\n", "\n").replace('\n', ' ').strip()


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


class LiteralSchema(BaseSchema):
    """Represents a literal value, often found inside an Attribute's value.
    Also normally used to just set until version
    """
    kind: Literal["literal"] = Field(repr=False)
    value: Annotated[
        StringSchema | IntSchema | FloatSchema | BooleanSchema | ShortSchema | LongSchema | ByteSchema | StructSchema,
        Field(discriminator="kind"),
    ]

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value.to_annotation(ctx)


# ==================================================================================================================================
# Primitive Schemas (string, int, float, boolean, etc.)


class IntSchema(BaseSchema):
    kind: Literal["int"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    value: Literal[-1, 0, 1, 3, 16, 20, 90, 180, 270, 32500] | None = None  # This is for speed, but should probably go back to int.

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value_range.to_annotation(ctx, "int", self.attributes) if self.value_range else "int"


class StringSchema(BaseSchema):
    kind: Literal["string"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value: str | None = None  # For literal strings

    # Value options (only these ones)
    # [
    #     'atlas', 'attacker', 'block', 'block_entity', 'ceiling', 'container', 'default', 'entity', 'entity_position',
    #     'floor', 'front', 'in_bounding_box', 'keybind', 'nbt', 'object', 'override', 'player', 'score', 'selector',
    #     'side', 'storage', 'text', 'tool', 'translatable', 'victim'
    # ]

    # Returning soon:
    # def _escaped_id_attribute(self) -> str | None:
    #     id_attribute = next((attribute for attribute in self.attributes if attribute.name == "id"), None)
    #     if id_attribute is None or id_attribute.value is None:
    #         return None

    #     if isinstance(id_attribute.value, LiteralSchema) and isinstance(id_attribute.value.value, StringSchema):
    #         assert id_attribute.value.value.value is not None
    #         raw_literal = id_attribute.value.value.value
    #         escaped = raw_literal.replace("\\", "\\\\").replace('"', '\\"')
    #         return escaped
    #     return None

    def to_annotation(self, ctx: RenderContext) -> str:
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
            # If we get to here, there is never an id attribute, so we can just do normal str stuff.
            return f"Annotated[str, '{self.length_range.to_annotation_suffix()}']" if self.length_range else "str"

        # Else, it's a literal/string of type, do it like that:
        # === Temporarily disabled, wasn't happy with this, it worked, but was ugly ===
        # id_attribute = self._escaped_id_attribute()
        # if id_attribute:
        #     ctx.require_annotated()
        #     return f"Annotated[str, 'string type=\"{id_attribute}\"']"

        # Else, normal string:
        return "str"


class FloatSchema(BaseSchema):
    kind: Literal["float", "double"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    # value: float | None = None  # For literal floats (not used in the symbols yet)

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value_range.to_annotation(ctx, "float", self.attributes) if self.value_range else "float"


class BooleanSchema(BaseSchema):
    kind: Literal["boolean"] = Field(repr=False)
    # value: bool | None = None  # For literal booleans (not used in the symbols yet)

    def to_annotation(self, ctx: RenderContext) -> str:
        return "bool"


class ShortSchema(BaseSchema):
    kind: Literal["short"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    # value: int | None = None  # For literal shorts (not used in the symbols yet)

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value_range.to_annotation(ctx, "int", self.attributes) if self.value_range else "int"


class LongSchema(BaseSchema):
    kind: Literal["long"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    # value: int | None = None  # For literal longs (not used in the symbols yet)

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value_range.to_annotation(ctx, "int", self.attributes) if self.value_range else "int"


class ByteSchema(BaseSchema):
    kind: Literal["byte"] = Field(repr=False)
    value_range: ValueRange | None = Field(default=None, alias="valueRange")
    # value: bool | int | None = None  # For literal bytes (not used in the symbols yet)
    # Also has "attributes": [{"name": "canonical"}] + Version stuff

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.value_range.to_annotation(ctx, "int", self.attributes) if self.value_range else "int"


class AnySchema(BaseSchema):
    kind: Literal["any"] = Field(repr=False)

    def to_annotation(self, ctx: RenderContext) -> str:
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
        return isinstance(self.item, StructSchema) or isinstance(self.item, ListSchema) and self.item.contains_inline_struct()

    def _calculated_item_annotation(self, ctx: RenderContext, nested_struct_name: str | None = None) -> str:
        """Either points directly to the normal annotation (e.g. list[>>>`int`<<<])
        Or, for locally generated structs, points to them (and creates their code)"""
        if isinstance(self.item, StructSchema) and nested_struct_name is not None:
            return self.item.to_materialized_annotation(nested_struct_name, ctx)
        elif isinstance(self.item, ListSchema):  # TODO: Figure out when we have lists of lists?
            return self.item.to_annotation(ctx, nested_struct_name)
        return self.item.to_annotation(ctx)
        
    def to_annotation(self, ctx: RenderContext, nested_struct_name: str | None = None) -> str:
        item_annotation = self._calculated_item_annotation(ctx, nested_struct_name)
        if self.length_range is None:
            return f"list[{item_annotation}]"
        if self.length_range.min is not None and self.length_range.min == self.length_range.max:
            return f"tuple[{', '.join(item_annotation for _ in range(self.length_range.min))}]"
        ctx.require_annotated()
        return f"Annotated[list[{item_annotation}], '{self.length_range.to_annotation_suffix()}']"

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        type_param_names = sorted(symbol_path_to_object_name(path) for path in ctx.local_type_params)
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

    def to_annotation(self, ctx: RenderContext) -> str:
        return f"tuple[{', '.join(item.to_annotation(ctx) for item in self.items)}]"


class IntArraySchema(BaseSchema):
    kind: Literal["int_array"] = Field(repr=False)
    length_range: LengthRange | None = Field(default=None, alias="lengthRange")
    value_range: ValueRange | None = Field(default=None, alias="valueRange")

    def to_annotation(self, ctx: RenderContext) -> str:
        if self.length_range is None:
            # Only ever used by "::java::world::item::firework::Explosion"
            return "list[int]"
        if self.length_range.min != self.length_range.max:  # There's one item, no min, up to 9 max (world/block/crafter/Crafter)
            # ::java::world::block::crafter::Crafter
            int_annotation = IntSchema(kind="int", valueRange=self.value_range).to_annotation(ctx)
            ctx.require_annotated()
            return f"Annotated[list[{int_annotation}], '{self.length_range.to_annotation_suffix()}']"
        if self.length_range.min is not None:
            return f"tuple[{', '.join("int" for _ in range(self.length_range.min))}]"
        raise TypeError("Invalid IntArray input", self)


class EnumSchema(BaseSchema):
    kind: Literal["enum"] = Field(repr=False)
    enum_kind: Literal["byte", "int", "string"] = Field(alias="enumKind")
    values: list[EnumValue]

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        ctx.required_imports.add(Import("enum", "Enum", False, True))
        return [f"class {class_name}(Enum):"] + [
            f"    {value.identifier.upper()} = \"{value.value}\"" + (f"  # {value.description_text()}" if value.description else "")
            for value in self.values
        ]



# ==================================================================================================================================
# Meta types


type ConcreteSchemaTypeArgTypes = (
    AnySchema | BooleanSchema | ByteSchema | ConcreteSchema | DispatcherSchema | FloatSchema | IndexedSchema
    | IntArraySchema | IntSchema | ListSchema | LiteralSchema | LongSchema | ReferenceSchema | ShortSchema
    | StringSchema | TupleSchema | UnionSchema
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

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        # We ommit the "type" so we can bind them, and then other things can inherit this binding.
        return [f"{class_name} = {self.to_annotation(ctx)}"]

    def to_annotation(self, ctx: RenderContext) -> str:
        concrete_annotation = f"{self.child.to_annotation(ctx)}[{', '.join([type_arg.to_annotation(ctx) for type_arg in self.type_args])}]"
        if not self.type_args or not ctx.allow_type_args_kind_shortcut:
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

    def to_annotation(self, ctx: RenderContext) -> str:
        return self.child.to_annotation(ctx)


class ReferenceSchema(BaseSchema):
    """References another model/schema by path."""
    kind: Literal["reference"] = Field(repr=False)
    path: str
    attributes: list[Attribute] = Field(default_factory=list, repr=False)

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        path, name = symbol_path_to_import_string_and_name(self.path)

        # For regular Minecraft/Java mcdocs, we go this route
        if class_name == name:  # This is always True for `mcdoc`
            ctx.required_imports.add(Import(path, f"{name} as {name}_alias", type_checking_only=False, is_builtin=False))
            return [f"type {class_name} = {name}_alias"]

        # Normally true for mcdoc/dispatcher
        ctx.required_imports.add(Import(path, name, type_checking_only=False, is_builtin=False))
        return [f"type {class_name} = {name}"]

    def to_annotation(self, ctx: RenderContext) -> str:
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

    def to_annotation(self, ctx: RenderContext) -> str:
        if not self.members:  # For things like Player, who has weird fields...
            return "None"
        return " | ".join(dict.fromkeys(member.to_annotation(ctx) for member in self.members))

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        """   # TEMP
        type_param_names = sorted(symbol_path_to_object_name(path) for path in ctx.local_type_params)
        type_params = f"[{', '.join(type_param_names)}]" if type_param_names else ""

        # Preserve old-style template wrapper output for shapes like:
        # template child = T | struct{...pairs...}
        # These are better rendered as a single generic dataclass than as Struct1 + alias.
        # Keep union aliases for richer provider wrappers that include spread fields.
        if len(self.members) == 2 and type_param_names:
            struct_members = [member for member in self.members if isinstance(member, StructSchema)]
            reference_members = [member for member in self.members if isinstance(member, ReferenceSchema)]
            if len(struct_members) == 1 and len(reference_members) == 1:
                struct_member = struct_members[0]
                reference_member = reference_members[0]
                if reference_member.path in ctx.local_type_params and all(isinstance(field, PairSchema) for field in struct_member.fields):
                    return struct_member.to_python_code(class_name, ctx)
        """
        type_params = ""

        if len(self.members) == 1:
            member = self.members[0]
            if isinstance(member, StructSchema):
                return member.to_python_code(class_name, ctx)
            if isinstance(member, ListSchema) and member.contains_inline_struct():
                return [f"type {class_name} = {member.to_annotation(ctx, PairSchema.nested_struct_name(class_name))}"]
            return [f"type {class_name} = {member.to_annotation(ctx)}"]

        # Materialize struct members as concrete sibling symbols so the union alias can reference them.
        # This is normally when a type is of kind: Struct | Struct, we can't use either, so we make both,
        # then kind of glue them together here, using our already existing code.
        rendered_struct_members: list[str] = []
        union_member_annotations: list[str] = []
        materialized_index = 0

        materialized_member_count = len([
            member for member in self.members
            if isinstance(member, StructSchema) or isinstance(member, ListSchema) and member.contains_inline_struct()
        ])
        for member in self.members:
            if isinstance(member, StructSchema):
                materialized_index += 1
                member_name = f"{class_name}Struct{'' if materialized_member_count == 1 else materialized_index}"
                rendered_struct_members.extend(member.to_python_code(member_name, ctx) + [""])
                union_member_annotations.append(f"{member_name}{type_params}")
            elif isinstance(member, ListSchema) and member.contains_inline_struct():
                materialized_index += 1
                member_name = f"{class_name}Struct{'' if materialized_member_count == 1 else materialized_index}"
                union_member_annotations.append(member.to_annotation(ctx, member_name))
            else:
                union_member_annotations.append(member.to_annotation(ctx))

        deduped_annotations = list(dict.fromkeys(union_member_annotations)) or ["None"]
        alias_line = f"type {class_name}{type_params} = {' | '.join(deduped_annotations)}"

        if not rendered_struct_members:
            return [alias_line]

        return rendered_struct_members + [alias_line]


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

    def description_text(self) -> str:
        return self.description.replace("\\\n", "\n").replace('\n', ' ').strip()

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

    def _unravel_reference_path(self) -> ReferenceSchema | None:
        """Returns a reference, or a concrete schema's reference, or None"""
        if isinstance(self.type, ReferenceSchema):
            return self.type
        if isinstance(self.type, ConcreteSchema):
            if isinstance(self.type.child, ReferenceSchema):
                return self.type.child
            if isinstance(self.type.child, DispatcherSchema):  # TODO: Eventually inherit from these
                return None
            raise TypeError("Invalid SpreadField + ConcreteSchema")
        return None

    @classmethod
    def collect_runtime_symbol_imports(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema], ctx: RenderContext) -> None:
        """Adds all the necessary classes to the required imports list"""
        for spread_field_schema in [fld for fld in fields if isinstance(fld, SpreadFieldSchema)]:
            reference = spread_field_schema._unravel_reference_path()
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
    def collect_inherited_base_names(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema], ctx: RenderContext) -> list[str]:
        """Return a list of strings representing inherited classes, e.g. class MyClass(`<x>`, `<y>`) """
        base_names: list[str] = []
        for spread_field_schema in [fld for fld in fields if isinstance(fld, SpreadFieldSchema)]:
            # Keep concrete spread type arguments in inheritance, e.g. UniformIntProvider[T].
            strict_ctx = ctx.nested(allow_type_args_kind_shortcut=False)  # Don't allow inherited | float, for example.
            reference = spread_field_schema._unravel_reference_path()
            # base_name = None
            # if reference and reference.path not in ctx.local_type_params:
            #     base_name = spread_field_schema.type.to_annotation(strict_ctx)
            # elif isinstance(spread_field_schema.type, ConcreteSchema) and isinstance(spread_field_schema.type.child, DispatcherSchema):
            #     base_name = spread_field_schema.type.to_annotation(strict_ctx)
            base_name = (
                spread_field_schema.type.to_annotation(strict_ctx)
                if reference and reference.path not in ctx.local_type_params
                else None
            )
            if base_name is not None and base_name not in base_names:
                base_names.append(base_name)

            if isinstance(spread_field_schema.type, StructSchema):
                base_names.extend(SpreadFieldSchema.collect_inherited_base_names(spread_field_schema.type.fields, ctx))
        return base_names

    @classmethod
    def collect_inlined_pair_fields(cls, fields: list[PairSchema | SpreadFieldSchema | UnionSchema]) -> list[PairSchema]:
        """For all the fields, return only those that are `PairSchema`. \n
        If it's a struct, return **ITS** `PairSchema`s"""
        inlined_fields: list[PairSchema] = []
        for pair_field in fields:
            if isinstance(pair_field, PairSchema):
                inlined_fields.append(pair_field)
            if isinstance(pair_field, cls) and isinstance(pair_field.type, StructSchema):
                inlined_fields.extend(SpreadFieldSchema.collect_inlined_pair_fields(pair_field.type.fields))
        return inlined_fields


class TemplateTypeParam(BaseModel):
    """Represents a template type parameter path (e.g. ::java::world::item::T)."""
    path: str

    # def to_python_code(self) -> str:
    #     """Converts `::java::world::item::T` -> `T` """
    #     return self.path.split("::")[-1]


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

    def _add_local_type_params_to_context(self, ctx: RenderContext) -> None:
        ctx.local_type_params.update(type_param.path for type_param in self.type_params)

    def to_annotation(self, ctx: RenderContext) -> str:
        self._add_local_type_params_to_context(ctx)
        return self.child.to_annotation(ctx)

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        self._add_local_type_params_to_context(ctx)
        if isinstance(self.child, UnionSchema):
            struct_members = [member for member in self.child.members if isinstance(member, StructSchema)]
            return struct_members[0].to_python_code(class_name, ctx)  # Always have at least one struct
        return self.child.to_python_code(class_name, ctx)


class StructSchema(BaseSchema):
    kind: Literal["struct"]
    fields: list[Annotated[PairSchema | SpreadFieldSchema | UnionSchema, Field(discriminator="kind")]]

    @model_validator(mode="after")
    def prune_fields_on_version(self) -> Self:
        # All the PairSchema and SpreadFieldSchema fields have attributes, so we can filter them based on the current version.
        filtered_fields: list[PairSchema | SpreadFieldSchema | UnionSchema] = [
            field for field in self.fields
            if isinstance(field, (PairSchema, SpreadFieldSchema)) and is_valid_with_attributes(field.attributes)
        ]
        self.fields = filtered_fields
        return self

    def _mapping_alias_annotation(self, ctx: RenderContext) -> str | None:
        """Returns the mapping alias dict (i.e. dict[<x>, <x>]) for a struct, or None if it's not that kind of struct."""
        plain_pairs =      [field for field in self.fields if isinstance(field, PairSchema) and isinstance(field.key, str)]  # fmt: skip
        schema_key_pairs = [field for field in self.fields if isinstance(field, PairSchema) and not isinstance(field.key, str)]
        if len(schema_key_pairs) != 1 or plain_pairs:  # If it's not a single pair, it's just a simple dict.
            # TODO: Because a mapping can't be typed inline yet in Python, we don't generate a TypedDict, instead just put the first here.
            # I don't know if they specify more than one, perhaps we can chain them together, i.e. ` | `?
            return None

        field = schema_key_pairs[0]
        assert not isinstance(field.key, str)
        return f"dict[{field.key.to_annotation(ctx)}, {field.type.to_annotation(ctx)}]"

    def _calculate_inherited_names(self, template_type_names: list[str], ctx: RenderContext) -> list[str]:
        if template_type_names:
            ctx.required_imports.add(Import("typing", "Generic", False, True))
            return [f"Generic[{', '.join(template_type_names)}]"]
        return []

    def to_materialized_annotation(self, class_name: str, ctx: RenderContext) -> str:
        """Both adds itself to the list of created dataclasses, plus returns the annotation materialized."""
        ctx.add_dataclass(self.to_python_code(class_name, ctx))
        type_param_names = sorted(symbol_path_to_object_name(path) for path in ctx.local_type_params)
        type_args = f"[{', '.join(type_param_names)}]" if type_param_names else ""
        return f"{class_name}{type_args}"

    def _render_dataclass_from_struct(self, class_name: str, template_type_names: list[str], ctx: RenderContext) -> list[str]:
        # Collects Structs' inherrited children, e.g. Class(PredicateOffset)
        inherited_names = SpreadFieldSchema.collect_inherited_base_names(self.fields, ctx)
        inherited_names += self._calculate_inherited_names(template_type_names, ctx)
        lines: list[str] = ["@dataclass(kw_only=True)"]
        ctx.required_imports.add(Import("dataclasses", "dataclass", False, True))
        lines.append(
            f"class {class_name}:"
            if not inherited_names else
            f"class {class_name}({', '.join(inherited_names)}):"
        )

        # Collect field lines, separating required vs optional to satisfy dataclass ordering
        required_field_lines: list[str] = []
        optional_field_lines: list[str] = []

        # PairSchema is basically key_name, key_value, the only other possible type is SpreadFields, which we handle differently.
        assert all(isinstance(field, (PairSchema, SpreadFieldSchema)) for field in self.fields)
        pair_fields = SpreadFieldSchema.collect_inlined_pair_fields(self.fields)
        if not pair_fields:
            lines.append("    pass")

        for pair_field in pair_fields:
            key = PairSchema.clean_key(pair_field.key)  # type: ignore[arg-type]
            if isinstance(pair_field.type, StructSchema) and pair_field.type._mapping_alias_annotation(ctx) is None:
                nested_struct_name = PairSchema.nested_struct_name(key)
                annotation = pair_field.type.to_materialized_annotation(nested_struct_name, ctx)
            elif isinstance(pair_field.type, ListSchema):
                annotation = pair_field.type.to_annotation(ctx, PairSchema.nested_struct_name(key))
            else:
                annotation = pair_field.type.to_annotation(ctx)
            description = pair_field.description_text()
            comment = f"  # {description}" if description else ""
            if not annotation.strip() or annotation == "None":
                continue  # Empty unions represent "no local type" here; skip so parent members can remain authoritative.

            line = f"    {key}: {annotation}" + (" | None = None" if pair_field.optional else "") + comment
            if pair_field.optional:
                optional_field_lines.append(line)
            else:
                required_field_lines.append(line)

        # Write required fields first, then optional fields (to allow Pydantic's BaseModel to not complain about defaults before required fields)
        lines.extend(required_field_lines)
        lines.extend(optional_field_lines)
        return lines + [""]

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        mapping_alias = self._mapping_alias_annotation(ctx)
        if mapping_alias is not None:
            # This is exclusively type <x>[type?] = dict[<key>, <value>]
            template_type_names = sorted(symbol_path_to_object_name(path) for path in ctx.local_type_params)
            template_type_names_string = f"[{', '.join(template_type_names)}]" if template_type_names else ""
            return [f"type {class_name}{template_type_names_string} = {mapping_alias}\n"]

        SpreadFieldSchema.collect_runtime_symbol_imports(self.fields, ctx)  # Attaches them to ctx

        # Discover unresolved symbolic refs (e.g. ::java::...::T) before building Generic[...] bases.
        # These become local type params instead of invalid import targets.
        # Because ctx is being passed in, it can actually mutate and change the imports - intentionally.
        [
            field.type.to_annotation(ctx)
            for field in SpreadFieldSchema.collect_inlined_pair_fields(self.fields)
            if not isinstance(field.type, StructSchema)
            and not (isinstance(field.type, ListSchema) and field.type.contains_inline_struct())
        ]

        # Keep Generic parameter order stable across runs (local_type_params is a set).
        template_type_names = sorted(symbol_path_to_object_name(path) for path in ctx.local_type_params)

        return self._render_dataclass_from_struct(class_name=class_name, template_type_names=template_type_names, ctx=ctx)

    def to_annotation(self, ctx: RenderContext) -> str:
        mapping_alias = self._mapping_alias_annotation(ctx)
        if mapping_alias is not None:
            return mapping_alias

        from itertools import chain

        pair_schemas = [x for x in self.fields if isinstance(x, PairSchema)]
        union_schemas = [x for x in self.fields if isinstance(x, UnionSchema)]
        spread_schemas = [x for x in self.fields if isinstance(x, SpreadFieldSchema)]
        annotations = ["Any" for x in chain(pair_schemas, union_schemas, spread_schemas)] or ["Any"]  # TODO: Obviously we need to do this.
        ctx.required_imports.add(Import("typing", "Any", type_checking_only=False, is_builtin=True))
        return " | ".join(set(dict.fromkeys(annotations)))


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
    """No idea, this is weird... Seems like it's a bit like spread but from the custom registry?"""
    kind: Literal["dispatcher"] = Field(repr=False)
    parallel_indices: list[StaticIndexSchema | DynamicIndexSchema] = Field(alias="parallelIndices")
    registry: str

    def to_annotation(self, ctx: RenderContext) -> str:
        import_target = symbol_path_to_import_string_and_name(self.registry)
        if import_target is None or True:  # TODO: Remove OR TRUE to return functionality.
            ctx.required_imports.add(Import("typing", "Any", type_checking_only=False, is_builtin=True))
            return "Any"

        module, identifier = import_target  # type: ignore[unreachable]
        ctx.required_imports.add(Import(module, identifier, type_checking_only=True, is_builtin=False))
        return identifier


class TreeSchema(BaseSchema):
    """Represents a 'tree' structure, found inside an Attribute's value.
    Example: ::java::data::worldgen::attribute::PositionalEnvironmentAttribute """
    kind: Literal["tree"] = Field(repr=False)
    values: TreeValueSchema


class TreeValueSchema(RootModel[dict[str, TreeSchema | LiteralSchema]]):
    """Represents the 'values' part of a TreeSchema. It's a flexible dictionary."""
    root: dict[str, TreeSchema | LiteralSchema]


type MCDocDispatcherSchemaTypes = (
    AnySchema | BooleanSchema | ByteSchema | ConcreteSchema | DispatcherSchema | DynamicIndexSchema | EnumSchema
    | FloatSchema | IndexedSchema | IntArraySchema | IntSchema | ListSchema | LiteralSchema | LongSchema
    | PairSchema | ReferenceSchema | ShortSchema | SpreadFieldSchema | StaticIndexSchema | StringSchema
    | StructSchema | TemplateSchema | TreeSchema | TupleSchema | UnionSchema
)


class MCDocDispatcher(BaseSchema):
    """Represents one registry entry from "mcdoc/dispatcher".

    Shape after kind injection:
    {
        "kind": "mcdocdispatcher",
        "%none": {"kind": "struct", ...},
        "custom_case": {"kind": "union", ...},
    }
    """
    kind: Literal["mcdocdispatcher"] = Field(repr=False)
    branches: dict[str, Annotated[MCDocDispatcherSchemaTypes, Field(discriminator="kind")]] = Field(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def collect_branches(cls, data: object) -> object:
        if isinstance(data, dict):
            branches = {k: v for k, v in data.items() if k not in ["kind", "attribute"]}
            regular = {k: v for k, v in data.items() if k in ["kind", "attribute"]}
            return regular | {"branches": branches}
        return data

    def to_python_code(self, class_name: str, ctx: RenderContext) -> list[str]:
        if not self.branches:
            return [f"type {class_name} = None"]

        rendered_struct_members: list[str] = []
        union_member_annotations: list[str] = []
        struct_index = 0

        for member in self.branches.values():
            if isinstance(member, StructSchema):
                struct_index += 1
                member_name = f"{class_name}Struct{struct_index}"
                rendered_struct_members.extend(member.to_python_code(member_name, ctx))
                union_member_annotations.append(member_name)
            else:
                union_member_annotations.append(member.to_annotation(ctx))

        alias_line = f"type {class_name} = {' | '.join(list(dict.fromkeys(union_member_annotations)))}"
        return rendered_struct_members + [alias_line]

    def remove_version_data(self) -> Self:
        for schema in self.branches.values():
            schema.remove_version_data()
        return self


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================

type KindOption = Literal[
    "int", "string", "float", "double", "boolean", "short", "long", "byte", "literal", "any",
    "list", "tuple", "int_array", "enum",
    "concrete", "indexed", "reference", "union", "pair", "spread",
    "template", "struct", "dynamic", "static", "dispatcher", "tree", "mcdocdispatcher",
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
    "mcdocdispatcher": MCDocDispatcher,
}
