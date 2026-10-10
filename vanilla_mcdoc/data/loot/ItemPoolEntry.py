"""
Generated from symbols.json for ::java::data::loot::ItemPoolEntry
Local link to file: vanilla_mcdoc/data/loot/ItemPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry
from vanilla_mcdoc.minecraft_types import IdSpec


class ItemPoolEntry(SingletonPoolEntry):
    name: Annotated[str, IdSpec(registry='item', exclude=('air',))]
