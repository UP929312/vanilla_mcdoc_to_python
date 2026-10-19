"""
Generated from symbols.json for ::java::util::slot::SlottedItem
Local link to file: vanilla_mcdoc/util/slot/SlottedItem.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.world.item.ItemStack import ItemStack


T = TypeVar('T', default=Any)


class SlottedItem(ItemStack, Generic[T]):
    Slot: T | None = None  # Inventory slot the item is in
