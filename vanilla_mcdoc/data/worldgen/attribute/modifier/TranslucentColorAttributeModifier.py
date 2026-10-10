"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::TranslucentColorAttributeModifier
Local link to file: generated_symbols/data/worldgen/attribute/modifier/TranslucentColorAttributeModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from generated_symbols.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB


class TranslucentColorAttributeModifier(GeneratedModel):
    modifier: ColorModifierType
    argument: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::TranslucentColorAttributeModifier": {
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
                    "registry": "minecraft:environment_attribute_argb_color_modifier"
                }
            }
        ]
    }
}
