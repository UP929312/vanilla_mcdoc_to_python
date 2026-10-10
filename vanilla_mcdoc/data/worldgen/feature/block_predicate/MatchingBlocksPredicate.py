"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingBlocksPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/MatchingBlocksPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class MatchingBlocksPredicate(PredicateOffset):
    blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
