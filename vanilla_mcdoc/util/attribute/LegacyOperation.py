"""
Generated from symbols.json for ::java::util::attribute::LegacyOperation
Local link to file: vanilla_mcdoc/util/attribute/LegacyOperation.py
"""
# ~~~ CODE ~~~
from enum import IntEnum


class LegacyOperation(IntEnum):
    ADDITIVE = 0  # aka. `add_value`. Adds all of the modifiers' amounts to the current value of the attribute.
    MULTIPLICATIVE = 1  # aka. `add_multiplied_base`. Multiplies the current value of the attribute by (1 + x), where x is the sum of the modifiers' amounts.
    PERCENTAGE = 2  # aka. `add_multiplied_total`. For every modifier, multiplies the current value of the attribute by (1 + x), where x is the amount of the particular modifier. Functions the same as Operation 1 if there is only a single modifier with operation 1 or 2. However, for multiple modifiers it will multiply the modifiers rather than adding them
