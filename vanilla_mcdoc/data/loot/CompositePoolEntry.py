"""
Generated from symbols.json for ::java::data::loot::CompositePoolEntry
Local link to file: vanilla_mcdoc/data/loot/CompositePoolEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.LootPoolEntryBase import LootPoolEntryBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntry


class CompositePoolEntry(LootPoolEntryBase):
    children: Annotated[list[LootPoolEntry], Field(min_length=1)]
