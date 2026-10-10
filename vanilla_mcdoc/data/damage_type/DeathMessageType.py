"""
Generated from symbols.json for ::java::data::damage_type::DeathMessageType
Local link to file: vanilla_mcdoc/data/damage_type/DeathMessageType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DeathMessageType(StrEnum):
    DEFAULT = "default"  # Resulting translation key of `death.attack.` + message_id.
    FALLVARIANTS = "fall_variants"  # Resulting translation key of `death.attack.` + message_id.
    INTENTIONALGAMEDESIGN = "intentional_game_design"  # Resulting translation key of `death.attack.` + message_id + `.link`.
