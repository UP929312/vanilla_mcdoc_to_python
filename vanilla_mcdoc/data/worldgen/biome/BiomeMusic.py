"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeMusic
Local link to file: vanilla_mcdoc/data/worldgen/biome/BiomeMusic.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class BiomeMusic(GeneratedModel):
    sound: SoundEventRef
    min_delay: Annotated[int, Field(ge=0)]
    max_delay: Annotated[int, Field(ge=0)]
    replace_current_music: bool | None = None  # Defaults to `false`.
