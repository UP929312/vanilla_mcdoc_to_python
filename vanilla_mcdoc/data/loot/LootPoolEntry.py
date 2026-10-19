"""
Generated from symbols.json for ::java::data::loot::LootPoolEntry
Local link to file: vanilla_mcdoc/data/loot/LootPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.loot.CompositePoolEntry import CompositePoolEntry
from vanilla_mcdoc.data.loot.DynamicPoolEntry import DynamicPoolEntry
from vanilla_mcdoc.data.loot.ItemPoolEntry import ItemPoolEntry
from vanilla_mcdoc.data.loot.LootTablePoolEntry import LootTablePoolEntry
from vanilla_mcdoc.data.loot.SingletonPoolEntry import SingletonPoolEntry
from vanilla_mcdoc.data.loot.SlotsPoolEntry import SlotsPoolEntry
from vanilla_mcdoc.data.loot.TagPoolEntry import TagPoolEntry


class LootPoolEntryAlternatives(CompositePoolEntry):
    type: Literal['minecraft:alternatives', 'alternatives'] = 'minecraft:alternatives'


class LootPoolEntryDynamic(DynamicPoolEntry):
    type: Literal['minecraft:dynamic', 'dynamic'] = 'minecraft:dynamic'


class LootPoolEntryEmpty(SingletonPoolEntry):
    type: Literal['minecraft:empty', 'empty'] = 'minecraft:empty'


class LootPoolEntryGroup(CompositePoolEntry):
    type: Literal['minecraft:group', 'group'] = 'minecraft:group'


class LootPoolEntryItem(ItemPoolEntry):
    type: Literal['minecraft:item', 'item'] = 'minecraft:item'


class LootPoolEntryLootTable(LootTablePoolEntry):
    type: Literal['minecraft:loot_table', 'loot_table'] = 'minecraft:loot_table'


class LootPoolEntrySequence(CompositePoolEntry):
    type: Literal['minecraft:sequence', 'sequence'] = 'minecraft:sequence'


class LootPoolEntrySlots(SlotsPoolEntry):
    type: Literal['minecraft:slots', 'slots'] = 'minecraft:slots'


class LootPoolEntryTag(TagPoolEntry):
    type: Literal['minecraft:tag', 'tag'] = 'minecraft:tag'


type LootPoolEntry = Annotated[
    Annotated[LootPoolEntryAlternatives, Tag('minecraft:alternatives')]
    | Annotated[LootPoolEntryDynamic, Tag('minecraft:dynamic')]
    | Annotated[LootPoolEntryEmpty, Tag('minecraft:empty')]
    | Annotated[LootPoolEntryGroup, Tag('minecraft:group')]
    | Annotated[LootPoolEntryItem, Tag('minecraft:item')]
    | Annotated[LootPoolEntryLootTable, Tag('minecraft:loot_table')]
    | Annotated[LootPoolEntrySequence, Tag('minecraft:sequence')]
    | Annotated[LootPoolEntrySlots, Tag('minecraft:slots')]
    | Annotated[LootPoolEntryTag, Tag('minecraft:tag')],
    Discriminator(tag_of('type')),
]
