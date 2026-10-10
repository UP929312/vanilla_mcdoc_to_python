"""
Generated from symbols.json for ::java::world::item::book::WrittenBook
Local link to file: vanilla_mcdoc/world/item/book/WrittenBook.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Filterable import Filterable
    from vanilla_mcdoc.world.component.item.BookGeneration import BookGeneration


class WrittenBook(ItemBase):
    resolved: bool | None = None  # Whether the dynamic content on the pages has been resolved.
    pages: list[Filterable[str]] | None = None  # Pages of the book as JSON text components.
    generation: BookGeneration | None = None  # Generation of the book. 0 = original, 1 = copy of original, 2 = copy of copy, 3 = tattered.
    author: str | None = None
    title: Filterable[str] | None = None
