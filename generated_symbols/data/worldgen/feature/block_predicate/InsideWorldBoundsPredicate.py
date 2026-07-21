# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::InsideWorldBoundsPredicate
from dataclasses import dataclass
from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset


@dataclass(kw_only=True)
class InsideWorldBoundsPredicate(PredicateOffset):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::InsideWorldBoundsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::PredicateOffset"
                }
            }
        ]
    }
}

