"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ColorModifierType
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/ColorModifierType.py
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
