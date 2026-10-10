"""
Generated from symbols.json for ::java::assets::item_definition::CopperGolemStatue
Local link to file: generated_symbols/assets/item_definition/CopperGolemStatue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose


class CopperGolemStatue(GeneratedModel):
    pose: CopperGolemStatuePose
    texture: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CopperGolemStatue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pose",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::CopperGolemStatuePose"
                }
            },
            {
                "kind": "pair",
                "key": "texture",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}
