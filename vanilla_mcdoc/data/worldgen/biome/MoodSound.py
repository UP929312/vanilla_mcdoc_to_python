"""
Generated from symbols.json for ::java::data::worldgen::biome::MoodSound
Local link to file: vanilla_mcdoc/data/worldgen/biome/MoodSound.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class MoodSound(GeneratedModel):
    sound: SoundEventRef
    tick_delay: int
    block_search_extent: int
    offset: float
