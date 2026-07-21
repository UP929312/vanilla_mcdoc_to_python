# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ColorAttributeModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType


@dataclass(kw_only=True)
class ColorAttributeModifier:
    modifier: ColorModifierType
    argument: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::ColorAttributeModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::modifier::ColorModifierType"
                }
            },
            {
                "kind": "pair",
                "key": "argument",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "modifier"
                            ]
                        }
                    ],
                    "registry": "minecraft:environment_attribute_color_modifier"
                }
            }
        ]
    }
}

