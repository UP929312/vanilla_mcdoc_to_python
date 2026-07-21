# Generated from symbols.json for ::java::world::block::test_block::TestBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.block.test_block.TestBlockMode import TestBlockMode


@dataclass(kw_only=True)
class TestBlock(BlockEntity):
    mode: TestBlockMode | None = None
    message: str | None = None
    powered: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::test_block::TestBlock": {
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
                "key": "mode",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::test_block::TestBlockMode"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "message",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "powered",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

