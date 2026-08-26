"""
Generated from symbols.json for ::java::assets::texture_meta::GuiSpriteScaling
Local link to file: generated_symbols/assets/texture_meta/GuiSpriteScaling.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.assets.texture_meta.NineSlice import NineSlice
from generated_symbols.assets.texture_meta.TileScaling import TileScaling


@dataclass(kw_only=True)
class GuiSpriteScalingNineSlice(NineSlice):
    type: Literal['minecraft:nine_slice']


@dataclass(kw_only=True)
class GuiSpriteScalingStretch:
    type: Literal['minecraft:stretch']


@dataclass(kw_only=True)
class GuiSpriteScalingTile(TileScaling):
    type: Literal['minecraft:tile']


type GuiSpriteScaling = GuiSpriteScalingNineSlice | GuiSpriteScalingStretch | GuiSpriteScalingTile


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

