"""Vanilla's data/loot_table/shearing/mooshroom/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable

BROWN = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[LootPool(rolls=5, entries=[LootPoolEntryItem(name='minecraft:brown_mushroom', type='minecraft:item')])],
    random_sequence='minecraft:shearing/mooshroom/brown',
)

RED = LootTable(
    type=LootContextParamSets.SHEARING,
    pools=[LootPool(rolls=5, entries=[LootPoolEntryItem(name='minecraft:red_mushroom', type='minecraft:item')])],
    random_sequence='minecraft:shearing/mooshroom/red',
)
