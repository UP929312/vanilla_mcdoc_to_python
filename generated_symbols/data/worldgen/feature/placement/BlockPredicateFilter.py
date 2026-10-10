"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::BlockPredicateFilter
Local link to file: generated_symbols/data/worldgen/feature/placement/BlockPredicateFilter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class BlockPredicateFilter(GeneratedModel):
    predicate: BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::BlockPredicateFilter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            }
        ]
    }
}
