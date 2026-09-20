"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplay
Local link to file: generated_symbols/world/component/item/AttributeDisplay.py
"""
# ~~~ CODE ~~~
from typing import Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.world.component.item.AttributeDisplayTextOverride import AttributeDisplayTextOverride


class AttributeDisplayDefault(GeneratedModel):
    type: Literal['minecraft:default'] = 'minecraft:default'


class AttributeDisplayHidden(GeneratedModel):
    type: Literal['minecraft:hidden'] = 'minecraft:hidden'


class AttributeDisplayOverride(AttributeDisplayTextOverride):
    type: Literal['minecraft:override'] = 'minecraft:override'


type AttributeDisplay = AttributeDisplayDefault | AttributeDisplayHidden | AttributeDisplayOverride


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

