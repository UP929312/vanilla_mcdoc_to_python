"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::ChunkGenerator
Local link to file: vanilla_mcdoc/data/worldgen/dimension/chunk_generator/ChunkGenerator.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Flat import Flat
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Noise import Noise


class ChunkGeneratorFlat(Flat):
    type: Literal['minecraft:flat', 'flat'] = 'minecraft:flat'


class ChunkGeneratorNoise(Noise):
    type: Literal['minecraft:noise', 'noise'] = 'minecraft:noise'


class ChunkGeneratorDebug(GeneratedModel):
    type: Literal['minecraft:debug', 'debug'] = 'minecraft:debug'


type ChunkGenerator = Annotated[
    Annotated[ChunkGeneratorFlat, Tag('minecraft:flat')]
    | Annotated[ChunkGeneratorNoise, Tag('minecraft:noise')]
    | Annotated[ChunkGeneratorDebug, Tag('minecraft:debug')],
    Discriminator(tag_of('type')),
]
