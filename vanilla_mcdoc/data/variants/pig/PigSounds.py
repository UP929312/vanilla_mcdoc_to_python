"""
Generated from symbols.json for ::java::data::variants::pig::PigSounds
Local link to file: vanilla_mcdoc/data/variants/pig/PigSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class PigSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'pig_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef
    eat_sound: SoundEventRef
