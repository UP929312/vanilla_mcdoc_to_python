# Generated from symbols.json for ::java::world::item::HideFlags
from enum import Enum


class HideFlags(Enum):
    ENCHANTMENTS = "1"
    ATTRIBUTEMODIFIERS = "2"
    UNBREAKABLE = "3"
    CANDESTROY = "4"
    CANPLACEON = "5"
    OTHER = "6"
    LEATHERCOLOR = "7"
    TRIM = "8"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::HideFlags": {
        "kind": "enum",
        "enumKind": "int",
        "values": [
            {
                "identifier": "Enchantments",
                "value": 1
            },
            {
                "identifier": "AttributeModifiers",
                "value": 2
            },
            {
                "identifier": "Unbreakable",
                "value": 3
            },
            {
                "identifier": "CanDestroy",
                "value": 4
            },
            {
                "identifier": "CanPlaceOn",
                "value": 5
            },
            {
                "identifier": "Other",
                "value": 6
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16.2"
                            }
                        }
                    }
                ],
                "identifier": "LeatherColor",
                "value": 7
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
                "identifier": "Trim",
                "value": 8
            }
        ]
    }
}

