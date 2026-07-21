# Generated from symbols.json for ::java::world::block::jigsaw::JointType
from enum import Enum


class JointType(Enum):
    ROLLABLE = "rollable"  # The structure can be rotated
    ALIGNED = "aligned"  # The structure cannot be transformed


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::jigsaw::JointType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "The structure can be rotated",
                "identifier": "Rollable",
                "value": "rollable"
            },
            {
                "desc": "The structure cannot be transformed",
                "identifier": "Aligned",
                "value": "aligned"
            }
        ]
    }
}

