"""
Generated from symbols.json for ::java::data::advancement::trigger::BlockStateConditions
Local link to file: generated_symbols/data/advancement/trigger/BlockStateConditions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.registry_ref.BlockListRef import BlockListRef


type StateStructBlockStatesNone = dict[str, str]


@dataclass(kw_only=True)
class BlockStateConditions:
    blocks: BlockListRef | None = None
    state: StateStructBlockStatesNone | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::BlockStateConditions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "blocks",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::registry_ref::BlockListRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "block"
                                    ]
                                }
                            ],
                            "registry": "mcdoc:block_states",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "blocks"
                                    ]
                                }
                            ],
                            "registry": "mcdoc:block_states",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

