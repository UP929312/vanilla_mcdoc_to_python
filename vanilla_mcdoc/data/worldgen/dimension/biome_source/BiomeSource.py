"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::BiomeSource
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/BiomeSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
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


class BiomeSourceMultiNoiseNether(MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Literal['minecraft:nether', 'nether'] | None = 'minecraft:nether'


class BiomeSourceMultiNoiseOverworld(MultiNoiseBase):
    type: Literal['minecraft:multi_noise', 'multi_noise'] = 'minecraft:multi_noise'
    preset: Literal['minecraft:overworld', 'overworld'] | None = 'minecraft:overworld'


type BiomeSourceMultiNoise = BiomeSourceMultiNoiseDefault | BiomeSourceMultiNoiseNether | BiomeSourceMultiNoiseOverworld


class BiomeSourceTheEnd(TheEnd):
    type: Literal['minecraft:the_end', 'the_end'] = 'minecraft:the_end'


type BiomeSource = Annotated[
    Annotated[BiomeSourceCheckerboard, Tag('minecraft:checkerboard')]
    | Annotated[BiomeSourceFixed, Tag('minecraft:fixed')]
    | Annotated[BiomeSourceMultiNoise, Tag('minecraft:multi_noise')]
    | Annotated[BiomeSourceTheEnd, Tag('minecraft:the_end')],
    Discriminator(tag_of('type')),
]
