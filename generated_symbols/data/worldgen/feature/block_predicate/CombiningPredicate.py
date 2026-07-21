# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::CombiningPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


@dataclass(kw_only=True)
class CombiningPredicate:
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

