"""
Generated from symbols.json for ::java::data::variants::chicken::ChickenSounds
Local link to file: vanilla_mcdoc/data/variants/chicken/ChickenSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class ChickenSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'chicken_sound_variant'

    ambient_sound: SoundEventRef
    hurt_sound: SoundEventRef
    death_sound: SoundEventRef
    step_sound: SoundEventRef
