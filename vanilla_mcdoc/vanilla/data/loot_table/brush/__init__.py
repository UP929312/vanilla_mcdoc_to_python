"""Vanilla's data/loot_table/brush/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable

ARMADILLO = LootTable(
    type=LootContextParamSets.ENTITYINTERACT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:armadillo_scute', type='minecraft:item')])],
    random_sequence='minecraft:brush/armadillo',
)
