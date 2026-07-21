# Generated from symbols.json for ::java::data::worldgen::biome::GrassColorModifier
from enum import Enum


class GrassColorModifier(Enum):
    NONE = "none"
    DARKFOREST = "dark_forest"  # Grass color will be average of the base color and `#28340a`.
    SWAMP = "swamp"  # Grass color will be either `#4c763c` or `#6a7039`, depending on block position.  The base color is ignored.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::GrassColorModifier": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "None",
                "value": "none"
            },
            {
                "desc": "Grass color will be average of the base color and `#28340a`.",
                "identifier": "DarkForest",
                "value": "dark_forest"
            },
            {
                "desc": "Grass color will be either `#4c763c` or `#6a7039`, depending on block position. \\\nThe base color is ignored.",
                "identifier": "Swamp",
                "value": "swamp"
            }
        ]
    }
}

