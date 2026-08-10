"""
Generated from symbols.json for ::java::data::worldgen::template_pool::Projection
Local link to file: generated_symbols/data/worldgen/template_pool/Projection.py
"""
# ~~~ CODE ~~~
from enum import Enum


class Projection(Enum):
    RIGID = "rigid"
    TERRAINMATCHING = "terrain_matching"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::Projection": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Rigid",
                "value": "rigid"
            },
            {
                "identifier": "TerrainMatching",
                "value": "terrain_matching"
            }
        ]
    }
}

