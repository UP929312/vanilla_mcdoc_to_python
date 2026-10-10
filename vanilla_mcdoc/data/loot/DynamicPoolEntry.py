"""
Generated from symbols.json for ::java::data::loot::DynamicPoolEntry
Local link to file: vanilla_mcdoc/data/loot/DynamicPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.DynamicDrops import DynamicDrops


class DynamicPoolEntry(SingletonPoolEntry):
    name: DynamicDrops
