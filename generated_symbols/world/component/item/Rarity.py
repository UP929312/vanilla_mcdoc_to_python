# Generated from symbols.json for ::java::world::component::item::Rarity
from enum import Enum


class Rarity(Enum):
    COMMON = "common"  # White name, or aqua when enchanted.
    UNCOMMON = "uncommon"  # Yellow name, or aqua when enchanted.
    RARE = "rare"  # Aqua name, or light purple when enchanted.
    EPIC = "epic"  # Light purple name.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Rarity": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "White name, or aqua when enchanted.",
                "identifier": "Common",
                "value": "common"
            },
            {
                "desc": "Yellow name, or aqua when enchanted.",
                "identifier": "Uncommon",
                "value": "uncommon"
            },
            {
                "desc": "Aqua name, or light purple when enchanted.",
                "identifier": "Rare",
                "value": "rare"
            },
            {
                "desc": "Light purple name.",
                "identifier": "Epic",
                "value": "epic"
            }
        ]
    }
}

