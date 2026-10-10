"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockStateRuleProviderEntry
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockStateRuleProviderEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class BlockStateRuleProviderEntry(GeneratedModel):
    if_true: BlockPredicate
    then: BlockStateProviderRef
