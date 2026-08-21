"""
Generated from symbols.json for ::java::world::entity::mob::player::Gamemode
Local link to file: generated_symbols/world/entity/mob/player/Gamemode.py
"""
# ~~~ CODE ~~~
from enum import IntEnum


class Gamemode(IntEnum):
    SURVIVAL = 0
    CREATIVE = 1
    ADVENTURE = 2
    SPECTATOR = 3


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::Gamemode": {
        "kind": "enum",
        "enumKind": "int",
        "values": [
            {
                "identifier": "Survival",
                "value": 0
            },
            {
                "identifier": "Creative",
                "value": 1
            },
            {
                "identifier": "Adventure",
                "value": 2
            },
            {
                "identifier": "Spectator",
                "value": 3
            }
        ]
    }
}

