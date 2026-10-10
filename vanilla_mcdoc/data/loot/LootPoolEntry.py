"""
Generated from symbols.json for ::java::data::loot::LootPoolEntry
Local link to file: vanilla_mcdoc/data/loot/LootPoolEntry.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

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
    LootPoolEntryAlternatives | LootPoolEntryDynamic | LootPoolEntryEmpty | LootPoolEntryGroup | LootPoolEntryItem | LootPoolEntryLootTable | LootPoolEntrySequence | LootPoolEntrySlots | LootPoolEntryTag,
    Field(discriminator='type'),
]


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
