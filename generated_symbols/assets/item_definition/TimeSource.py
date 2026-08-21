"""
Generated from symbols.json for ::java::assets::item_definition::TimeSource
Local link to file: generated_symbols/assets/item_definition/TimeSource.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class TimeSource(StrEnum):
    DAYTIME = "daytime"
    MOONPHASE = "moon_phase"
    RANDOM = "random"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::TimeSource": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Daytime",
                "value": "daytime"
            },
            {
                "identifier": "MoonPhase",
                "value": "moon_phase"
            },
            {
                "identifier": "Random",
                "value": "random"
            }
        ]
    }
}

