# Generated from symbols.json for ::java::data::damage_type::DamageEffects
from enum import Enum


class DamageEffects(Enum):
    HURT = "hurt"  # Default hurt sound.
    THORNS = "thorns"  # Thorns hurt sound.
    DROWNING = "drowning"  # Drowing sound.
    BURNING = "burning"  # A single tick of burning hurt sound.
    POKING = "poking"  # Berry bush poke sound.
    FREEZING = "freezing"  # A single tick of freezing hurt sound.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::damage_type::DamageEffects": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Default hurt sound.",
                "identifier": "Hurt",
                "value": "hurt"
            },
            {
                "desc": "Thorns hurt sound.",
                "identifier": "Thorns",
                "value": "thorns"
            },
            {
                "desc": "Drowing sound.",
                "identifier": "Drowning",
                "value": "drowning"
            },
            {
                "desc": "A single tick of burning hurt sound.",
                "identifier": "Burning",
                "value": "burning"
            },
            {
                "desc": "Berry bush poke sound.",
                "identifier": "Poking",
                "value": "poking"
            },
            {
                "desc": "A single tick of freezing hurt sound.",
                "identifier": "Freezing",
                "value": "freezing"
            }
        ]
    }
}

