"""
Generated from symbols.json for ::java::data::loot::LootPoolEntry
Local link to file: generated_symbols/data/loot/LootPoolEntry.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.LootPoolEntryBase import LootPoolEntryBase
from generated_symbols.data.loot.SingletonPoolEntry import SingletonPoolEntry
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.loot.DynamicDrops import DynamicDrops
    from generated_symbols.data.loot.LootTableListRef import LootTableListRef
    from generated_symbols.data.slot_source.SlotSource import SlotSource
    from generated_symbols.util.registry_ref.ItemListRef import ItemListRef


@dataclass(kw_only=True)
class LootPoolEntryAlternatives(LootPoolEntryBase):
    type: Literal['minecraft:alternatives']
    children: Annotated[list[LootPoolEntry], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class LootPoolEntryDynamic(SingletonPoolEntry):
    type: Literal['minecraft:dynamic']
    name: DynamicDrops


@dataclass(kw_only=True)
class LootPoolEntryEmpty(LootPoolEntryBase):
    type: Literal['minecraft:empty']
    weight: Annotated[int, 'Range | `1` and above | inclusive'] | None = None
    quality: int | None = None


@dataclass(kw_only=True)
class LootPoolEntryGroup(LootPoolEntryBase):
    type: Literal['minecraft:group']
    children: Annotated[list[LootPoolEntry], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class LootPoolEntryItem(SingletonPoolEntry):
    type: Literal['minecraft:item']
    name: Annotated[str, IdSpec(registry='item', exclude=('air',))]


@dataclass(kw_only=True)
class LootPoolEntryLootTable(SingletonPoolEntry):
    type: Literal['minecraft:loot_table']
    value: LootTableListRef
    expand: bool | None = None  # If `true`, randomly selects a loot table to drop.  If `false`, drops all loot tables.  Defaults to `false`.


@dataclass(kw_only=True)
class LootPoolEntrySequence(LootPoolEntryBase):
    type: Literal['minecraft:sequence']
    children: Annotated[list[LootPoolEntry], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class LootPoolEntrySlots(SingletonPoolEntry):
    type: Literal['minecraft:slots']
    slot_source: SlotSource


@dataclass(kw_only=True)
class LootPoolEntryTag(SingletonPoolEntry):
    type: Literal['minecraft:tag']
    items: ItemListRef
    expand: bool | None = None  # If `true`, randomly selects an item to drop.  If `false`, drops all items.  Defaults to `false`.


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

