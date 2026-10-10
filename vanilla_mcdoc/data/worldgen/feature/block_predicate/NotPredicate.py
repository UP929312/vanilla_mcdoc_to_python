"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::NotPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/NotPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class NotPredicate(GeneratedModel):
    predicate: BlockPredicate
