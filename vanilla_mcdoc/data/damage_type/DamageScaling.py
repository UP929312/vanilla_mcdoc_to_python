"""
Generated from symbols.json for ::java::data::damage_type::DamageScaling
Local link to file: vanilla_mcdoc/data/damage_type/DamageScaling.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class DamageScaling(StrEnum):
    NEVER = "never"  # Always the same.
    ALWAYS = "always"  # Always scale with difficulty.
    LIVINGNONPLAYER = "when_caused_by_living_non_player"  # Scale with difficulty if it was caused by a living entity who is not a player.
