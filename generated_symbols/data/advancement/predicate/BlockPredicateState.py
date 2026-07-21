# Generated from symbols.json for ::java::data::advancement::predicate::BlockPredicateState
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


type BlockPredicateState = dict[Any, MinMaxBounds[Any]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::BlockPredicateState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "parent"
                                },
                                "blocks"
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_state_keys"
                },
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "indexed",
                            "child": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            {
                                                "keyword": "parent"
                                            },
                                            "blocks"
                                        ]
                                    }
                                ],
                                "registry": "mcdoc:block_states"
                            },
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        {
                                            "keyword": "key"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

