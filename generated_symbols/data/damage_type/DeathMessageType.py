"""
Generated from symbols.json for ::java::data::damage_type::DeathMessageType
Local link to file: generated_symbols/data/damage_type/DeathMessageType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DeathMessageType(StrEnum):
    DEFAULT = "default"  # Resulting translation key of `death.attack.` + message_id.
    FALLVARIANTS = "fall_variants"  # Resulting translation key of `death.attack.` + message_id.
    INTENTIONALGAMEDESIGN = "intentional_game_design"  # Resulting translation key of `death.attack.` + message_id + `.link`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::damage_type::DeathMessageType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Resulting translation key of `death.attack.` + message_id.",
                "identifier": "Default",
                "value": "default"
            },
            {
                "desc": "Resulting translation key of `death.attack.` + message_id.",
                "identifier": "FallVariants",
                "value": "fall_variants"
            },
            {
                "desc": "Resulting translation key of `death.attack.` + message_id + `.link`.",
                "identifier": "IntentionalGameDesign",
                "value": "intentional_game_design"
            }
        ]
    }
}

