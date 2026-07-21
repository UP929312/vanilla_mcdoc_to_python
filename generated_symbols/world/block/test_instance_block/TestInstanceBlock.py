# Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlock
from dataclasses import dataclass
from typing import Any
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class TestInstanceBlock(BlockEntity):
    data: Any | None = None
    errors: list[Any] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::test_instance_block::TestInstanceBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "pair",
                "key": "data",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "test",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "test_instance"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "size",
                            "type": {
                                "kind": "int_array",
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 3,
                                    "max": 3
                                }
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "rotation",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::Rotation"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "ignore_entities",
                            "type": {
                                "kind": "boolean"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "status",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::block::test_instance_block::TestInstanceBlockStatus"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "error_message",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            },
                            "optional": True
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "key": "errors",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "pos",
                                "type": {
                                    "kind": "int_array",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 3,
                                        "max": 3
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "text",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::util::text::Text"
                                }
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

