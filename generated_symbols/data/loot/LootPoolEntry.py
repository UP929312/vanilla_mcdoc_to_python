"""
Generated from symbols.json for ::java::data::loot::LootPoolEntry
Local link to file: generated_symbols/data/loot/LootPoolEntry.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.loot.CompositePoolEntry import CompositePoolEntry
from generated_symbols.data.loot.DynamicPoolEntry import DynamicPoolEntry
from generated_symbols.data.loot.ItemPoolEntry import ItemPoolEntry
from generated_symbols.data.loot.LootTablePoolEntry import LootTablePoolEntry
from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry
from generated_symbols.data.loot.SlotsPoolEntry import SlotsPoolEntry
from generated_symbols.data.loot.TagPoolEntry import TagPoolEntry


@dataclass(kw_only=True)
class LootPoolEntryAlternatives(CompositePoolEntry):
    type: Literal['minecraft:alternatives'] = 'minecraft:alternatives'


@dataclass(kw_only=True)
class LootPoolEntryDynamic(DynamicPoolEntry):
    type: Literal['minecraft:dynamic'] = 'minecraft:dynamic'


@dataclass(kw_only=True)
class LootPoolEntryEmpty(SingletonPoolEntry):
    type: Literal['minecraft:empty'] = 'minecraft:empty'


@dataclass(kw_only=True)
class LootPoolEntryGroup(CompositePoolEntry):
    type: Literal['minecraft:group'] = 'minecraft:group'


@dataclass(kw_only=True)
class LootPoolEntryItem(ItemPoolEntry):
    type: Literal['minecraft:item'] = 'minecraft:item'


@dataclass(kw_only=True)
class LootPoolEntryLootTable(LootTablePoolEntry):
    type: Literal['minecraft:loot_table'] = 'minecraft:loot_table'


@dataclass(kw_only=True)
class LootPoolEntrySequence(CompositePoolEntry):
    type: Literal['minecraft:sequence'] = 'minecraft:sequence'


@dataclass(kw_only=True)
class LootPoolEntrySlots(SlotsPoolEntry):
    type: Literal['minecraft:slots'] = 'minecraft:slots'


@dataclass(kw_only=True)
class LootPoolEntryTag(TagPoolEntry):
    type: Literal['minecraft:tag'] = 'minecraft:tag'


type LootPoolEntry = LootPoolEntryAlternatives | LootPoolEntryDynamic | LootPoolEntryEmpty | LootPoolEntryGroup | LootPoolEntryItem | LootPoolEntryLootTable | LootPoolEntrySequence | LootPoolEntrySlots | LootPoolEntryTag


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootPoolEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::LootEntryType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_pool_entry_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:loot_pool_entry"
                }
            }
        ]
    }
}

