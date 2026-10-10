"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::BlockPredicateFilter
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/BlockPredicateFilter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class BlockPredicateFilter(GeneratedModel):
    predicate: BlockPredicate
