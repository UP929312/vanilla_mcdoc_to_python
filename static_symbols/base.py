import sys
from types import ModuleType
from typing import Any

from pydantic import BaseModel, ConfigDict


class GeneratedModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",  # Keep any data we don't model (yet), rather than silently dropping it
        validate_by_name=True, serialize_by_alias=True,  # Renamed fields (e.g. `from_`) are aliased to their real JSON keys
    )

    def __init__(self, **data: Any) -> None:
        model = type(self)
        if not model.__pydantic_complete__:
            namespace: dict[str, object] = {}
            for module in tuple(sys.modules.values()):
                if isinstance(module, ModuleType) and module.__name__.startswith("generated_symbols"):
                    namespace.update(vars(module))
            model.model_rebuild(_types_namespace=namespace)
        super().__init__(**data)
