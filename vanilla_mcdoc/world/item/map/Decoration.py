"""
Generated from symbols.json for ::java::world::item::map::Decoration
Local link to file: vanilla_mcdoc/world/item/map/Decoration.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.map.IconByteId import IconByteId


class Decoration(GeneratedModel):
    type: IconByteId  # Decoration type.
    x: float  # World x position.
    z: float  # World z position.
    rot: float  # Rotation of the decoration, measured in degrees clockwise.
