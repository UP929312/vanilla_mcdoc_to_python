"""
Generated from symbols.json for ::java::world::entity::item::Item
Local link to file: vanilla_mcdoc/world/entity/item/Item.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Item(EntityBase):
    Age: int | None = None  # Ticks it has existed.
    Health: int | None = None
    PickupDelay: int | None = None  # Ticks until an entity can pick up this item.
    Owner: MinecraftUUID | None = None  # Only this entity can pick up the item.
    Thrower: MinecraftUUID | None = None  # Player who threw the item. Can be set and/or changed to any entity.
    Item: ItemStack | None = None
