# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::HasSturdyFacePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset

if TYPE_CHECKING:
    from generated_symbols.util.direction.Direction import Direction


@dataclass(kw_only=True)
class HasSturdyFacePredicate(PredicateOffset):
    direction: Direction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::HasSturdyFacePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::PredicateOffset"
                }
            },
            {
                "kind": "pair",
                "key": "direction",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::Direction"
                }
            }
        ]
    }
}

