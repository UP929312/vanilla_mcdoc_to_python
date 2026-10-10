"""
Generated from symbols.json for ::java::world::block::lectern::Lectern
Local link to file: vanilla_mcdoc/world/block/lectern/Lectern.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Lectern(BlockEntity):
    Book: ItemStack | None = None
    Page: int | None = None  # Current page the book is on.
