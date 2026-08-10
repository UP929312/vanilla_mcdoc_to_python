# ~~~ WHAT ARE WE TESTING ~~~

# Mapping values that are structs become named dataclasses rather than unions of their field keys.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::model::ModelElementFaceMap
Local link to file: generated_symbols/assets/model/ModelElementFaceMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class ModelElementFaceMapValueStruct:
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None


type ModelElementFaceMap = dict[Direction, ModelElementFaceMapValueStruct]
