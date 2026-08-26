"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplay
Local link to file: generated_symbols/world/component/item/AttributeDisplay.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.world.component.item.AttributeDisplayTextOverride import AttributeDisplayTextOverride


@dataclass(kw_only=True)
class AttributeDisplayDefault:
    type: Literal['minecraft:default']


@dataclass(kw_only=True)
class AttributeDisplayHidden:
    type: Literal['minecraft:hidden']


@dataclass(kw_only=True)
class AttributeDisplayOverride(AttributeDisplayTextOverride):
    type: Literal['minecraft:override']


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

