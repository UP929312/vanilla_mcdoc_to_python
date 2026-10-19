"""Vanilla's data/loot_table/till/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount

ROOTED_DIRT = LootTable(
    type=LootContextParamSets.BLOCKINTERACT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:hanging_roots',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:till/rooted_dirt',
)
