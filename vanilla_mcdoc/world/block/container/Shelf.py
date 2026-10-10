"""
Generated from symbols.json for ::java::world::block::container::Shelf
Local link to file: vanilla_mcdoc/world/block/container/Shelf.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class Shelf(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=2)]]], Field(min_length=0, max_length=3)] | None = None  # Slots from 0 to 2.
    align_items_to_bottom: bool | None = None  # Defaults to `false`.
