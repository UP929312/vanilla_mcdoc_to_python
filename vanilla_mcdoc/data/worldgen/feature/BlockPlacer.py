"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockPlacer.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.feature.ColumnPlacer import ColumnPlacer


class BlockPlacerColumnPlacer(ColumnPlacer):
    type: Literal['minecraft:column_placer', 'column_placer'] = 'minecraft:column_placer'


class BlockPlacerDoublePlantPlacer(GeneratedModel):
    type: Literal['minecraft:double_plant_placer', 'double_plant_placer'] = 'minecraft:double_plant_placer'


class BlockPlacerSimpleBlockPlacer(GeneratedModel):
    type: Literal['minecraft:simple_block_placer', 'simple_block_placer'] = 'minecraft:simple_block_placer'


type BlockPlacer = Annotated[
    BlockPlacerColumnPlacer | BlockPlacerDoublePlantPlacer | BlockPlacerSimpleBlockPlacer,
    Field(discriminator='type'),
]
