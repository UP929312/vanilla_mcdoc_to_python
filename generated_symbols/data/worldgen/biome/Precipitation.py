"""
Generated from symbols.json for ::java::data::worldgen::biome::Precipitation
Local link to file: generated_symbols/data/worldgen/biome/Precipitation.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class Precipitation(StrEnum):
    NONE = "none"
    RAIN = "rain"
    SNOW = "snow"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::Precipitation": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "None",
                "value": "none"
            },
            {
                "identifier": "Rain",
                "value": "rain"
            },
            {
                "identifier": "Snow",
                "value": "snow"
            }
        ]
    }
}

