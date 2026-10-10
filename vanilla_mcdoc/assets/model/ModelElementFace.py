"""
Generated from symbols.json for ::java::assets::model::ModelElementFace
Local link to file: vanilla_mcdoc/assets/model/ModelElementFace.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Direction import Direction


class ModelElementFace(GeneratedModel):
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None
