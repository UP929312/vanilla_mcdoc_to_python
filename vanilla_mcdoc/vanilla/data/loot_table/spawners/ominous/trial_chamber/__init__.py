"""Vanilla's data/loot_table/spawners/ominous/trial_chamber/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

CONSUMABLES = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:cooked_beef',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:baked_potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:golden_carrot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:regeneration', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:strength', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:spawners/ominous/trial_chamber/consumables',
)

KEY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:ominous_trial_key', type='minecraft:item')])],
    random_sequence='minecraft:spawners/ominous/trial_chamber/key',
)
