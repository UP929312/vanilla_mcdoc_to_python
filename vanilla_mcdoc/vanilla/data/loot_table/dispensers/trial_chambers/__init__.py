"""Vanilla's data/loot_table/dispensers/trial_chambers/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

CHAMBER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=4,
                    name='minecraft:water_bucket',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:snowball',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:egg',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=6,
                    name='minecraft:fire_charge',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:slowness', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:splash_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:splash_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:weakness', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:splash_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:slowness', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:weakness', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetPotion(id='minecraft:healing', type='minecraft:set_potion'),
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:lingering_potion',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:dispensers/trial_chambers/chamber',
)

CORRIDOR = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:dispensers/trial_chambers/corridor',
)

WATER = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:water_bucket',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:dispensers/trial_chambers/water',
)
