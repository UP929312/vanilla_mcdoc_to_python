"""
Generated from symbols.json for ::java::data::worldgen::feature::SpeleothemClusterPlacementMode
Local link to file: generated_symbols/data/worldgen/feature/SpeleothemClusterPlacementMode.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class SpeleothemClusterPlacementMode(StrEnum):
    FLOORANDCEILING = "floor_and_ceiling"
    FLOOR = "floor_only"
    CEILING = "ceiling_only"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SpeleothemClusterPlacementMode": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "FloorAndCeiling",
                "value": "floor_and_ceiling"
            },
            {
                "identifier": "Floor",
                "value": "floor_only"
            },
            {
                "identifier": "Ceiling",
                "value": "ceiling_only"
            }
        ]
    }
}

