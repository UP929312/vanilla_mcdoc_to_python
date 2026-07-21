# Generated from symbols.json for ::java::world::component::item::ItemUseAnimation
from enum import Enum


class ItemUseAnimation(Enum):
    NONE = "none"
    EAT = "eat"
    DRINK = "drink"
    BLOCK = "block"
    BOW = "bow"
    OLDTRIDENT = "spear"  # Used for Tridents.
    TRIDENT = "trident"
    SPEAR = "spear"
    CROSSBOW = "crossbow"
    SPYGLASS = "spyglass"
    TOOTHORN = "toot_horn"  # Used for Goat Horns.
    BRUSH = "brush"
    BUNDLE = "bundle"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ItemUseAnimation": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "None",
                "value": "none"
            },
            {
                "identifier": "Eat",
                "value": "eat"
            },
            {
                "identifier": "Drink",
                "value": "drink"
            },
            {
                "identifier": "Block",
                "value": "block"
            },
            {
                "identifier": "Bow",
                "value": "bow"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Used for Tridents.",
                "identifier": "OldTrident",
                "value": "spear"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "identifier": "Trident",
                "value": "trident"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "identifier": "Spear",
                "value": "spear"
            },
            {
                "identifier": "Crossbow",
                "value": "crossbow"
            },
            {
                "identifier": "Spyglass",
                "value": "spyglass"
            },
            {
                "desc": "Used for Goat Horns.",
                "identifier": "TootHorn",
                "value": "toot_horn"
            },
            {
                "identifier": "Brush",
                "value": "brush"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "identifier": "Bundle",
                "value": "bundle"
            }
        ]
    }
}

