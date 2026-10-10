"""
Generated from symbols.json for ::java::data::worldgen::biome::BiomeSoundAdditions
Local link to file: vanilla_mcdoc/data/worldgen/biome/BiomeSoundAdditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class BiomeSoundAdditions(GeneratedModel):
    sound: SoundEventRef
    tick_chance: Annotated[float, Field(ge=0, le=1)]
