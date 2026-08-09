# Generated from symbols.json for ::java::assets::texture_meta::GuiSpriteScaling
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.NineSliceBorder import NineSliceBorder


@dataclass(kw_only=True)
class GuiSpriteScalingNineSlice:
    type: Literal['minecraft:nine_slice']
    width: Annotated[int, 'Range | Min `1` and above | inclusive']
    height: Annotated[int, 'Range | Min `1` and above | inclusive']
    border: Annotated[int, 'Range | Min `1` and above | inclusive'] | NineSliceBorder
    stretch_inner: bool | None = None  # Defaults to `false`.


@dataclass(kw_only=True)
class GuiSpriteScalingStretch:
    type: Literal['minecraft:stretch']


@dataclass(kw_only=True)
class GuiSpriteScalingTile:
    type: Literal['minecraft:tile']
    width: Annotated[int, 'Range | Min `1` and above | inclusive']
    height: Annotated[int, 'Range | Min `1` and above | inclusive']


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

