"""
Generated from symbols.json for ::java::data::damage_type::DamageEffects
Local link to file: vanilla_mcdoc/data/damage_type/DamageEffects.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DamageEffects(StrEnum):
    HURT = "hurt"  # Default hurt sound.
    THORNS = "thorns"  # Thorns hurt sound.
    DROWNING = "drowning"  # Drowing sound.
    BURNING = "burning"  # A single tick of burning hurt sound.
    POKING = "poking"  # Berry bush poke sound.
    FREEZING = "freezing"  # A single tick of freezing hurt sound.
