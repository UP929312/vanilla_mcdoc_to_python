# ~~~ WHAT ARE WE TESTING ~~~

# Mapping values that are structs become named models rather than unions of their field keys.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::model::ModelElementFaceMap
Local link to file: vanilla_mcdoc/assets/model/ModelElementFaceMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Direction import Direction


class ModelElementFaceMapValueStruct(GeneratedModel):
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None


type ModelElementFaceMap = dict[Direction, ModelElementFaceMapValueStruct]
