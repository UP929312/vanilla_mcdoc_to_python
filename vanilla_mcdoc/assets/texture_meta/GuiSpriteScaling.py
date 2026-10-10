"""
Generated from symbols.json for ::java::assets::texture_meta::GuiSpriteScaling
Local link to file: vanilla_mcdoc/assets/texture_meta/GuiSpriteScaling.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.assets.texture_meta.NineSlice import NineSlice
from vanilla_mcdoc.assets.texture_meta.TileScaling import TileScaling
from vanilla_mcdoc.base import GeneratedModel


class GuiSpriteScalingNineSlice(NineSlice):
    type: Literal['minecraft:nine_slice', 'nine_slice'] = 'minecraft:nine_slice'


class GuiSpriteScalingStretch(GeneratedModel):
    type: Literal['minecraft:stretch', 'stretch'] = 'minecraft:stretch'


class GuiSpriteScalingTile(TileScaling):
    type: Literal['minecraft:tile', 'tile'] = 'minecraft:tile'


type GuiSpriteScaling = Annotated[
    GuiSpriteScalingNineSlice | GuiSpriteScalingStretch | GuiSpriteScalingTile,
    Field(discriminator='type'),
]
