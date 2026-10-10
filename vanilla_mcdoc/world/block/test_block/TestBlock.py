"""
Generated from symbols.json for ::java::world::block::test_block::TestBlock
Local link to file: vanilla_mcdoc/world/block/test_block/TestBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.test_block.TestBlockMode import TestBlockMode


class TestBlock(BlockEntity):
    mode: TestBlockMode | None = None
    message: str | None = None
    powered: bool | None = None
