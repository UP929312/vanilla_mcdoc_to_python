"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoise
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/MultiNoise.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.worldgen.dimension.biome_source.DirectMultiNoise import DirectMultiNoise
from vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBase import MultiNoiseBase
from vanilla_mcdoc.minecraft_types import IdSpec


class MultiNoiseDefault(DirectMultiNoise, MultiNoiseBase):
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


class MultiNoiseUnknown(MultiNoiseBase):
    preset: Annotated[str, IdSpec(registry='worldgen/multi_noise_biome_source_parameter_list')] | None = None


type MultiNoise = MultiNoiseDefault | MultiNoiseUnknown
