"""
Generated from symbols.json for ::java::data::variants::cow::OptionalCowSounds
Local link to file: vanilla_mcdoc/data/variants/cow/OptionalCowSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class OptionalCowSounds(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'cow_sound_variant'

    ambient_sound: SoundEventRef | None = None
    hurt_sound: SoundEventRef | None = None
    death_sound: SoundEventRef | None = None
    step_sound: SoundEventRef | None = None
