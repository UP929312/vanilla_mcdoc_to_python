# Generated from symbols.json for ::java::util::slot::EquipmentSlot
from enum import Enum


class EquipmentSlot(Enum):
    MAINHAND = "mainhand"
    OFFHAND = "offhand"
    HEAD = "head"
    CHEST = "chest"
    LEGS = "legs"
    FEET = "feet"
    BODY = "body"
    SADDLE = "saddle"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::slot::EquipmentSlot": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Mainhand",
                "value": "mainhand"
            },
            {
                "identifier": "Offhand",
                "value": "offhand"
            },
            {
                "identifier": "Head",
                "value": "head"
            },
            {
                "identifier": "Chest",
                "value": "chest"
            },
            {
                "identifier": "Legs",
                "value": "legs"
            },
            {
                "identifier": "Feet",
                "value": "feet"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "identifier": "Body",
                "value": "body"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "identifier": "Saddle",
                "value": "saddle"
            }
        ]
    }
}

