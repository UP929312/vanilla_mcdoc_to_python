"""
Generated from symbols.json for ::java::data::variants::cow::CowSounds
Local link to file: vanilla_mcdoc/data/variants/cow/CowSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class CowSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'cow_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef
