"""
Generated from symbols.json for ::java::assets::item_definition::TintSourceType
Local link to file: generated_symbols/assets/item_definition/TintSourceType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class TintSourceType(StrEnum):
    CONSTANT = "constant"
    CUSTOMMODELDATA = "custom_model_data"
    DYE = "dye"
    FIREWORK = "firework"
    GRASS = "grass"
    POTION = "potion"
    TEAM = "team"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::TintSourceType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Constant",
                "value": "constant"
            },
            {
                "identifier": "CustomModelData",
                "value": "custom_model_data"
            },
            {
                "identifier": "Dye",
                "value": "dye"
            },
            {
                "identifier": "Firework",
                "value": "firework"
            },
            {
                "identifier": "Grass",
                "value": "grass"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "identifier": "MapColor",
                "value": "map_color"
            },
            {
                "identifier": "Potion",
                "value": "potion"
            },
            {
                "identifier": "Team",
                "value": "team"
            }
        ]
    }
}

