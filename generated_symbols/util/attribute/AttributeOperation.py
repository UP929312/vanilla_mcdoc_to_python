# Generated from symbols.json for ::java::util::attribute::AttributeOperation
from enum import Enum


class AttributeOperation(Enum):
    ADDVALUE = "add_value"  # Adds all of the modifiers' amounts to the current value of the attribute.
    ADDMULTIPLIEDBASE = "add_multiplied_base"  # Multiplies the current value of the attribute by `(1 + x)`, where `x` is the sum of the modifiers' amounts.
    ADDMULTIPLIEDTOTAL = "add_multiplied_total"  # For every modifier, multiplies the current value of the attribute by `(1 + x)`, where `x` is the amount of the particular modifier.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::attribute::AttributeOperation": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Adds all of the modifiers' amounts to the current value of the attribute.",
                "identifier": "AddValue",
                "value": "add_value"
            },
            {
                "desc": "Multiplies the current value of the attribute by `(1 + x)`,\nwhere `x` is the sum of the modifiers' amounts.",
                "identifier": "AddMultipliedBase",
                "value": "add_multiplied_base"
            },
            {
                "desc": "For every modifier, multiplies the current value of the attribute by `(1 + x)`,\nwhere `x` is the amount of the particular modifier.",
                "identifier": "AddMultipliedTotal",
                "value": "add_multiplied_total"
            }
        ]
    }
}

