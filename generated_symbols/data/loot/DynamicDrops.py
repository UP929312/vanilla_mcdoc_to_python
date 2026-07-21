# Generated from symbols.json for ::java::data::loot::DynamicDrops
from enum import Enum


class DynamicDrops(Enum):
    CONTENTS = "contents"  # Drops the items in a shulker box.
    SHERDS = "sherds"  # Drops the sherds of a decorated pot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::DynamicDrops": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Drops the items in a shulker box.",
                "identifier": "Contents",
                "value": "contents"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "desc": "Drops the sherds of a decorated pot.",
                "identifier": "Sherds",
                "value": "sherds"
            }
        ]
    }
}

