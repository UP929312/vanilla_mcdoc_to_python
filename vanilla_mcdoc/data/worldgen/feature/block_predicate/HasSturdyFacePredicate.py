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
