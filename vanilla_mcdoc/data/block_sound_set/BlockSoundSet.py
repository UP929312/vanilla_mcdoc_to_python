"""
Generated from symbols.json for ::java::data::block_sound_set::BlockSoundSet
Local link to file: vanilla_mcdoc/data/block_sound_set/BlockSoundSet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class BlockSoundSet(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'block_sound_set'

    volume: Annotated[float, Field(ge=1e-05, le=10)] | None = None  # Defaults to 1.
    pitch: Annotated[float, Field(ge=1e-05, le=2)] | None = None  # Defauls to 1.
    break_sound: SoundEventRef | None = None
    step_sound: SoundEventRef | None = None
    place_sound: SoundEventRef | None = None
    hit_sound: SoundEventRef | None = None
    fall_sound: SoundEventRef | None = None
