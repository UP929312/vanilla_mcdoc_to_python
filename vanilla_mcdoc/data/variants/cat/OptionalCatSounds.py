"""
Generated from symbols.json for ::java::data::variants::cat::OptionalCatSounds
Local link to file: vanilla_mcdoc/data/variants/cat/OptionalCatSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class OptionalCatSounds(GeneratedModel):
    ambient_sound: SoundEventRef | None = None
    stray_ambient_sound: SoundEventRef | None = None
    hiss_sound: SoundEventRef | None = None
    hurt_sound: SoundEventRef | None = None
    death_sound: SoundEventRef | None = None
    eat_sound: SoundEventRef | None = None
    beg_for_food_sound: SoundEventRef | None = None
    purr_sound: SoundEventRef | None = None
    purreow_sound: SoundEventRef | None = None
