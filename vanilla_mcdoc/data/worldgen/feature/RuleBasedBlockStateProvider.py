"""
Generated from symbols.json for ::java::data::worldgen::feature::RuleBasedBlockStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/RuleBasedBlockStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class RulesStruct(GeneratedModel):
    if_true: BlockPredicate
    then: BlockStateProviderRef


class RuleBasedBlockStateProvider(GeneratedModel):
    fallback: BlockStateProviderRef | None = None
    rules: list[RulesStruct]
