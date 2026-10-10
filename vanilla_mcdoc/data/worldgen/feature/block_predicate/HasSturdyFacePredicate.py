"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::HasSturdyFacePredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/HasSturdyFacePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Direction import Direction


class HasSturdyFacePredicate(PredicateOffset):
    direction: Direction
