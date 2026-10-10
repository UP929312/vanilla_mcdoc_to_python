"""
Generated from symbols.json for ::java::assets::item_definition::Head
Local link to file: vanilla_mcdoc/assets/item_definition/Head.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.HeadType import HeadType


class Head(GeneratedModel):
    kind: HeadType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/')] | None = None  # Texture to use instead of the texture from `kind`.
    animation: float | None = None  # Controls the animation time for piglin and dragon heads. Defaults to `0`.
