"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::MatchingFluidsPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/MatchingFluidsPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class MatchingFluidsPredicate(PredicateOffset):
    fluids: list[Annotated[str, IdSpec(registry='fluid')]] | Annotated[str, IdSpec(registry='fluid', tags='allowed')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::MatchingFluidsPredicate": {
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
                "key": "fluids",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "fluid"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "fluid"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

