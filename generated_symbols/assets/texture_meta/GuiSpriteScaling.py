# Generated from symbols.json for ::java::assets::texture_meta::GuiSpriteScaling
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.GuiSpriteScalingType import GuiSpriteScalingType


@dataclass(kw_only=True)
class GuiSpriteScaling:
    type: GuiSpriteScalingType


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

