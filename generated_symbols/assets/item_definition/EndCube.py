"""
Generated from symbols.json for ::java::assets::item_definition::EndCube
Local link to file: generated_symbols/assets/item_definition/EndCube.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.EndCubeEffectType import EndCubeEffectType


class EndCube(GeneratedModel):
    effect: EndCubeEffectType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::EndCube": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::EndCubeEffectType"
                }
            }
        ]
    }
}

