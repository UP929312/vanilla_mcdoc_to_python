"""
Generated from symbols.json for ::java::util::block_state::BlockState
Local link to file: generated_symbols/util/block_state/BlockState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.block_state.FullBlockState import FullBlockState


type BlockState = Annotated[str, IdSpec(registry='block')] | KnownBlockId | FullBlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::block_state::BlockState": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "Name",
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
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "Properties",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "Name"
                                    ]
                                }
                            ],
                            "registry": "mcdoc:block_states"
                        },
                        "optional": True
                    }
                ],
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
                "kind": "string",
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
                    },
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
            {
                "kind": "reference",
                "path": "::java::util::block_state::FullBlockState",
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
    }
}
