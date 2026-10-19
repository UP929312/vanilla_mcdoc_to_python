"""Vanilla's data/loot_table/pots/trial_chambers/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

CORRIDOR = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=125,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=100,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=100,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:trial_key',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:music_disc_creator_music_box', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=5,
                    name='minecraft:emerald_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:diamond_block',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:pots/trial_chambers/corridor',
)
