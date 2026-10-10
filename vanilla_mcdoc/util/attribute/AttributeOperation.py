"""
Generated from symbols.json for ::java::util::attribute::AttributeOperation
Local link to file: vanilla_mcdoc/util/attribute/AttributeOperation.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class AttributeOperation(StrEnum):
    ADDVALUE = "add_value"  # Adds all of the modifiers' amounts to the current value of the attribute.
    ADDMULTIPLIEDBASE = "add_multiplied_base"  # Multiplies the current value of the attribute by `(1 + x)`, where `x` is the sum of the modifiers' amounts.
    ADDMULTIPLIEDTOTAL = "add_multiplied_total"  # For every modifier, multiplies the current value of the attribute by `(1 + x)`, where `x` is the amount of the particular modifier.
