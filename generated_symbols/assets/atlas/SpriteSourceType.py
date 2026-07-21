# Generated from symbols.json for ::java::assets::atlas::SpriteSourceType
from enum import Enum


class SpriteSourceType(Enum):
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

