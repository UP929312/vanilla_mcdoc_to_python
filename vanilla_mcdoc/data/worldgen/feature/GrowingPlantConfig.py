"""
Generated from symbols.json for ::java::data::worldgen::feature::GrowingPlantConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/GrowingPlantConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.WeightedList import WeightedList
    from vanilla_mcdoc.util.direction.Direction import Direction


class GrowingPlantConfig(GeneratedModel):
    direction: Direction
    allow_water: bool
    height_distribution: WeightedList[IntProvider[int] | int]
    body_provider: BlockStateProviderRef
    head_provider: BlockStateProviderRef
