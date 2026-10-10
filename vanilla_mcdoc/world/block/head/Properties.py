"""
Generated from symbols.json for ::java::world::block::head::Properties
Local link to file: vanilla_mcdoc/world/block/head/Properties.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.head.Texture import Texture


class Properties(GeneratedModel):
    textures: list[Texture] | None = None
