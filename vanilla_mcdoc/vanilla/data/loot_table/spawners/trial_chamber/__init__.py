"""Vanilla's data/loot_table/spawners/trial_chamber/ files"""
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
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=3,
                    name='minecraft:cooked_chicken',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:baked_potato',
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
                        LootFunctionSetPotion(id='minecraft:swiftness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:spawners/trial_chamber/consumables',
)

ITEMS_TO_DROP_WHEN_OMINOUS = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:wind_charged', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:oozing', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:weaving', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:infested', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:strength', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:swiftness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:slow_falling', type='minecraft:set_potion'),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:strong_slowness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:fire_charge',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:wind_charge',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:spawners/trial_chamber/items_to_drop_when_ominous',
)

KEY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:trial_key', type='minecraft:item')])],
    random_sequence='minecraft:spawners/trial_chamber/key',
)
