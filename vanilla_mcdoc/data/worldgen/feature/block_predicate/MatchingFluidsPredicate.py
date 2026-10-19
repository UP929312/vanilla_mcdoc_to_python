"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingFluidsPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/MatchingFluidsPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.FluidPredicateState import FluidPredicateState


class MatchingFluidsPredicate(PredicateOffset):
    fluids: list[Annotated[str, IdSpec(registry='fluid')]] | Annotated[str, IdSpec(registry='fluid', tags='allowed')]
    state: FluidPredicateState | None = None
