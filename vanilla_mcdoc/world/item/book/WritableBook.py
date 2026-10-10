"""
Generated from symbols.json for ::java::world::item::book::WritableBook
Local link to file: vanilla_mcdoc/world/item/book/WritableBook.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.item.ItemBase import ItemBase


class WritableBook(ItemBase):
    pages: list[str] | None = None
