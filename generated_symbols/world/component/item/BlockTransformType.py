# Generated from symbols.json for ::java::world::component::item::BlockTransformType
from enum import Enum


class BlockTransformType(Enum):
    SINGLEBLOCK = "single_block"
    COPPERCHEST = "copper_chest"  # If the original block and the transformed block are both copper chests of any kind, the transform applies to the other half of the double chest.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BlockTransformType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "SingleBlock",
                "value": "single_block"
            },
            {
                "desc": "If the original block and the transformed block are both copper chests of any kind, the transform applies to the other half of the double chest.",
                "identifier": "CopperChest",
                "value": "copper_chest"
            }
        ]
    }
}

