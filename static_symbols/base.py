import importlib
import sys
from functools import cache
from typing import Any

from pydantic import BaseModel, ConfigDict, GetCoreSchemaHandler
from pydantic_core import CoreSchema

PACKAGE = __name__.split(".", maxsplit=1)[0]


@cache  # Only ever needs doing once
def import_annotation_types() -> None:
    """Generated modules only import the types their annotations use under `if TYPE_CHECKING:`, because importing them
    for real while the package is still being imported would be circular. When a model is first used, importing has
    finished, so this imports them for real, into each module (type_checking_imports.py says what they are)."""
    type_checking_imports: dict[str, dict[str, tuple[str, str]]] = importlib.import_module(f"{PACKAGE}.type_checking_imports").TYPE_CHECKING_IMPORTS
    for module_name, names in type_checking_imports.items():
        module = importlib.import_module(module_name)
        for name, (source, attribute) in names.items():
            setattr(module, name, getattr(importlib.import_module(source), attribute))

    # Pydantic evaluates a model's inherited fields in the model's own module, not the parent's, so give each module the
    # names its models' parents' modules have too (without replacing its own, which may be aliased differently).
    for module in [module for name, module in tuple(sys.modules.items()) if name.startswith(f"{PACKAGE}.")]:
        models = [value for value in vars(module).values() if isinstance(value, type) and issubclass(value, BaseModel) and value.__module__ == module.__name__]
        for parent in {parent for model in models for parent in model.__mro__[1:] if parent.__module__.startswith(f"{PACKAGE}.")}:
            for name, value in vars(sys.modules[parent.__module__]).items():
                vars(module).setdefault(name, value)


class GeneratedModel(BaseModel):
    model_config = ConfigDict(
        defer_build=True,  # Build a model's schema when it's first used, rather than when it's defined
        extra="allow",  # Keep any data we don't model (yet), rather than silently dropping it
        validate_by_name=True, serialize_by_alias=True,  # Renamed fields (e.g. `from_`) are aliased to their real JSON keys
    )

    @classmethod
    def model_rebuild(cls, **kwargs: Any) -> bool | None:
        """Pydantic calls this itself the first time a model is used, e.g. `Smelting(...)` or `Smelting.model_validate(...)`."""
        if "_types_namespace" in kwargs and not cls.__pydantic_complete__:
            # Pydantic making e.g. MinMaxBounds[int] rebuilds MinMaxBounds "in case new types have been defined", which
            # builds its whole schema (and of everything it uses) for every one made. defer_build builds it when it's used.
            return None
        import_annotation_types()
        return super().model_rebuild(**kwargs)

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[BaseModel], handler: GetCoreSchemaHandler) -> CoreSchema:  # pylint: disable=arguments-differ  # Pydantic wraps the original
        """Pydantic calls this when something else uses this model, e.g. TypeAdapter(Dialog) for a union of models (which
        never calls model_rebuild), so the types have to be imported here too."""
        import_annotation_types()
        return handler(source)
