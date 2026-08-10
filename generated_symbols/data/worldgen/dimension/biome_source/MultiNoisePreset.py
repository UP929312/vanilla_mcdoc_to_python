"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoisePreset
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/MultiNoisePreset.py
"""
# ~~~ CODE ~~~
from enum import Enum


class MultiNoisePreset(Enum):
    NETHER = "nether"
    OVERWORLD = "overworld"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::MultiNoisePreset": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Nether",
                "value": "nether"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "identifier": "Overworld",
                "value": "overworld"
            }
        ]
    }
}

