"""
Generated from symbols.json for ::java::world::block::chiseled_bookshelf::ChiseledBookshelf
Local link to file: vanilla_mcdoc/world/block/chiseled_bookshelf/ChiseledBookshelf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class ChiseledBookshelf(BlockEntity):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=5)]]], Field(min_length=0, max_length=6)] | None = None  # Slots from 0 to 5.
    last_interacted_slot: Annotated[int, Field(ge=0, le=5)] | None = None
