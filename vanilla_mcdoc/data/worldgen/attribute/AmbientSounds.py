"""
Generated from symbols.json for ::java::data::worldgen::attribute::AmbientSounds
Local link to file: vanilla_mcdoc/data/worldgen/attribute/AmbientSounds.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.biome.BiomeSoundAdditions import BiomeSoundAdditions
    from vanilla_mcdoc.data.worldgen.biome.MoodSound import MoodSound


class AmbientSounds(GeneratedModel):
    loop: SoundEventRef | None = None
    mood: MoodSound | None = None
    additions: BiomeSoundAdditions | list[BiomeSoundAdditions] | None = None
