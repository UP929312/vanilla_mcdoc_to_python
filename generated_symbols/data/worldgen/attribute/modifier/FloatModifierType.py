"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatModifierType
Local link to file: generated_symbols/data/worldgen/attribute/modifier/FloatModifierType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class FloatModifierType(StrEnum):
    OVERRIDE = "override"
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    ALPHABLEND = "alpha_blend"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::FloatModifierType": {
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
                "identifier": "Minimum",
                "value": "minimum"
            },
            {
                "identifier": "Maximum",
                "value": "maximum"
            },
            {
                "identifier": "AlphaBlend",
                "value": "alpha_blend"
            }
        ]
    }
}

