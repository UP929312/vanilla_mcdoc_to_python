"""
Generated from symbols.json for ::java::data::loot::function::SetNameTarget
Local link to file: generated_symbols/data/loot/function/SetNameTarget.py
"""
# ~~~ CODE ~~~
from enum import Enum


class SetNameTarget(Enum):
    ITEMNAME = "item_name"
    CUSTOMNAME = "custom_name"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetNameTarget": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "ItemName",
                "value": "item_name"
            },
            {
                "identifier": "CustomName",
                "value": "custom_name"
            }
        ]
    }
}

