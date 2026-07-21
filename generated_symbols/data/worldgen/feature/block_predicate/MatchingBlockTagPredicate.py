# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingBlockTagPredicate
from dataclasses import dataclass
from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset


@dataclass(kw_only=True)
class MatchingBlockTagPredicate(PredicateOffset):
    tag: str


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

