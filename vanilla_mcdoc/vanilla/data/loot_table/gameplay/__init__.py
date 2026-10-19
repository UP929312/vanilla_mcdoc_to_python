"""Vanilla's data/loot_table/gameplay/ files"""
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.FishingHookPredicate import FishingHookPredicate
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryAlternatives, LootPoolEntryEmpty, LootPoolEntryItem, LootPoolEntryLootTable
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionEntityProperties
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionEnchantRandomly, LootFunctionSetCount, LootFunctionSetPotion
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructUniform
from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate

ARMADILLO_SHED = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:armadillo_scute', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/armadillo_shed',
)

CAT_MORNING_GIFT = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(weight=10, name='minecraft:rabbit_hide', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:rabbit_foot', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:chicken', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:feather', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:rotten_flesh', type='minecraft:item'),
                LootPoolEntryItem(weight=10, name='minecraft:string', type='minecraft:item'),
                LootPoolEntryItem(weight=2, name='minecraft:phantom_membrane', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/cat_morning_gift',
)

CHICKEN_LAY = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(chicken_variant='minecraft:temperate'),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            name='minecraft:egg',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(chicken_variant='minecraft:warm'),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            name='minecraft:brown_egg',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(
                                    components=DataComponentExactPredicate(chicken_variant='minecraft:cold'),
                                ),
                                type='minecraft:entity_properties',
                            ),
                            name='minecraft:blue_egg',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/chicken_lay',
)

FISHING = LootTable(
    type=LootContextParamSets.FISHING,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryLootTable(
                    weight=10,
                    quality=-2,
                    value='minecraft:gameplay/fishing/junk',
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    condition=LootConditionEntityProperties(
                        entity=EntityTarget.THIS,
                        predicate=EntitySubPredicateMap(type_specific_fishing_hook=FishingHookPredicate(in_open_water=True)),
                        type='minecraft:entity_properties',
                    ),
                    weight=5,
                    quality=2,
                    value='minecraft:gameplay/fishing/treasure',
                    type='minecraft:loot_table',
                ),
                LootPoolEntryLootTable(
                    weight=85,
                    quality=-1,
                    value='minecraft:gameplay/fishing/fish',
                    type='minecraft:loot_table',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/fishing',
)

PANDA_SNEEZE = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:slime_ball', type='minecraft:item'),
                LootPoolEntryEmpty(weight=699, type='minecraft:empty'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/panda_sneeze',
)

PIGLIN_BARTERING = LootTable(
    type=LootContextParamSets.BARTER,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:soul_speed', type='minecraft:enchant_randomly'),
                    weight=5,
                    name='minecraft:book',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionEnchantRandomly(options='minecraft:soul_speed', type='minecraft:enchant_randomly'),
                    weight=8,
                    name='minecraft:iron_boots',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetPotion(id='minecraft:fire_resistance', type='minecraft:set_potion'),
                    weight=8,
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetPotion(id='minecraft:fire_resistance', type='minecraft:set_potion'),
                    weight=8,
                    name='minecraft:splash_potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetPotion(id='minecraft:water', type='minecraft:set_potion'),
                    weight=10,
                    name='minecraft:potion',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=10, max=36),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:iron_nugget',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=10,
                    name='minecraft:ender_pearl',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                    weight=10,
                    name='minecraft:dried_ghast',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=9),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:string',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=5, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=20,
                    name='minecraft:quartz',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=40, name='minecraft:obsidian', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:crying_obsidian',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(weight=40, name='minecraft:fire_charge', type='minecraft:item'),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:leather',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:soul_sand',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=8),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:nether_brick',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=6, max=12),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:spectral_arrow',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=16),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:gravel',
                    type='minecraft:item',
                ),
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=8, max=16),
                        type='minecraft:set_count',
                    ),
                    weight=40,
                    name='minecraft:blackstone',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/piglin_bartering',
)

SNIFFER_DIGGING = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(name='minecraft:torchflower_seeds', type='minecraft:item'),
                LootPoolEntryItem(name='minecraft:pitcher_pod', type='minecraft:item'),
            ],
        ),
    ],
    random_sequence='minecraft:gameplay/sniffer_digging',
)

TURTLE_GROW = LootTable(
    type=LootContextParamSets.GIFT,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:turtle_scute', type='minecraft:item')])],
    random_sequence='minecraft:gameplay/turtle_grow',
)
