"""
Generated from symbols.json for ::java::data::worldgen::attribute::BackgroundMusic
Local link to file: vanilla_mcdoc/data/worldgen/attribute/BackgroundMusic.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.biome.BiomeMusic import BiomeMusic


class BackgroundMusic(GeneratedModel):
    default: BiomeMusic | None = None  # Default music to play
    underwater: BiomeMusic | None = None  # Overrides default music when underwater
    creative: BiomeMusic | None = None  # Overrides default music when in creative mode
