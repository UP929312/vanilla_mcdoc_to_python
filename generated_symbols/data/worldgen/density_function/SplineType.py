"""
Generated from symbols.json for ::java::data::worldgen::density_function::SplineType
Local link to file: generated_symbols/data/worldgen/density_function/SplineType.py
"""
# ~~~ CODE ~~~
from enum import Enum


class SplineType(Enum):
    OFFSET = "offset"
    FACTOR = "factor"
    JAGGEDNESS = "jaggedness"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::SplineType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Offset",
                "value": "offset"
            },
            {
                "identifier": "Factor",
                "value": "factor"
            },
            {
                "identifier": "Jaggedness",
                "value": "jaggedness"
            }
        ]
    }
}

