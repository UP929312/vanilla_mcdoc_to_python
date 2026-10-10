"""
Generated from symbols.json for ::java::data::loot::LootTablePoolEntry
Local link to file: vanilla_mcdoc/data/loot/LootTablePoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootTableListRef import LootTableListRef


class LootTablePoolEntry(SingletonPoolEntry):
    value: LootTableListRef
    expand: bool | None = None  # If `true`, each of the loot tables becomes an independent entry in the pool with the same `weight` and `quality`.  If `false`, drops all loot tables.  Defaults to `false`.
