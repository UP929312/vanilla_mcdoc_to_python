# Generated from symbols.json for ::java::world::component::item::AttributeDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class AttributeDisplayDefault:
    type: Literal['minecraft:default']


@dataclass(kw_only=True)
class AttributeDisplayHidden:
    type: Literal['minecraft:hidden']


@dataclass(kw_only=True)
class AttributeDisplayOverride:
    type: Literal['minecraft:override']
    value: Text  # The text contents to show for this attribute modifer entry.


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

