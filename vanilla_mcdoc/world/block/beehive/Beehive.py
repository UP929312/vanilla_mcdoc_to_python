"""
Generated from symbols.json for ::java::world::block::beehive::Beehive
Local link to file: vanilla_mcdoc/world/block/beehive/Beehive.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.beehive.Bee import Bee


class Beehive(BlockEntity):
    flower_pos: tuple[int, int, int] | None = None
    bees: list[Bee] | None = None
