"""
Generated from symbols.json for ::java::data::loot::TagPoolEntry
Local link to file: vanilla_mcdoc/data/loot/TagPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from vanilla_mcdoc.util.registry_ref.ItemListRef import ItemListRef


class TagPoolEntry(SingletonPoolEntry):
    items: ItemListRef
    expand: bool | None = None  # If `true`, each of the items becomes an independent entry in the pool with the same `weight` and `quality`.  If `false`, drops all items in the tag.  Defaults to `false`.
