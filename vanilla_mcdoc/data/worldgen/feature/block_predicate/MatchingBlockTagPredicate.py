"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingBlockTagPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/MatchingBlockTagPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class MatchingBlockTagPredicate(PredicateOffset):
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')] | KnownBlockId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::MatchingBlockTagPredicate": {
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
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "block"
                                        }
                                    },
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}
