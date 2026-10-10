"""
Generated from symbols.json for ::java::data::variants::wolf::WolfSounds
Local link to file: vanilla_mcdoc/data/variants/wolf/WolfSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class WolfSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'wolf_sound_variant'

    ambient_sound: SoundEventRef
    death_sound: SoundEventRef
    growl_sound: SoundEventRef
    hurt_sound: SoundEventRef
    pant_sound: SoundEventRef
    whine_sound: SoundEventRef
