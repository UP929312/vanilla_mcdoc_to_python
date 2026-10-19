"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockPlacer.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.feature.ColumnPlacer import ColumnPlacer


class BlockPlacerColumnPlacer(ColumnPlacer):
    type: Literal['minecraft:column_placer', 'column_placer'] = 'minecraft:column_placer'


class BlockPlacerDoublePlantPlacer(GeneratedModel):
    type: Literal['minecraft:double_plant_placer', 'double_plant_placer'] = 'minecraft:double_plant_placer'


class BlockPlacerSimpleBlockPlacer(GeneratedModel):
    type: Literal['minecraft:simple_block_placer', 'simple_block_placer'] = 'minecraft:simple_block_placer'


type BlockPlacer = Annotated[
    Annotated[BlockPlacerColumnPlacer, Tag('minecraft:column_placer')]
    | Annotated[BlockPlacerDoublePlantPlacer, Tag('minecraft:double_plant_placer')]
    | Annotated[BlockPlacerSimpleBlockPlacer, Tag('minecraft:simple_block_placer')],
    Discriminator(tag_of('type')),
]
