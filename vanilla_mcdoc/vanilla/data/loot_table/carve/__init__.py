"""Vanilla's data/loot_table/carve/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount

PUMPKIN = LootTable(
    type=LootContextParamSets.BLOCKINTERACT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=4, type='minecraft:set_count'),
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:carve/pumpkin',
)
