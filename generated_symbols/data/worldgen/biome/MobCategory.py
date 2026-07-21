# Generated from symbols.json for ::java::data::worldgen::biome::MobCategory
from enum import Enum


class MobCategory(Enum):
    MONSTER = "monster"
    CREATURE = "creature"
    AMBIENT = "ambient"
    AXOLOTLS = "axolotls"
    UNDERGROUNDWATERCREATURE = "underground_water_creature"
    WATERCREATURE = "water_creature"
    WATERAMBIENT = "water_ambient"
    MISC = "misc"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::MobCategory": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Monster",
                "value": "monster"
            },
            {
                "identifier": "Creature",
                "value": "creature"
            },
            {
                "identifier": "Ambient",
                "value": "ambient"
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
                "identifier": "Axolotls",
                "value": "axolotls"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "identifier": "UndergroundWaterCreature",
                "value": "underground_water_creature"
            },
            {
                "identifier": "WaterCreature",
                "value": "water_creature"
            },
            {
                "identifier": "WaterAmbient",
                "value": "water_ambient"
            },
            {
                "identifier": "Misc",
                "value": "misc"
            }
        ]
    }
}

