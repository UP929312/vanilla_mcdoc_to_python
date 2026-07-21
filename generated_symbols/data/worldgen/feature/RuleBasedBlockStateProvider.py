# Generated from symbols.json for ::java::data::worldgen::feature::RuleBasedBlockStateProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class RuleBasedBlockStateProvider:
    rules: list[Any]
    fallback: BlockStateProvider | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RuleBasedBlockStateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "fallback",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "fallback",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "if_True",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "then",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

