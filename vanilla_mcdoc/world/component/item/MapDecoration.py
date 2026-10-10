"""
Generated from symbols.json for ::java::world::component::item::MapDecoration
Local link to file: vanilla_mcdoc/world/component/item/MapDecoration.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class MapDecoration(GeneratedModel):
    type: Annotated[str, IdSpec(registry='map_decoration_type')]  # Decoration type.
    x: float  # World x position.
    z: float  # World z position.
    rotation: float  # Rotation of the decoration, measured in degrees clockwise.
