"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeNoiseEntry
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/BiomeNoiseEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameters import ClimateParameters


class BiomeNoiseEntry(GeneratedModel):
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]
    parameters: ClimateParameters
