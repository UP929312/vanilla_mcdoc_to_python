"""
Generated from symbols.json for ::java::data::util::SoundEventRef
Local link to file: vanilla_mcdoc/data/util/SoundEventRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class SoundEventRefStruct(GeneratedModel):
    sound_id: Annotated[str, IdSpec(registry='weighed_sound_event', empty='allowed')]
    range: float | None = None  # Range in blocks. If the player is further than this range from the source of the sound, the sound will be inaudible. If omitted, the sound will have a variable range.


type SoundEventRef = Annotated[str, IdSpec(registry='sound_event')] | SoundEventRefStruct
