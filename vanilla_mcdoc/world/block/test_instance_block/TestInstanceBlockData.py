"""
Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlockData
Local link to file: vanilla_mcdoc/world/block/test_instance_block/TestInstanceBlockData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownTestInstanceId import KnownTestInstanceId
    from vanilla_mcdoc.util.Rotation import Rotation
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlockStatus import TestInstanceBlockStatus


class TestInstanceBlockData(GeneratedModel):
    test: Annotated[str, IdSpec(registry='test_instance')] | KnownTestInstanceId | None = None
    size: tuple[int, int, int]
    rotation: Rotation
    ignore_entities: bool
    status: TestInstanceBlockStatus
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
