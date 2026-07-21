# Generated from symbols.json for ::java::assets::item_definition::EndCube
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.EndCubeEffectType import EndCubeEffectType


@dataclass(kw_only=True)
class EndCube:
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

