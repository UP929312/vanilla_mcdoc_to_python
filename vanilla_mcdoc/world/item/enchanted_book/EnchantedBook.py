"""
Generated from symbols.json for ::java::world::item::enchanted_book::EnchantedBook
Local link to file: vanilla_mcdoc/world/item/enchanted_book/EnchantedBook.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.Enchantment import Enchantment


class EnchantedBook(ItemBase):
    StoredEnchantments: list[Enchantment] | None = None
