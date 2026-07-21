# Generated from symbols.json for ::java::util::attribute::LegacyOperation
from enum import Enum


class LegacyOperation(Enum):
    ADDITIVE = "0"  # aka. `add_value`. Adds all of the modifiers' amounts to the current value of the attribute.
    MULTIPLICATIVE = "1"  # aka. `add_multiplied_base`. Multiplies the current value of the attribute by (1 + x), where x is the sum of the modifiers' amounts.
    PERCENTAGE = "2"  # aka. `add_multiplied_total`. For every modifier, multiplies the current value of the attribute by (1 + x), where x is the amount of the particular modifier. Functions the same as Operation 1 if there is only a single modifier with operation 1 or 2. However, for multiple modifiers it will multiply the modifiers rather than adding them


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::attribute::LegacyOperation": {
        "kind": "enum",
        "enumKind": "int",
        "values": [
            {
                "desc": "aka. `add_value`. Adds all of the modifiers' amounts to the current value of the attribute.",
                "identifier": "Additive",
                "value": 0
            },
            {
                "desc": "aka. `add_multiplied_base`. Multiplies the current value of the attribute by (1 + x),\nwhere x is the sum of the modifiers' amounts.",
                "identifier": "Multiplicative",
                "value": 1
            },
            {
                "desc": "aka. `add_multiplied_total`. For every modifier, multiplies the current value of the attribute by (1 + x),\nwhere x is the amount of the particular modifier.\nFunctions the same as Operation 1 if there is only a single modifier with operation 1 or 2.\nHowever, for multiple modifiers it will multiply the modifiers rather than adding them",
                "identifier": "Percentage",
                "value": 2
            }
        ]
    }
}

