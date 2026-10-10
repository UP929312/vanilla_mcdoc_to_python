"""
Generated from symbols.json for ::java::data::advancement::predicate::EquipmentPredicateSlot
Local link to file: vanilla_mcdoc/data/advancement/predicate/EquipmentPredicateSlot.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class EquipmentPredicateSlot(StrEnum):
    MAINHAND = "mainhand"
    OFFHAND = "offhand"
    HEAD = "head"
    CHEST = "chest"
    LEGS = "legs"
    FEET = "feet"
    BODY = "body"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EquipmentPredicateSlot": {
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
            }
        ]
    }
}
