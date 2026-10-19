"""Vanilla's data/loot_table/chests/trial_chambers/ files"""
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryItem, LootPoolEntryLootTable
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionRandomChance
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionEnchantRandomly, LootFunctionEnchantWithLevels, LootFunctionSetCount, LootFunctionSetDamage, LootFunctionSetEnchantments, LootFunctionSetOminousBottleAmplifier, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructUniform
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

CORRIDOR = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.4, max=0.9),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:iron_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:honeycomb',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=2,
                    name='minecraft:stone_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=2,
                    name='minecraft:stone_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:ender_pearl',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:bamboo_hanging_sign',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:bamboo_planks',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:scaffolding',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=20),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:tuff',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/corridor',
)

ENTRANCE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:trial_key',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:wooden_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:honeycomb',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/entrance',
)

INTERSECTION = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:diamond_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:emerald_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.1, max=0.5),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=5,
                    name='minecraft:diamond_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.1, max=0.5),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=5,
                    name='minecraft:diamond_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:cake',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=20),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:amethyst_shard',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:iron_block',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/intersection',
)

INTERSECTION_BARREL = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.4, max=0.9),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantRandomly(
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_randomly',
                        ),
                    ],
                    name='minecraft:diamond_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    name='minecraft:diamond_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    name='minecraft:compass',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:bucket',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=4,
                    name='minecraft:golden_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=4,
                    name='minecraft:golden_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bamboo_planks',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:baked_potato',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/intersection_barrel',
)

REWARD = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    weight=8,
                    value='minecraft:chests/trial_chambers/reward_rare',
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    weight=2,
                    value='minecraft:chests/trial_chambers/reward_common',
                    type='minecraft:loot_table',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryLootTable(
                    value='minecraft:chests/trial_chambers/reward_common',
                    type='minecraft:loot_table',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    value='minecraft:chests/trial_chambers/reward_unique',
                    type='minecraft:loot_table',
                ),
            ],
            condition=LootConditionRandomChance(chance=0.25, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward',
)

REWARD_COMMON = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                    ],
                    weight=4,
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:wind_charge',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:honey_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetOminousBottleAmplifier(
                            amplifier=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_ominous_bottle_amplifier',
                        ),
                    ],
                    weight=2,
                    name='minecraft:ominous_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=12),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:wind_charge',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_common',
)

REWARD_OMINOUS = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    weight=8,
                    value='minecraft:chests/trial_chambers/reward_ominous_rare',
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    weight=2,
                    value='minecraft:chests/trial_chambers/reward_ominous_common',
                    type='minecraft:loot_table',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryLootTable(
                    value='minecraft:chests/trial_chambers/reward_ominous_common',
                    type='minecraft:loot_table',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    value='minecraft:chests/trial_chambers/reward_ominous_unique',
                    type='minecraft:loot_table',
                ),
            ],
            condition=LootConditionRandomChance(chance=0.75, type='minecraft:random_chance'),
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_ominous',
)

REWARD_OMINOUS_COMMON = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:wind_charge',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=12),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:strong_slowness', type='minecraft:set_potion'),
                    ],
                    weight=3,
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetOminousBottleAmplifier(
                            amplifier=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                            type='minecraft:set_ominous_bottle_amplifier',
                        ),
                    ],
                    name='minecraft:ominous_bottle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_ominous_common',
)

REWARD_OMINOUS_RARE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=5, name='minecraft:emerald_block', type='minecraft:item'),
                LootPoolEntryItem(weight=4, name='minecraft:iron_block', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=20),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=4,
                    name='minecraft:crossbow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=3, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=20),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=20),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:diamond_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(
                        options=[
                            'minecraft:knockback',
                            'minecraft:punch',
                            'minecraft:smite',
                            'minecraft:looting',
                            'minecraft:multishot',
                        ],
                        type='minecraft:enchant_randomly',
                    ),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(
                        options=['minecraft:breach', 'minecraft:density'],
                        type='minecraft:enchant_randomly',
                    ),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetEnchantments(
                        enchantments={'minecraft:wind_burst': 1},
                        type='minecraft:set_enchantments',
                    ),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:diamond_block', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_ominous_rare',
)

REWARD_OMINOUS_UNIQUE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=3, name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=3, name='minecraft:flow_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:flow_banner_pattern', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:music_disc_creator', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:heavy_core', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_ominous_unique',
)

REWARD_RARE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetDamage(
                        damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.5, max=1.0),
                        type='minecraft:set_damage',
                    ),
                    weight=3,
                    name='minecraft:shield',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=15),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:bow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=20),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=2,
                    name='minecraft:crossbow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=10),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=2,
                    name='minecraft:iron_axe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=10),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=2,
                    name='minecraft:iron_chestplate',
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
                    modifier=LootFunctionEnchantRandomly(
                        options=[
                            'minecraft:sharpness',
                            'minecraft:bane_of_arthropods',
                            'minecraft:efficiency',
                            'minecraft:fortune',
                            'minecraft:silk_touch',
                            'minecraft:feather_falling',
                        ],
                        type='minecraft:enchant_randomly',
                    ),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(
                        options=[
                            'minecraft:riptide',
                            'minecraft:loyalty',
                            'minecraft:channeling',
                            'minecraft:impaling',
                            'minecraft:mending',
                        ],
                        type='minecraft:enchant_randomly',
                    ),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=15),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:diamond_chestplate',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=15),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:diamond_axe',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_rare',
)

REWARD_UNIQUE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=4, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=3, name='minecraft:bolt_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:guster_banner_pattern', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_precipice', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:trident', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/reward_unique',
)

SUPPLY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=14),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:poison', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:slowness', type='minecraft:set_potion'),
                    ],
                    name='minecraft:tipped_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:baked_potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:glow_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:acacia_planks',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:moss_block',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:bone_meal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=10),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:tuff',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=2, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:regeneration', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=2, type='minecraft:set_count'),
                        LootFunctionSetPotion(id='minecraft:strength', type='minecraft:set_potion'),
                    ],
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.15, max=0.8),
                            type='minecraft:set_damage',
                        ),
                    ],
                    weight=2,
                    name='minecraft:stone_pickaxe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    name='minecraft:milk_bucket',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/trial_chambers/supply',
)
