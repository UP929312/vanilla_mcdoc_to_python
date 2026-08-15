"""
Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlock
Local link to file: generated_symbols/world/block/test_instance_block/TestInstanceBlock.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.world.block.BlockEntity import BlockEntity
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownTestInstanceId import KnownTestInstanceId
    from generated_symbols.util.Rotation import Rotation
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.block.test_instance_block.TestInstanceBlockStatus import TestInstanceBlockStatus


@dataclass(kw_only=True)
class DataStruct:
    size: tuple[int, int, int]
    rotation: Rotation
    ignore_entities: bool
    status: TestInstanceBlockStatus
    test: Annotated[str, IdSpec(registry='test_instance')] | KnownTestInstanceId | None = None
    error_message: Text | None = None


@dataclass(kw_only=True)
class ErrorsStruct:
    pos: tuple[int, int, int]
    text: Text


@dataclass(kw_only=True)
class TestInstanceBlock(BlockEntity):
    data: DataStruct | None = None
    errors: list[ErrorsStruct] | None = None


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

