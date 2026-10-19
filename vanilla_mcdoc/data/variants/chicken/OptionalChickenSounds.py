"""
Generated from symbols.json for ::java::data::variants::chicken::OptionalChickenSounds
Local link to file: vanilla_mcdoc/data/variants/chicken/OptionalChickenSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class OptionalChickenSounds(GeneratedModel):
    ambient_sound: SoundEventRef | None = None
    hurt_sound: SoundEventRef | None = None
    death_sound: SoundEventRef | None = None
    step_sound: SoundEventRef | None = None
