"""
Generated from symbols.json for ::java::data::variants::pig::OptionalPigSounds
Local link to file: vanilla_mcdoc/data/variants/pig/OptionalPigSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class OptionalPigSounds(GeneratedModel):
    ambient_sound: SoundEventRef | None = None
    hurt_sound: SoundEventRef | None = None
    death_sound: SoundEventRef | None = None
    step_sound: SoundEventRef | None = None
    eat_sound: SoundEventRef | None = None
