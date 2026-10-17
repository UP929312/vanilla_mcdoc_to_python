"""This file is part of the static_symbols package, which contains models for Minecraft data files.
It defines a base model class, GeneratedModel, that extends Pydantic's BaseModel with additional functionality
for deferred schema building and JSON schema generation.
The module also includes utility functions for importing annotation types,
and handling discriminated unions.
It's kind of gross, if you have a better way of doing this, please let me know! - Skezza
"""
import importlib
import sys
from collections.abc import Callable
from contextvars import ContextVar
from typing import Any

from pydantic import BaseModel, ConfigDict, GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import CoreSchema, core_schema

PACKAGE = __name__.split(".", maxsplit=1)[0]
# The model GeneratedModel.model_rebuild is building the validator of right now, so __get_pydantic_core_schema__ can tell
# that apart from another model using it (a ContextVar, rather than a plain variable, so two threads can't mix them up)
BUILDING: ContextVar[type[BaseModel] | None] = ContextVar("BUILDING", default=None)
# While models' JSON schemas are being written, the ones still to write, and every model that's been added to it (see
# GeneratedModel._json_schema)
JSON_SCHEMAS_TO_WRITE: ContextVar[tuple[list[CoreSchema], set[type[BaseModel]]] | None] = ContextVar("JSON_SCHEMAS_TO_WRITE", default=None)


def import_annotation_types() -> None:
    """Generated modules import some types only under `if TYPE_CHECKING:`, as importing them for real would be circular,
    e.g. CompositePoolEntry's children are LootPoolEntrys, and LootPoolEntry's variants are CompositePoolEntrys. Editors
    see them, but pydantic needs them at runtime too, to read annotations. So once the package is imported (__init__.py
    calls this), import each one for real, into its module. type_checking_imports.py lists them, e.g.
    {'vanilla_mcdoc.data.loot.CompositePoolEntry': {'LootPoolEntry': ('vanilla_mcdoc.data.loot.LootPoolEntry', 'LootPoolEntry')}}
    for `from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry` in CompositePoolEntry.py."""
    type_checking_imports: dict[str, dict[str, tuple[str, str]]] = importlib.import_module(f"{PACKAGE}.type_checking_imports").TYPE_CHECKING_IMPORTS
    for module_name, names in type_checking_imports.items():
        module = importlib.import_module(module_name)
        for name, (source_module, attribute) in names.items():
            setattr(module, name, getattr(importlib.import_module(source_module), attribute))


def tag_of(field: str) -> Callable[[Any], Any]:
    """For discriminated unions: which member some data (or a model) is, from its `field`, e.g. "minecraft:set_count".
    The tags are resource locations, which can leave out the "minecraft:", so it's added if it is."""
    def tag(value: Any) -> Any:
        found = value.get(field) if isinstance(value, dict) else getattr(value, field, None)
        return f"minecraft:{found}" if isinstance(found, str) and ":" not in found else found
    return tag


class GeneratedModel(BaseModel):
    model_config = ConfigDict(
        defer_build=True,  # Build a model's schema when it's first used, rather than when it's defined
        extra="allow",  # Keep any data we don't model (yet), rather than silently dropping it
        validate_by_name=True, serialize_by_alias=True,  # Renamed fields (e.g. `from_`) are aliased to their real JSON keys
    )

    @classmethod
    def model_rebuild(cls, **kwargs: Any) -> bool | None:
        """Pydantic calls this itself the first time a model is used, e.g. `Smelting(...)` or `Smelting.model_validate(...)`,
        to build its validator."""
        if "_types_namespace" in kwargs and not cls.__pydantic_complete__:
            # Pydantic making e.g. MinMaxBounds[int] rebuilds MinMaxBounds "in case new types have been defined", which
            # builds its whole schema (and of everything it uses) for every one made. defer_build builds it when it's used.
            return None
        kwargs["_types_namespace"] = cls.annotation_names()
        building = BUILDING.set(cls)
        try:
            return super().model_rebuild(**kwargs)
        finally:
            BUILDING.reset(building)

    @classmethod
    def annotation_names(cls) -> dict[str, Any]:
        """The names this model's annotations can use: its module's, and its parents' modules'. Pydantic reads the fields
        a model inherits in the model's module, not where they're written, e.g. RecipeCraftingShaped (in Recipe.py)
        inherits CraftingShaped's fields, which use names only CraftingShaped.py imports. Its own module's go last, so
        they win if a name means something else there."""
        names: dict[str, Any] = {}
        for model in reversed(cls.__mro__):
            if model.__module__.startswith(f"{PACKAGE}."):
                names |= vars(sys.modules[model.__module__])
        return names

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[BaseModel], handler: GetCoreSchemaHandler) -> CoreSchema:  # pylint: disable=arguments-differ  # Pydantic wraps the original
        """Pydantic calls this for the model's own schema, and when something else uses it, e.g. a field, or
        TypeAdapter(Dialog) for a union of models.

        Only its own schema is built in full. Pydantic would otherwise copy the schema of everything a model uses into
        it (and of everything they use...), which for e.g. a loot table is most of the package, and once per model used:
        50 models took 23s and 1.3 GB. So other models are validated with their own validator (built when first needed).
        Pydantic doesn't say which of the two it's asking for, so model_rebuild sets BUILDING to the model it's building."""
        if BUILDING.get() is cls:  # Its own schema
            return handler(source)

        def validate(value: Any) -> tuple[dict[str, Any], dict[str, Any] | None, set[str]]:
            model = cls.__pydantic_validator__.validate_python(value)
            return model.__dict__, model.__pydantic_extra__, model.__pydantic_fields_set__  # What a model schema makes the model from

        # Still a model schema, so errors say where, e.g. `result.ItemStack.id`, and serialized with the model's own serializer
        return core_schema.model_schema(
            cls, core_schema.no_info_plain_validator_function(validate), serialization=core_schema.simple_ser_schema("any"),
            metadata={"pydantic_js_annotation_functions": [cls._json_schema]},
        )

    @classmethod
    def _json_schema(cls, _: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        """The JSON schema for where another model uses this one: a $ref to its own schema, in $defs. Its validator is just
        a function, so pydantic can't write that itself.

        Each model's is written after the one that uses it, rather than inside it, as for e.g. a recipe that goes about 25
        models deep (an item's components, then theirs...), which is too deep for Python. So the first model used writes
        its own, then the ones it uses, and so on, and the rest just add themselves to the list."""
        # Not handler(...), as pydantic's own JSON schema function for models is in it, which swaps $refs for what they
        # refer to, so each model would be written out in full everywhere it's used
        generator: GenerateJsonSchema = handler.generate_json_schema  # type: ignore[attr-defined]  # It's there, just not typed
        if not cls.__pydantic_complete__:
            cls.model_rebuild()
        own_schema = cls.__pydantic_core_schema__
        # e.g. {'type': 'model', 'ref': ...}, or for a model that uses itself, {'type': 'definitions', 'schema': {'type': 'definition-ref', ...}, ...}
        schema = own_schema["schema"] if own_schema["type"] == "definitions" else own_schema
        reference = core_schema.definition_reference_schema(schema["schema_ref"] if schema["type"] == "definition-ref" else schema["ref"])  # pyright: ignore
        if (to_write := JSON_SCHEMAS_TO_WRITE.get()) is None:
            to_write = [own_schema], {cls}
            writing = JSON_SCHEMAS_TO_WRITE.set(to_write)  # pyright: ignore
            try:
                while to_write[0]:
                    generator.generate_inner(to_write[0].pop())  # Puts it in $defs
            finally:
                JSON_SCHEMAS_TO_WRITE.reset(writing)
        elif cls not in to_write[1]:
            to_write[0].append(own_schema)
            to_write[1].add(cls)
        return generator.generate_inner(reference)
