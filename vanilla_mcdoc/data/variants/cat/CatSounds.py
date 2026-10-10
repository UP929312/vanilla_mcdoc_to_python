"""
Generated from symbols.json for ::java::data::variants::cat::CatSounds
Local link to file: vanilla_mcdoc/data/variants/cat/CatSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class CatSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'cat_sound_variant'

    ambient_sound: SoundEventRef
    stray_sound: SoundEventRef
    hiss_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    eat_sound: SoundEventRef
    beg_for_food_sound: SoundEventRef
    purr_sound: SoundEventRef
    purreow_sound: SoundEventRef
