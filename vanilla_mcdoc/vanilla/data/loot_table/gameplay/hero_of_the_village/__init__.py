"""Vanilla's data/loot_table/gameplay/hero_of_the_village/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionSetCount, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

ARMORER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:chainmail_helmet', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:chainmail_chestplate', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:chainmail_leggings', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:chainmail_boots', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/armorer_gift',
)

BABY_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:poppy', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/hero_of_the_village/baby_gift',
)

BUTCHER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:cooked_rabbit', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cooked_chicken', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cooked_porkchop', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cooked_beef', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cooked_mutton', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/butcher_gift',
)

CARTOGRAPHER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:map', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:paper', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/cartographer_gift',
)

CLERIC_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:redstone', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:lapis_lazuli', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/cleric_gift',
)

FARMER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:bread', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:pumpkin_pie', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cookie', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/farmer_gift',
)

FISHERMAN_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:cod', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:salmon', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/fisherman_gift',
)

FLETCHER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=26, name='minecraft:arrow', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:swiftness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:slowness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:strength', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:healing', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:harming', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:leaping', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:regeneration', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:fire_resistance', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:water_breathing', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:invisibility', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:night_vision', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:weakness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/fletcher_gift',
)

LEATHERWORKER_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:leather', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/hero_of_the_village/leatherworker_gift',
)

LIBRARIAN_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:book', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/hero_of_the_village/librarian_gift',
)

MASON_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:clay', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/hero_of_the_village/mason_gift',
)

SHEPHERD_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:white_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:orange_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:magenta_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:light_blue_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:yellow_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:lime_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:pink_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:gray_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:light_gray_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:cyan_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:purple_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:blue_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:brown_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:green_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:red_wool', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:black_wool', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/shepherd_gift',
)

TOOLSMITH_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:stone_pickaxe', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:stone_axe', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:stone_hoe', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:stone_shovel', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/toolsmith_gift',
)

UNEMPLOYED_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:wheat_seeds', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/hero_of_the_village/unemployed_gift',
)

WEAPONSMITH_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:stone_axe', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_axe', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_axe', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/hero_of_the_village/weaponsmith_gift',
)
