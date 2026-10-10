"""
Generated from symbols.json for ::java::world::block::container::Container27
Local link to file: vanilla_mcdoc/world/block/container/Container27.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.block.container.ContainerBase import ContainerBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.SlottedItem import SlottedItem


class Container27(ContainerBase):
    Items: Annotated[list[SlottedItem[Annotated[int, Field(ge=0, le=26)]]], Field(min_length=0, max_length=27)] | None = None  # Slots from 0 to 26.
