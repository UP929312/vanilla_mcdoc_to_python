"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::WeightedBlockStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/WeightedBlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class WeightedBlockStateProvider(GeneratedModel):
    entries: NonEmptyWeightedList[BlockState]
