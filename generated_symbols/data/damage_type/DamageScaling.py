# Generated from symbols.json for ::java::data::damage_type::DamageScaling
from enum import Enum


class DamageScaling(Enum):
    NEVER = "never"  # Always the same.
    ALWAYS = "always"  # Always scale with difficulty.
    LIVINGNONPLAYER = "when_caused_by_living_non_player"  # Scale with difficulty if it was caused by a living entity who is not a player.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::damage_type::DamageScaling": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Always the same.",
                "identifier": "Never",
                "value": "never"
            },
            {
                "desc": "Always scale with difficulty.",
                "identifier": "Always",
                "value": "always"
            },
            {
                "desc": "Scale with difficulty if it was caused by a living entity who is not a player.",
                "identifier": "LivingNonPlayer",
                "value": "when_caused_by_living_non_player"
            }
        ]
    }
}

