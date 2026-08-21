"""
Generated from symbols.json for ::java::world::entity::mob::breedable::armadillo::ArmadilloState
Local link to file: generated_symbols/world/entity/mob/breedable/armadillo/ArmadilloState.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ArmadilloState(StrEnum):
    IDLE = "idle"
    ROLLING = "rolling"
    SCARED = "scared"
    UNROLLING = "unrolling"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::armadillo::ArmadilloState": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Idle",
                "value": "idle"
            },
            {
                "identifier": "Rolling",
                "value": "rolling"
            },
            {
                "identifier": "Scared",
                "value": "scared"
            },
            {
                "identifier": "Unrolling",
                "value": "unrolling"
            }
        ]
    }
}

