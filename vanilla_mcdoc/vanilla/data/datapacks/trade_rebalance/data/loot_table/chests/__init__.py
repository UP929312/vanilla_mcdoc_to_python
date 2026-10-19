"""Vanilla's data/datapacks/trade_rebalance/data/loot_table/chests/ files"""
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryEmpty, LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionLocationCheck
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionEnchantRandomly, LootFunctionEnchantWithLevels, LootFunctionSetCount, LootFunctionSetDamage, LootFunctionSetInstrument, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProviderStructUniform
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform

ABANDONED_MINESHAFT = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=20, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=30, name='minecraft:name_tag', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=5, name='minecraft:iron_pickaxe', type='minecraft:item'),
                LootPoolEntryEmpty(weight=5, type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:redstone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:lapis_lazuli',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bread',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:glow_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=3,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:powered_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:detector_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:activator_rail',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=16),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    condition=LootConditionLocationCheck(
                        predicate=LocationPredicate(biomes='minecraft:sulfur_caves'),
                        type='minecraft:location_check',
                    ),
                    weight=10,
                    name='minecraft:music_disc_bounce',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=4, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:efficiency', type='minecraft:enchant_randomly'),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/abandoned_mineshaft',
)

ANCIENT_CITY = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=10),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:enchanted_golden_apple',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(name='minecraft:music_disc_otherside', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:compass',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:sculk_catalyst',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(count=1, type='minecraft:set_count'),
                        LootFunctionSetDamage(
                            damage=ContextFloatProviderStructUniform(type='minecraft:uniform', min=0.8, max=1.0),
                            type='minecraft:set_damage',
                        ),
                        LootFunctionEnchantWithLevels(
                            levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=30, max=50),
                            options='#minecraft:on_random_loot',
                            type='minecraft:enchant_with_levels',
                        ),
                    ],
                    weight=2,
                    name='minecraft:diamond_hoe',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:lead',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:diamond_horse_armor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=2,
                    name='minecraft:saddle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_13', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:music_disc_cat', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=30, max=50),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=2,
                    name='minecraft:diamond_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:swift_sneak', type='minecraft:enchant_randomly'),
                    weight=3,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:sculk',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:sculk_sensor',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:candle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:amethyst_shard',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:experience_bottle',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:glow_berries',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=ContextIntProviderStructUniform(type='minecraft:uniform', min=20, max=39),
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    weight=3,
                    name='minecraft:iron_leggings',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:echo_shard',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:disc_fragment_5',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetPotion(id='minecraft:strong_regeneration', type='minecraft:set_potion'),
                    ],
                    weight=5,
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=10),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:soul_torch',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=15),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:coal',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=71, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:mending', type='minecraft:enchant_randomly'),
                    weight=4,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=4, name='minecraft:ward_armor_trim_smithing_template', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:silence_armor_trim_smithing_template', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:chests/ancient_city',
)

DESERT_PYRAMID = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:spider_eye',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=25,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=20, name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=15, name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(weight=5, name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    weight=10,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=20, name='minecraft:golden_apple', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:enchanted_golden_apple', type='minecraft:item'),
                LootPoolEntryEmpty(weight=15, type='minecraft:empty'),
            ],
        ),
        LootPool(
            rolls=4,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:gunpowder',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:sand',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=4, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:dune_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:unbreaking', type='minecraft:enchant_randomly'),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/desert_pyramid',
)

JUNGLE_TEMPLE = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:diamond',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:gold_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=15,
                    name='minecraft:bamboo',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=2,
                    name='minecraft:emerald',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:bone',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=16,
                    name='minecraft:rotten_flesh',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=3, name='minecraft:saddle', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:copper_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:iron_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:golden_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:diamond_horse_armor', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantWithLevels(
                        levels=30,
                        options='#minecraft:on_random_loot',
                        type='minecraft:enchant_with_levels',
                    ),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=2, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:wild_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:unbreaking', type='minecraft:enchant_randomly'),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/jungle_temple',
)

PILLAGER_OUTPOST = LootTable(
    type=LootContextParamSets.CHEST,
    pools=[
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[LootPoolEntryItem(name='minecraft:crossbow', type='minecraft:item')],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=7,
                    name='minecraft:wheat',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=5),
                        type='minecraft:set_count',
                    ),
                    weight=5,
                    name='minecraft:carrot',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:dark_oak_log',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
            entries=[
                LootPoolEntryItem(weight=7, name='minecraft:experience_bottle', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=6),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=7),
                        type='minecraft:set_count',
                    ),
                    weight=4,
                    name='minecraft:arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:tripwire_hook',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=3,
                    name='minecraft:iron_ingot',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='#minecraft:on_random_loot', type='minecraft:enchant_randomly'),
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
            entries=[LootPoolEntryItem(name='minecraft:goat_horn', type='minecraft:item')],
            modifier=LootFunctionSetInstrument(options='#minecraft:regular_goat_horns', type='minecraft:set_instrument'),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(weight=3, type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:sentry_armor_trim_smithing_template',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryEmpty(type='minecraft:empty'),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:quick_charge', type='minecraft:enchant_randomly'),
                    weight=2,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:chests/pillager_outpost',
)
