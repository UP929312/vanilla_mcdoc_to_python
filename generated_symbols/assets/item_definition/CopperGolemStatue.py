# Generated from symbols.json for ::java::assets::item_definition::CopperGolemStatue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose


@dataclass(kw_only=True)
class CopperGolemStatue:
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

