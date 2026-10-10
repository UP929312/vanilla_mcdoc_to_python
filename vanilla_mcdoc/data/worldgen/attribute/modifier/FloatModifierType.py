"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::FloatModifierType
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/FloatModifierType.py
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
