"""
Generated from symbols.json for ::java::world::entity::item_frame::ItemFrame
Local link to file: vanilla_mcdoc/world/entity/item_frame/ItemFrame.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.DirectionByte import DirectionByte
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ItemFrame(BlockAttachedEntity):
    Facing: DirectionByte | None = None  # Direction it is facing.
    Item: ItemStack | None = None
    ItemDropChance: float | None = None  # Chance the item has to drop.
    ItemRotation: Annotated[int, Field(ge=0, le=7)] | None = None  # Rotation of the item.
    Invisible: bool | None = None  # Whether the item frame should be invisible. The item inside the frame is not effected.
    Fixed: bool | None = None  # Whether the item frame should not be able to be broken and should disallow the item to be moved.
