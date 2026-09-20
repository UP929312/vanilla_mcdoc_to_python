"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::CombiningPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/CombiningPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class CombiningPredicate(GeneratedModel):
    predicates: list[BlockPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::CombiningPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicates",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                    }
                }
            }
        ]
    }
}

