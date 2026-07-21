# Generated from symbols.json for ::java::assets::item_definition::TimeSource
from enum import Enum


class TimeSource(Enum):
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

