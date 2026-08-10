"""
Generated from symbols.json for ::java::data::worldgen::attribute::BedRuleType
Local link to file: generated_symbols/data/worldgen/attribute/BedRuleType.py
"""
# ~~~ CODE ~~~
from enum import Enum


class BedRuleType(Enum):
    ALWAYS = "always"
    WHENDARK = "when_dark"
    NEVER = "never"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::BedRuleType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Always",
                "value": "always"
            },
            {
                "identifier": "WhenDark",
                "value": "when_dark"
            },
            {
                "identifier": "Never",
                "value": "never"
            }
        ]
    }
}

