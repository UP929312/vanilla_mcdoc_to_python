# Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlockData
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.Rotation import Rotation
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.block.test_instance_block.TestInstanceBlockStatus import TestInstanceBlockStatus


@dataclass(kw_only=True)
class TestInstanceBlockData:
    size: tuple[int, int, int]
    rotation: Rotation
    ignore_entities: bool
    status: TestInstanceBlockStatus
    test: str | None = None
    error_message: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::test_instance_block::TestInstanceBlockData": {
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
    }
}

