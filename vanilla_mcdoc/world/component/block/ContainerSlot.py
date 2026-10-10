"""
Generated from symbols.json for ::java::world::component::block::ContainerSlot
Local link to file: vanilla_mcdoc/world/component/block/ContainerSlot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class ContainerSlot(GeneratedModel):
    slot: Annotated[int, Field(ge=0, le=255)]  # The slot ID of the container.
    item: ItemStackTemplate  # The item stack in this container slot.
