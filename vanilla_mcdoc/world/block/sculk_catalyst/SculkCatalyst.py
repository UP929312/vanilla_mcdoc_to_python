"""
Generated from symbols.json for ::java::world::block::sculk_catalyst::SculkCatalyst
Local link to file: vanilla_mcdoc/world/block/sculk_catalyst/SculkCatalyst.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.sculk_catalyst.ChargeCursor import ChargeCursor


class SculkCatalyst(BlockEntity):
    cursors: list[ChargeCursor] | None = None
