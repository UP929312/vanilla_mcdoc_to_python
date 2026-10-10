"""
Generated from symbols.json for ::java::assets::item_definition::Compass
Local link to file: vanilla_mcdoc/assets/item_definition/Compass.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.CompassTarget import CompassTarget


class Compass(GeneratedModel):
    target: CompassTarget
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Compass": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::CompassTarget"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to oscillate for some time around target before settling. Defaults to True.",
                "key": "wobble",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
