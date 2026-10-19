"""
Generated from symbols.json for ::java::data::variants::wolf::OptionalWolfSounds
Local link to file: vanilla_mcdoc/data/variants/wolf/OptionalWolfSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class OptionalWolfSounds(GeneratedModel):
    ambient_sound: SoundEventRef | None = None
    death_sound: SoundEventRef | None = None
    growl_sound: SoundEventRef | None = None
    hurt_sound: SoundEventRef | None = None
    pant_sound: SoundEventRef | None = None
    whine_sound: SoundEventRef | None = None
