"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ColorModifierType
Local link to file: generated_symbols/data/worldgen/attribute/modifier/ColorModifierType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ColorModifierType(StrEnum):
    OVERRIDE = "override"
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    ALPHABLEND = "alpha_blend"
    BLENDTOGRAY = "blend_to_gray"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::ColorModifierType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Override",
                "value": "override"
            },
            {
                "identifier": "Add",
                "value": "add"
            },
            {
                "identifier": "Subtract",
                "value": "subtract"
            },
            {
                "identifier": "Multiply",
                "value": "multiply"
            },
            {
                "identifier": "AlphaBlend",
                "value": "alpha_blend"
            },
            {
                "identifier": "BlendToGray",
                "value": "blend_to_gray"
            }
        ]
    }
}

