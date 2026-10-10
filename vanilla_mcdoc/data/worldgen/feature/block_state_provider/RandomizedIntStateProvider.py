"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::RandomizedIntStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/RandomizedIntStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class RandomizedIntStateProvider(GeneratedModel):
    property: str
    values: IntProvider[int] | int
    source: BlockStateProviderRef
