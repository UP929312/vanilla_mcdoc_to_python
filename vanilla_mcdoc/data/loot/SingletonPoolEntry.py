"""
Generated from symbols.json for ::java::data::loot::SingletonPoolEntry
Local link to file: vanilla_mcdoc/data/loot/SingletonPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.LootPoolEntryBase import LootPoolEntryBase


class SingletonPoolEntry(LootPoolEntryBase):
    weight: Annotated[int, Field(ge=1)] | None = None
    quality: int | None = None
