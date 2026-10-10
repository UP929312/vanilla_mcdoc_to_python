"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeSource
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/BiomeSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.data.worldgen.dimension.biome_source.Checkerboard import Checkerboard
from vanilla_mcdoc.data.worldgen.dimension.biome_source.DirectMultiNoise import DirectMultiNoise
from vanilla_mcdoc.data.worldgen.dimension.biome_source.Fixed import Fixed
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
from vanilla_mcdoc.data.worldgen.dimension.biome_source.TheEnd import TheEnd
from vanilla_mcdoc.minecraft_types import IdSpec


class BiomeSourceCheckerboard(Checkerboard):
    type: Literal['minecraft:checkerboard', 'checkerboard'] = 'minecraft:checkerboard'


class BiomeSourceFixed(Fixed):
    type: Literal['minecraft:fixed', 'fixed'] = 'minecraft:fixed'


class BiomeSourceMultiNoiseDefault(DirectMultiNoise, MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


class BiomeSourceMultiNoiseUnknown(MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


type BiomeSourceMultiNoise = BiomeSourceMultiNoiseDefault | BiomeSourceMultiNoiseUnknown


class BiomeSourceTheEnd(TheEnd):
    type: Literal['minecraft:the_end', 'the_end'] = 'minecraft:the_end'


type BiomeSource = BiomeSourceCheckerboard | BiomeSourceFixed | BiomeSourceMultiNoise | BiomeSourceTheEnd
