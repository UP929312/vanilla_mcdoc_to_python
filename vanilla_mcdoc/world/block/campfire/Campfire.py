"""
Generated from symbols.json for ::java::world::block::campfire::Campfire
Local link to file: vanilla_mcdoc/world/block/campfire/Campfire.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class Campfire(BlockEntity):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=3)]]], Field(min_length=0, max_length=4)] | None = None
    CookingTimes: tuple[int, int, int, int] | None = None  # Ticks each item has been cooking. Index is according to item slot.
    CookingTotalTimes: tuple[int, int, int, int] | None = None  # Ticks each item still has to cook. Index is according to item slot.
