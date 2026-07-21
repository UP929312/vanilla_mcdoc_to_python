# Generated from symbols.json for ::java::world::entity::mob::breedable::panda::Gene
from enum import Enum


class Gene(Enum):
    NORMAL = "normal"  # (dominant)
    LAZY = "lazy"  # (dominant)
    WORRIED = "worried"  # (dominant)
    PLAYFUL = "playful"  # (dominant)
    BROWN = "brown"  # (recessive)
    WEAK = "weak"  # (recessive)
    AGGRESSIVE = "aggressive"  # (dominant)


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::panda::Gene": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "(dominant)",
                "identifier": "Normal",
                "value": "normal"
            },
            {
                "desc": "(dominant)",
                "identifier": "Lazy",
                "value": "lazy"
            },
            {
                "desc": "(dominant)",
                "identifier": "Worried",
                "value": "worried"
            },
            {
                "desc": "(dominant)",
                "identifier": "Playful",
                "value": "playful"
            },
            {
                "desc": "(recessive)",
                "identifier": "Brown",
                "value": "brown"
            },
            {
                "desc": "(recessive)",
                "identifier": "Weak",
                "value": "weak"
            },
            {
                "desc": "(dominant)",
                "identifier": "Aggressive",
                "value": "aggressive"
            }
        ]
    }
}

