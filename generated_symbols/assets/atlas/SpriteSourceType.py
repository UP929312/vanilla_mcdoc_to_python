"""
Generated from symbols.json for ::java::assets::atlas::SpriteSourceType
Local link to file: generated_symbols/assets/atlas/SpriteSourceType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class SpriteSourceType(StrEnum):
    SINGLE = "single"
    DIRECTORY = "directory"
    FILTER = "filter"
    UNSTITCH = "unstitch"
    PALETTEDPERMUTATIONS = "paletted_permutations"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::SpriteSourceType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Single",
                "value": "single"
            },
            {
                "identifier": "Directory",
                "value": "directory"
            },
            {
                "identifier": "Filter",
                "value": "filter"
            },
            {
                "identifier": "Unstitch",
                "value": "unstitch"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "identifier": "PalettedPermutations",
                "value": "paletted_permutations"
            }
        ]
    }
}

