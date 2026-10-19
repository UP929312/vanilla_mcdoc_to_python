"""Vanilla's data/loot_table/harvest/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionMatchBlock
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

BEEHIVE = LootTable(
    type=LootContextParamSets.BLOCKINTERACT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=3, type='minecraft:set_count'),
                    name='minecraft:honeycomb',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:harvest/beehive',
)

CAVE_VINE = LootTable(
    type=LootContextParamSets.BLOCKINTERACT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:glow_berries', type='minecraft:item')])],
    random_sequence='minecraft:harvest/cave_vine',
)

SWEET_BERRY_BUSH = LootTable(
    type=LootContextParamSets.BLOCKINTERACT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:sweet_berry_bush',
                        state={'age': '3'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:sweet_berries',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:sweet_berries',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:harvest/sweet_berry_bush',
)
