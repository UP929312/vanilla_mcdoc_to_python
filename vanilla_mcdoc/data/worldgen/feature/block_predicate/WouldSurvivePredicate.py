"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::WouldSurvivePredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/WouldSurvivePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class WouldSurvivePredicate(PredicateOffset):
    state: BlockState
