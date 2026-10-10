"""
Generated from symbols.json for ::java::assets::texture_meta::GuiSpriteScaling
Local link to file: generated_symbols/assets/texture_meta/GuiSpriteScaling.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.assets.texture_meta.NineSlice import NineSlice
from generated_symbols.assets.texture_meta.TileScaling import TileScaling
from generated_symbols.base import GeneratedModel


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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::GuiSpriteScaling": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::texture_meta::GuiSpriteScalingType"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:gui_sprite_scaling"
                }
            }
        ]
    }
}
