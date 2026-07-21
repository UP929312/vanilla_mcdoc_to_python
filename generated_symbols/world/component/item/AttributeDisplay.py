# Generated from symbols.json for ::java::world::component::item::AttributeDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.AttributeDisplayType import AttributeDisplayType


@dataclass(kw_only=True)
class AttributeDisplay:
    type: AttributeDisplayType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttributeDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::AttributeDisplayType"
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
                    "registry": "minecraft:attribute_display"
                }
            }
        ]
    }
}

