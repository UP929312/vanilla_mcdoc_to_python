"""Vanilla's data/loot_table/blocks/ files"""
from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.loot.DynamicDrops import DynamicDrops
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.LootContextParamSets import LootContextParamSets
from vanilla_mcdoc.data.loot.LootPool import LootPool
from vanilla_mcdoc.data.loot.LootPoolEntry import LootPoolEntryAlternatives, LootPoolEntryDynamic, LootPoolEntryItem
from vanilla_mcdoc.data.loot.LootTable import LootTable
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionAnyOf, LootConditionEntityProperties, LootConditionInverted, LootConditionLocationCheck, LootConditionMatchBlock, LootConditionMatchTool, LootConditionRandomChance, LootConditionSurvivesExplosion, LootConditionTableBonus
from vanilla_mcdoc.data.loot.function.BinomialWithBonusCountFormula import ParametersStruct
from vanilla_mcdoc.data.loot.function.LimitCount import LimitStruct
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunctionApplyBonusBinomialWithBonusCount, LootFunctionApplyBonusOreDrops, LootFunctionApplyBonusUniformBonusCount, LootFunctionCopyComponents, LootFunctionCopyState, LootFunctionExplosionDecay, LootFunctionLimitCount, LootFunctionSetCount
from vanilla_mcdoc.data.loot.function.UniformBonusFormula import ParametersStruct as ParametersStruct2
from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProviderStructBinomial, ContextIntProviderStructUniform

ACACIA_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_button',
)

ACACIA_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:acacia_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:acacia_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_door',
)

ACACIA_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_fence',
)

ACACIA_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_fence_gate',
)

ACACIA_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_hanging_sign',
)

ACACIA_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:acacia_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:acacia_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_leaves',
)

ACACIA_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_log',
)

ACACIA_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_planks',
)

ACACIA_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_pressure_plate',
)

ACACIA_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_sapling',
)

ACACIA_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_shelf',
)

ACACIA_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_sign',
)

ACACIA_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:acacia_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:acacia_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/acacia_slab',
)

ACACIA_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_stairs',
)

ACACIA_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_trapdoor',
)

ACACIA_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/acacia_wood',
)

ACTIVATOR_RAIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:activator_rail', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/activator_rail',
)

ALLIUM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:allium', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/allium',
)

AMETHYST_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:amethyst_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/amethyst_block',
)

AMETHYST_CLUSTER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:amethyst_cluster',
                            type='minecraft:item',
                        ),
                        LootPoolEntryAlternatives(
                            children=[
                                LootPoolEntryItem(
                                    modifier=[
                                        LootFunctionSetCount(count=4, type='minecraft:set_count'),
                                        LootFunctionApplyBonusOreDrops(
                                            type='minecraft:apply_bonus',
                                            enchantment='minecraft:fortune',
                                            formula='minecraft:ore_drops',
                                        ),
                                    ],
                                    condition=LootConditionMatchTool(
                                        predicate=ItemPredicate(items='#minecraft:cluster_max_harvestables'),
                                        type='minecraft:match_tool',
                                    ),
                                    name='minecraft:amethyst_shard',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=[
                                        LootFunctionSetCount(count=2, type='minecraft:set_count'),
                                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                                    ],
                                    name='minecraft:amethyst_shard',
                                    type='minecraft:item',
                                ),
                            ],
                            type='minecraft:alternatives',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/amethyst_cluster',
)

ANCIENT_DEBRIS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:ancient_debris', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/ancient_debris',
)

ANDESITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:andesite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/andesite',
)

ANDESITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:andesite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:andesite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/andesite_slab',
)

ANDESITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:andesite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/andesite_stairs',
)

ANDESITE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:andesite_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/andesite_wall',
)

ANVIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:anvil', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/anvil',
)

ATTACHED_MELON_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructBinomial(n=3, p=0.53333336, type='minecraft:binomial'),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
            ],
            modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
        ),
    ],
    random_sequence='minecraft:blocks/attached_melon_stem',
)

ATTACHED_PUMPKIN_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(
                        count=ContextIntProviderStructBinomial(n=3, p=0.53333336, type='minecraft:binomial'),
                        type='minecraft:set_count',
                    ),
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
            ],
            modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
        ),
    ],
    random_sequence='minecraft:blocks/attached_pumpkin_stem',
)

AZALEA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:azalea', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/azalea',
)

AZALEA_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:azalea_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:azalea',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/azalea_leaves',
)

AZURE_BLUET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:azure_bluet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/azure_bluet',
)

BAMBOO = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo',
)

BAMBOO_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_block',
)

BAMBOO_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_button',
)

BAMBOO_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:bamboo_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:bamboo_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_door',
)

BAMBOO_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_fence',
)

BAMBOO_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_fence_gate',
)

BAMBOO_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_hanging_sign',
)

BAMBOO_MOSAIC = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_mosaic', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_mosaic',
)

BAMBOO_MOSAIC_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:bamboo_mosaic_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:bamboo_mosaic_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_mosaic_slab',
)

BAMBOO_MOSAIC_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_mosaic_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_mosaic_stairs',
)

BAMBOO_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_planks',
)

BAMBOO_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_pressure_plate',
)

BAMBOO_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_sapling',
)

BAMBOO_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_shelf',
)

BAMBOO_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_sign',
)

BAMBOO_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:bamboo_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:bamboo_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_slab',
)

BAMBOO_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_stairs',
)

BAMBOO_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bamboo_trapdoor',
)

BARREL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:barrel',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/barrel',
)

BASALT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:basalt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/basalt',
)

BEACON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:beacon',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/beacon',
)

BEEHIVE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionCopyComponents(
                                    source='block_entity',
                                    include=['minecraft:bees'],
                                    type='minecraft:copy_components',
                                ),
                                LootFunctionCopyState(
                                    block='minecraft:beehive',
                                    properties=['honey_level'],
                                    type='minecraft:copy_state',
                                ),
                            ],
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:beehive',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(name='minecraft:beehive', type='minecraft:item'),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/beehive',
)

BEETROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:beetroots',
                                state={'age': '3'},
                                type='minecraft:match_block',
                            ),
                            name='minecraft:beetroot',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(name='minecraft:beetroot_seeds', type='minecraft:item'),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionApplyBonusBinomialWithBonusCount(
                        parameters=ParametersStruct(extra=3, probability=0.5714286),
                        type='minecraft:apply_bonus',
                        enchantment='minecraft:fortune',
                        formula='minecraft:binomial_with_bonus_count',
                    ),
                    name='minecraft:beetroot_seeds',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionMatchBlock(blocks='minecraft:beetroots', state={'age': '3'}, type='minecraft:match_block'),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/beetroots',
)

BEE_NEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:bees'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:bee_nest',
                            properties=['honey_level'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:bee_nest',
                    type='minecraft:item',
                ),
            ],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/bee_nest',
)

BELL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bell', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bell',
)

BIG_DRIPLEAF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:big_dripleaf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/big_dripleaf',
)

BIG_DRIPLEAF_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:big_dripleaf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/big_dripleaf_stem',
)

BIRCH_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_button',
)

BIRCH_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:birch_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:birch_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_door',
)

BIRCH_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_fence',
)

BIRCH_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_fence_gate',
)

BIRCH_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_hanging_sign',
)

BIRCH_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:birch_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:birch_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/birch_leaves',
)

BIRCH_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_log',
)

BIRCH_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_planks',
)

BIRCH_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_pressure_plate',
)

BIRCH_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_sapling',
)

BIRCH_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_shelf',
)

BIRCH_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_sign',
)

BIRCH_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:birch_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:birch_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/birch_slab',
)

BIRCH_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_stairs',
)

BIRCH_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_trapdoor',
)

BIRCH_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/birch_wood',
)

BLACKSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blackstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blackstone',
)

BLACKSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blackstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:blackstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/blackstone_slab',
)

BLACKSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blackstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blackstone_stairs',
)

BLACKSTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blackstone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blackstone_wall',
)

BLACK_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:black_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_banner',
)

BLACK_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:black_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:black_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_bed',
)

BLACK_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:black_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:black_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:black_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:black_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/black_candle',
)

BLACK_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:black_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/black_candle_cake',
)

BLACK_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_carpet',
)

BLACK_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_concrete',
)

BLACK_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_concrete_powder',
)

BLACK_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:black_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:black_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/black_concrete_slab',
)

BLACK_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_concrete_stairs',
)

BLACK_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_glazed_terracotta',
)

BLACK_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:black_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/black_shulker_box',
)

BLACK_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/black_stained_glass',
)

BLACK_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/black_stained_glass_pane',
)

BLACK_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_terracotta',
)

BLACK_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_wool',
)

BLACK_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:black_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:black_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/black_wool_slab',
)

BLACK_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:black_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/black_wool_stairs',
)

BLAST_FURNACE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:blast_furnace',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blast_furnace',
)

BLUE_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:blue_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_banner',
)

BLUE_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:blue_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:blue_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_bed',
)

BLUE_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blue_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blue_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blue_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:blue_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/blue_candle',
)

BLUE_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:blue_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/blue_candle_cake',
)

BLUE_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_carpet',
)

BLUE_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_concrete',
)

BLUE_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_concrete_powder',
)

BLUE_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blue_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:blue_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/blue_concrete_slab',
)

BLUE_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_concrete_stairs',
)

BLUE_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_glazed_terracotta',
)

BLUE_ICE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_ice', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/blue_ice',
)

BLUE_ORCHID = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_orchid', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_orchid',
)

BLUE_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:blue_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/blue_shulker_box',
)

BLUE_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/blue_stained_glass',
)

BLUE_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/blue_stained_glass_pane',
)

BLUE_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_terracotta',
)

BLUE_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_wool',
)

BLUE_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:blue_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:blue_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/blue_wool_slab',
)

BLUE_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/blue_wool_stairs',
)

BONE_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bone_block',
)

BOOKSHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:bookshelf',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(count=3, type='minecraft:set_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:book',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/bookshelf',
)

BRAIN_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brain_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/brain_coral',
)

BRAIN_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:brain_coral_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dead_brain_coral_block',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brain_coral_block',
)

BRAIN_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brain_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/brain_coral_fan',
)

BREWING_STAND = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:brewing_stand',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brewing_stand',
)

BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/bricks',
)

BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brick_slab',
)

BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brick_stairs',
)

BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brick_wall',
)

BRITTLE_ICE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brittle_ice', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/brittle_ice',
)

BROWN_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:brown_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_banner',
)

BROWN_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:brown_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:brown_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_bed',
)

BROWN_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brown_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brown_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brown_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:brown_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brown_candle',
)

BROWN_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:brown_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/brown_candle_cake',
)

BROWN_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_carpet',
)

BROWN_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_concrete',
)

BROWN_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_concrete_powder',
)

BROWN_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brown_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:brown_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brown_concrete_slab',
)

BROWN_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_concrete_stairs',
)

BROWN_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_glazed_terracotta',
)

BROWN_MUSHROOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_mushroom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_mushroom',
)

BROWN_MUSHROOM_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:brown_mushroom_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-6, max=2),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(min=0), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:brown_mushroom',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brown_mushroom_block',
)

BROWN_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:brown_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brown_shulker_box',
)

BROWN_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/brown_stained_glass',
)

BROWN_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/brown_stained_glass_pane',
)

BROWN_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_terracotta',
)

BROWN_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_wool',
)

BROWN_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:brown_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:brown_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/brown_wool_slab',
)

BROWN_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/brown_wool_stairs',
)

BUBBLE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bubble_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/bubble_coral',
)

BUBBLE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:bubble_coral_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dead_bubble_coral_block',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/bubble_coral_block',
)

BUBBLE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bubble_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/bubble_coral_fan',
)

BUDDING_AMETHYST = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/budding_amethyst')

BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bush', type='minecraft:item')],
            condition=LootConditionAnyOf(
                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                type='minecraft:any_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/bush',
)

CACTUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cactus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cactus',
)

CACTUS_FLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cactus_flower', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cactus_flower',
)

CAKE = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/cake')

CALCITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:calcite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/calcite',
)

CALIBRATED_SCULK_SENSOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:calibrated_sculk_sensor', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/calibrated_sculk_sensor',
)

CAMPFIRE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:campfire',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:charcoal',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/campfire',
)

CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/candle',
)

CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/candle_cake',
)

CARROTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:carrot', type='minecraft:item')]),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionApplyBonusBinomialWithBonusCount(
                        parameters=ParametersStruct(extra=3, probability=0.5714286),
                        type='minecraft:apply_bonus',
                        enchantment='minecraft:fortune',
                        formula='minecraft:binomial_with_bonus_count',
                    ),
                    name='minecraft:carrot',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionMatchBlock(blocks='minecraft:carrots', state={'age': '7'}, type='minecraft:match_block'),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/carrots',
)

CARTOGRAPHY_TABLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cartography_table', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cartography_table',
)

CARVED_PUMPKIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:carved_pumpkin', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/carved_pumpkin',
)

CAULDRON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cauldron', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cauldron',
)

CAVE_VINES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:glow_berries', type='minecraft:item')],
            condition=LootConditionMatchBlock(
                blocks='minecraft:cave_vines',
                state={'berries': 'true'},
                type='minecraft:match_block',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/cave_vines',
)

CAVE_VINES_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:glow_berries', type='minecraft:item')],
            condition=LootConditionMatchBlock(
                blocks='minecraft:cave_vines_plant',
                state={'berries': 'true'},
                type='minecraft:match_block',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/cave_vines_plant',
)

CHERRY_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_button',
)

CHERRY_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:cherry_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:cherry_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_door',
)

CHERRY_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_fence',
)

CHERRY_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_fence_gate',
)

CHERRY_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_hanging_sign',
)

CHERRY_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:cherry_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:cherry_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_leaves',
)

CHERRY_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_log',
)

CHERRY_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_planks',
)

CHERRY_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_pressure_plate',
)

CHERRY_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_sapling',
)

CHERRY_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_shelf',
)

CHERRY_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_sign',
)

CHERRY_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cherry_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cherry_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cherry_slab',
)

CHERRY_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_stairs',
)

CHERRY_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_trapdoor',
)

CHERRY_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cherry_wood',
)

CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chest',
)

CHIPPED_ANVIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chipped_anvil', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chipped_anvil',
)

CHISELED_BOOKSHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_bookshelf', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_bookshelf',
)

CHISELED_CINNABAR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_cinnabar', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_cinnabar',
)

CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_copper',
)

CHISELED_DEEPSLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_deepslate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_deepslate',
)

CHISELED_NETHER_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_nether_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_nether_bricks',
)

CHISELED_POLISHED_BLACKSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_polished_blackstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_polished_blackstone',
)

CHISELED_QUARTZ_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_quartz_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_quartz_block',
)

CHISELED_RED_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_red_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_red_sandstone',
)

CHISELED_RESIN_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_resin_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_resin_bricks',
)

CHISELED_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_sandstone',
)

CHISELED_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_stone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_stone_bricks',
)

CHISELED_SULFUR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_sulfur', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_sulfur',
)

CHISELED_TUFF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_tuff', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_tuff',
)

CHISELED_TUFF_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_tuff_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/chiseled_tuff_bricks',
)

CHORUS_FLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionAllOf(
                        terms=[
                            LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            LootConditionEntityProperties(
                                entity=EntityTarget.THIS,
                                predicate=EntitySubPredicateMap(),
                                type='minecraft:entity_properties',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    name='minecraft:chorus_flower',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/chorus_flower',
)

CHORUS_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=1),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:chorus_fruit',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/chorus_plant',
)

CINNABAR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar',
)

CINNABAR_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_bricks',
)

CINNABAR_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cinnabar_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cinnabar_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_brick_slab',
)

CINNABAR_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_brick_stairs',
)

CINNABAR_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_brick_wall',
)

CINNABAR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cinnabar_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cinnabar_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_slab',
)

CINNABAR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_stairs',
)

CINNABAR_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cinnabar_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cinnabar_wall',
)

CLAY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:clay',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(count=4, type='minecraft:set_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:clay_ball',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/clay',
)

CLOSED_EYEBLOSSOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:closed_eyeblossom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/closed_eyeblossom',
)

COAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:coal_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/coal_block',
)

COAL_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:coal_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:coal',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/coal_ore',
)

COARSE_DIRT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:coarse_dirt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/coarse_dirt',
)

COBBLED_DEEPSLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobbled_deepslate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobbled_deepslate',
)

COBBLED_DEEPSLATE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cobbled_deepslate_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cobbled_deepslate_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cobbled_deepslate_slab',
)

COBBLED_DEEPSLATE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobbled_deepslate_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobbled_deepslate_stairs',
)

COBBLED_DEEPSLATE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobbled_deepslate_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobbled_deepslate_wall',
)

COBBLESTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobblestone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobblestone',
)

COBBLESTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cobblestone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cobblestone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cobblestone_slab',
)

COBBLESTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobblestone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobblestone_stairs',
)

COBBLESTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobblestone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cobblestone_wall',
)

COBWEB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:cobweb',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:string',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cobweb',
)

COCOA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cocoa',
                                state={'age': '2'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cocoa_beans',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cocoa',
)

COMPARATOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:comparator', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/comparator',
)

COMPOSTER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    name='minecraft:composter',
                    type='minecraft:item',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bone_meal', type='minecraft:item')],
            condition=LootConditionMatchBlock(blocks='minecraft:composter', state={'level': '8'}, type='minecraft:match_block'),
        ),
    ],
    random_sequence='minecraft:blocks/composter',
)

CONDUIT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:conduit', type='minecraft:item')])],
    random_sequence='minecraft:blocks/conduit',
)

COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_bars',
)

COPPER_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_block',
)

COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_bulb',
)

COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_chain',
)

COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_chest',
)

COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_door',
)

COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_golem_statue',
)

COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_grate',
)

COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_lantern',
)

COPPER_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:copper_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_copper',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/copper_ore',
)

COPPER_TORCH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_torch', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_torch',
)

COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/copper_trapdoor',
)

CORNFLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cornflower', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cornflower',
)

CRACKED_DEEPSLATE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_deepslate_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cracked_deepslate_bricks',
)

CRACKED_DEEPSLATE_TILES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_deepslate_tiles', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cracked_deepslate_tiles',
)

CRACKED_NETHER_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_nether_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cracked_nether_bricks',
)

CRACKED_POLISHED_BLACKSTONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_polished_blackstone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cracked_polished_blackstone_bricks',
)

CRACKED_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_stone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cracked_stone_bricks',
)

CRAFTER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crafter', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crafter',
)

CRAFTING_TABLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crafting_table', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crafting_table',
)

CREAKING_HEART = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:creaking_heart',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=3),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(max=9), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:resin_clump',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/creaking_heart',
)

CREEPER_HEAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:creeper_head',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/creeper_head',
)

CRIMSON_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_button',
)

CRIMSON_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:crimson_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:crimson_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_door',
)

CRIMSON_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_fence',
)

CRIMSON_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_fence_gate',
)

CRIMSON_FUNGUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_fungus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_fungus',
)

CRIMSON_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_hanging_sign',
)

CRIMSON_HYPHAE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_hyphae', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_hyphae',
)

CRIMSON_NYLIUM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:crimson_nylium',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:netherrack',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/crimson_nylium',
)

CRIMSON_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_planks',
)

CRIMSON_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_pressure_plate',
)

CRIMSON_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_roots',
)

CRIMSON_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_shelf',
)

CRIMSON_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_sign',
)

CRIMSON_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:crimson_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:crimson_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/crimson_slab',
)

CRIMSON_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_stairs',
)

CRIMSON_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_stem', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_stem',
)

CRIMSON_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crimson_trapdoor',
)

CRYING_OBSIDIAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crying_obsidian', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/crying_obsidian',
)

CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cut_copper',
)

CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cut_copper_slab',
)

CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cut_copper_stairs',
)

CUT_RED_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cut_red_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cut_red_sandstone',
)

CUT_RED_SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cut_red_sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cut_red_sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cut_red_sandstone_slab',
)

CUT_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cut_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cut_sandstone',
)

CUT_SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cut_sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cut_sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cut_sandstone_slab',
)

CYAN_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:cyan_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_banner',
)

CYAN_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:cyan_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:cyan_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_bed',
)

CYAN_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cyan_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cyan_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cyan_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cyan_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cyan_candle',
)

CYAN_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:cyan_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/cyan_candle_cake',
)

CYAN_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_carpet',
)

CYAN_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_concrete',
)

CYAN_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_concrete_powder',
)

CYAN_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cyan_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cyan_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cyan_concrete_slab',
)

CYAN_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_concrete_stairs',
)

CYAN_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_glazed_terracotta',
)

CYAN_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:cyan_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cyan_shulker_box',
)

CYAN_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/cyan_stained_glass',
)

CYAN_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/cyan_stained_glass_pane',
)

CYAN_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_terracotta',
)

CYAN_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_wool',
)

CYAN_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:cyan_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:cyan_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/cyan_wool_slab',
)

CYAN_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cyan_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/cyan_wool_stairs',
)

DAMAGED_ANVIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:damaged_anvil', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/damaged_anvil',
)

DANDELION = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dandelion', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dandelion',
)

DARK_OAK_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_button',
)

DARK_OAK_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:dark_oak_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:dark_oak_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_door',
)

DARK_OAK_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_fence',
)

DARK_OAK_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_fence_gate',
)

DARK_OAK_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_hanging_sign',
)

DARK_OAK_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:dark_oak_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:dark_oak_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionAllOf(
                        terms=[
                            LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.005, 0.0055555557, 0.00625, 0.008333334, 0.025],
                                type='minecraft:table_bonus',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_leaves',
)

DARK_OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_log',
)

DARK_OAK_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_planks',
)

DARK_OAK_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_pressure_plate',
)

DARK_OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_sapling',
)

DARK_OAK_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_shelf',
)

DARK_OAK_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_sign',
)

DARK_OAK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:dark_oak_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:dark_oak_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_slab',
)

DARK_OAK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_stairs',
)

DARK_OAK_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_trapdoor',
)

DARK_OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_oak_wood',
)

DARK_PRISMARINE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_prismarine', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_prismarine',
)

DARK_PRISMARINE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:dark_prismarine_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:dark_prismarine_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/dark_prismarine_slab',
)

DARK_PRISMARINE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_prismarine_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dark_prismarine_stairs',
)

DAYLIGHT_DETECTOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:daylight_detector', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/daylight_detector',
)

DEAD_BRAIN_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_brain_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_brain_coral',
)

DEAD_BRAIN_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_brain_coral_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dead_brain_coral_block',
)

DEAD_BRAIN_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_brain_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_brain_coral_fan',
)

DEAD_BUBBLE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_bubble_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_bubble_coral',
)

DEAD_BUBBLE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_bubble_coral_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dead_bubble_coral_block',
)

DEAD_BUBBLE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_bubble_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_bubble_coral_fan',
)

DEAD_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_shear',
                            name='minecraft:dead_bush',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=0, max=2),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:stick',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/dead_bush',
)

DEAD_FIRE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_fire_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_fire_coral',
)

DEAD_FIRE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_fire_coral_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dead_fire_coral_block',
)

DEAD_FIRE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_fire_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_fire_coral_fan',
)

DEAD_HORN_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_horn_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_horn_coral',
)

DEAD_HORN_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_horn_coral_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dead_horn_coral_block',
)

DEAD_HORN_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_horn_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_horn_coral_fan',
)

DEAD_TUBE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_tube_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_tube_coral',
)

DEAD_TUBE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_tube_coral_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dead_tube_coral_block',
)

DEAD_TUBE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_tube_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/dead_tube_coral_fan',
)

DECORATED_POT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryDynamic(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:decorated_pot',
                                state={'cracked': 'true'},
                                type='minecraft:match_block',
                            ),
                            name=DynamicDrops.SHERDS,
                            type='minecraft:dynamic',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionCopyComponents(
                                source='block_entity',
                                include=['minecraft:pot_decorations'],
                                type='minecraft:copy_components',
                            ),
                            name='minecraft:decorated_pot',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/decorated_pot',
)

DEEPSLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:cobbled_deepslate',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate',
)

DEEPSLATE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_bricks',
)

DEEPSLATE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:deepslate_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:deepslate_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_brick_slab',
)

DEEPSLATE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_brick_stairs',
)

DEEPSLATE_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_brick_wall',
)

DEEPSLATE_COAL_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_coal_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:coal',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_coal_ore',
)

DEEPSLATE_COPPER_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_copper_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_copper',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_copper_ore',
)

DEEPSLATE_DIAMOND_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_diamond_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:diamond',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_diamond_ore',
)

DEEPSLATE_EMERALD_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_emerald_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:emerald',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_emerald_ore',
)

DEEPSLATE_GOLD_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_gold_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_gold',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_gold_ore',
)

DEEPSLATE_IRON_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_iron_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_iron',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_iron_ore',
)

DEEPSLATE_LAPIS_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_lapis_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:lapis_lazuli',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_lapis_ore',
)

DEEPSLATE_REDSTONE_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:deepslate_redstone_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=5),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:redstone',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_redstone_ore',
)

DEEPSLATE_TILES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_tiles', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_tiles',
)

DEEPSLATE_TILE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:deepslate_tile_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:deepslate_tile_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_tile_slab',
)

DEEPSLATE_TILE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_tile_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_tile_stairs',
)

DEEPSLATE_TILE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate_tile_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/deepslate_tile_wall',
)

DETECTOR_RAIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:detector_rail', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/detector_rail',
)

DIAMOND_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:diamond_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/diamond_block',
)

DIAMOND_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:diamond_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:diamond',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/diamond_ore',
)

DIORITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:diorite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/diorite',
)

DIORITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:diorite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:diorite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/diorite_slab',
)

DIORITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:diorite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/diorite_stairs',
)

DIORITE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:diorite_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/diorite_wall',
)

DIRT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dirt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dirt',
)

DIRT_PATH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dirt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dirt_path',
)

DISPENSER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:dispenser',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dispenser',
)

DRAGON_EGG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:dragon_egg', type='minecraft:item')])],
    random_sequence='minecraft:blocks/dragon_egg',
)

DRAGON_HEAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:dragon_head',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/dragon_head',
)

DRIED_GHAST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dried_ghast', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dried_ghast',
)

DRIED_KELP_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dried_kelp_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dried_kelp_block',
)

DRIPSTONE_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dripstone_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dripstone_block',
)

DROPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:dropper',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/dropper',
)

EMERALD_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:emerald_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/emerald_block',
)

EMERALD_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:emerald_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:emerald',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/emerald_ore',
)

ENCHANTING_TABLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:enchanting_table',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/enchanting_table',
)

ENDER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:ender_chest',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(count=8, type='minecraft:set_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:obsidian',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/ender_chest',
)

END_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:end_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/end_rod',
)

END_STONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:end_stone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/end_stone',
)

END_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:end_stone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/end_stone_bricks',
)

END_STONE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:end_stone_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:end_stone_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/end_stone_brick_slab',
)

END_STONE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:end_stone_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/end_stone_brick_stairs',
)

END_STONE_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:end_stone_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/end_stone_brick_wall',
)

EXPOSED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_chiseled_copper',
)

EXPOSED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper',
)

EXPOSED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_bars',
)

EXPOSED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_bulb',
)

EXPOSED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_chain',
)

EXPOSED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:exposed_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_chest',
)

EXPOSED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:exposed_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:exposed_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_door',
)

EXPOSED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:exposed_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:exposed_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_golem_statue',
)

EXPOSED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_grate',
)

EXPOSED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_lantern',
)

EXPOSED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_copper_trapdoor',
)

EXPOSED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_cut_copper',
)

EXPOSED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:exposed_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:exposed_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/exposed_cut_copper_slab',
)

EXPOSED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_cut_copper_stairs',
)

EXPOSED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:exposed_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/exposed_lightning_rod',
)

FARMLAND = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dirt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/farmland',
)

FERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_shear',
                            name='minecraft:fern',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=2),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            condition=LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/fern',
)

FIRE = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/fire')

FIREFLY_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:firefly_bush', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/firefly_bush',
)

FIRE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:fire_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/fire_coral',
)

FIRE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:fire_coral_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dead_fire_coral_block',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/fire_coral_block',
)

FIRE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:fire_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/fire_coral_fan',
)

FLETCHING_TABLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:fletching_table', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/fletching_table',
)

FLOWERING_AZALEA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flowering_azalea', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/flowering_azalea',
)

FLOWERING_AZALEA_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:flowering_azalea_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:flowering_azalea',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/flowering_azalea_leaves',
)

FLOWER_POT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/flower_pot',
)

FROGSPAWN = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/frogspawn')

FROSTED_ICE = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/frosted_ice')

FURNACE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:furnace',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/furnace',
)

GILDED_BLACKSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:gilded_blackstone',
                            type='minecraft:item',
                        ),
                        LootPoolEntryAlternatives(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            children=[
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(
                                        count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=5),
                                        type='minecraft:set_count',
                                    ),
                                    condition=LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.1, 0.14285715, 0.25, 1.0],
                                        type='minecraft:table_bonus',
                                    ),
                                    name='minecraft:gold_nugget',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(name='minecraft:gilded_blackstone', type='minecraft:item'),
                            ],
                            type='minecraft:alternatives',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gilded_blackstone',
)

GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/glass',
)

GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/glass_pane',
)

GLOWSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:glowstone',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(min=1, max=4), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:glowstone_dust',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/glowstone',
)

GLOW_LICHEN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'down': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'up': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'north': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'south': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'west': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:glow_lichen',
                                state={'east': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(count=-1, add=True, type='minecraft:set_count'),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition='minecraft:tool/can_shear',
                    name='minecraft:glow_lichen',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/glow_lichen',
)

GOLDEN_DANDELION = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:golden_dandelion', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/golden_dandelion',
)

GOLD_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gold_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gold_block',
)

GOLD_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:gold_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_gold',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gold_ore',
)

GRANITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:granite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/granite',
)

GRANITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:granite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:granite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/granite_slab',
)

GRANITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:granite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/granite_stairs',
)

GRANITE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:granite_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/granite_wall',
)

GRASS_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:grass_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dirt',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/grass_block',
)

GRAVEL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:gravel',
                            type='minecraft:item',
                        ),
                        LootPoolEntryAlternatives(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            children=[
                                LootPoolEntryItem(
                                    condition=LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.1, 0.14285715, 0.25, 1.0],
                                        type='minecraft:table_bonus',
                                    ),
                                    name='minecraft:flint',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(name='minecraft:gravel', type='minecraft:item'),
                            ],
                            type='minecraft:alternatives',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gravel',
)

GRAY_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:gray_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_banner',
)

GRAY_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:gray_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:gray_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_bed',
)

GRAY_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:gray_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:gray_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:gray_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:gray_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gray_candle',
)

GRAY_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:gray_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/gray_candle_cake',
)

GRAY_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_carpet',
)

GRAY_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_concrete',
)

GRAY_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_concrete_powder',
)

GRAY_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:gray_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:gray_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gray_concrete_slab',
)

GRAY_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_concrete_stairs',
)

GRAY_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_glazed_terracotta',
)

GRAY_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:gray_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gray_shulker_box',
)

GRAY_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/gray_stained_glass',
)

GRAY_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/gray_stained_glass_pane',
)

GRAY_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_terracotta',
)

GRAY_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_wool',
)

GRAY_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:gray_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:gray_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/gray_wool_slab',
)

GRAY_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:gray_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/gray_wool_stairs',
)

GREEN_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:green_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_banner',
)

GREEN_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:green_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:green_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_bed',
)

GREEN_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:green_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:green_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:green_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:green_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/green_candle',
)

GREEN_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:green_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/green_candle_cake',
)

GREEN_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_carpet',
)

GREEN_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_concrete',
)

GREEN_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_concrete_powder',
)

GREEN_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:green_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:green_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/green_concrete_slab',
)

GREEN_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_concrete_stairs',
)

GREEN_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_glazed_terracotta',
)

GREEN_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:green_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/green_shulker_box',
)

GREEN_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/green_stained_glass',
)

GREEN_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/green_stained_glass_pane',
)

GREEN_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_terracotta',
)

GREEN_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_wool',
)

GREEN_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:green_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:green_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/green_wool_slab',
)

GREEN_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:green_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/green_wool_stairs',
)

GRINDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:grindstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/grindstone',
)

HANGING_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:hanging_roots', type='minecraft:item')],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/hanging_roots',
)

HAY_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:hay_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/hay_block',
)

HEAVY_CORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:heavy_core', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/heavy_core',
)

HEAVY_WEIGHTED_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:heavy_weighted_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/heavy_weighted_pressure_plate',
)

HONEYCOMB_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:honeycomb_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/honeycomb_block',
)

HONEY_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:honey_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/honey_block',
)

HOPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:hopper',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/hopper',
)

HORN_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:horn_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/horn_coral',
)

HORN_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:horn_coral_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dead_horn_coral_block',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/horn_coral_block',
)

HORN_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:horn_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/horn_coral_fan',
)

ICE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:ice', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/ice',
)

ICE_CRYSTAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:ice_crystal', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/ice_crystal',
)

ICICLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:icicle', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/icicle',
)

INFESTED_CHISELED_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:chiseled_stone_bricks', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_chiseled_stone_bricks',
)

INFESTED_COBBLESTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cobblestone', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_cobblestone',
)

INFESTED_CRACKED_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cracked_stone_bricks', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_cracked_stone_bricks',
)

INFESTED_DEEPSLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:deepslate', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_deepslate',
)

INFESTED_MOSSY_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_stone_bricks', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_mossy_stone_bricks',
)

INFESTED_STONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_stone',
)

INFESTED_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_bricks', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/infested_stone_bricks',
)

IRON_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:iron_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/iron_bars',
)

IRON_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:iron_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/iron_block',
)

IRON_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:iron_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/iron_chain',
)

IRON_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:iron_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:iron_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/iron_door',
)

IRON_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:iron_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:raw_iron',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/iron_ore',
)

IRON_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:iron_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/iron_trapdoor',
)

JACK_O_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jack_o_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jack_o_lantern',
)

JUKEBOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jukebox', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jukebox',
)

JUNGLE_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_button',
)

JUNGLE_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:jungle_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:jungle_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_door',
)

JUNGLE_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_fence',
)

JUNGLE_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_fence_gate',
)

JUNGLE_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_hanging_sign',
)

JUNGLE_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:jungle_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.025, 0.027777778, 0.03125, 0.041666668, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:jungle_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_leaves',
)

JUNGLE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_log',
)

JUNGLE_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_planks',
)

JUNGLE_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_pressure_plate',
)

JUNGLE_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_sapling',
)

JUNGLE_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_shelf',
)

JUNGLE_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_sign',
)

JUNGLE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:jungle_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:jungle_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/jungle_slab',
)

JUNGLE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_stairs',
)

JUNGLE_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_trapdoor',
)

JUNGLE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/jungle_wood',
)

KELP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:kelp', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/kelp',
)

KELP_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:kelp', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/kelp_plant',
)

LADDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:ladder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/ladder',
)

LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lantern',
)

LAPIS_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lapis_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lapis_block',
)

LAPIS_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:lapis_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=9),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:lapis_lazuli',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/lapis_ore',
)

LARGE_AMETHYST_BUD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:large_amethyst_bud', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/large_amethyst_bud',
)

LARGE_FERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                            condition='minecraft:tool/can_shear',
                            name='minecraft:fern',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionMatchBlock(
                        blocks='minecraft:large_fern',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    LootConditionLocationCheck(
                        offsetY=1,
                        predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:large_fern', state={'half': 'upper'})),
                        type='minecraft:location_check',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                            condition='minecraft:tool/can_shear',
                            name='minecraft:fern',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionMatchBlock(
                        blocks='minecraft:large_fern',
                        state={'half': 'upper'},
                        type='minecraft:match_block',
                    ),
                    LootConditionLocationCheck(
                        offsetY=-1,
                        predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:large_fern', state={'half': 'lower'})),
                        type='minecraft:location_check',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/large_fern',
)

LAVA_CAULDRON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cauldron', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lava_cauldron',
)

LEAF_LITTER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:leaf_litter',
                                state={'segment_amount': '1'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:leaf_litter',
                                state={'segment_amount': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:leaf_litter',
                                state={'segment_amount': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:leaf_litter',
                                state={'segment_amount': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:leaf_litter',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/leaf_litter',
)

LECTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lectern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lectern',
)

LEVER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lever', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lever',
)

LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lightning_rod',
)

LIGHT_BLUE_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:light_blue_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_banner',
)

LIGHT_BLUE_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:light_blue_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:light_blue_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_bed',
)

LIGHT_BLUE_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_blue_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_blue_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_blue_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_blue_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_candle',
)

LIGHT_BLUE_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:light_blue_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/light_blue_candle_cake',
)

LIGHT_BLUE_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_carpet',
)

LIGHT_BLUE_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_concrete',
)

LIGHT_BLUE_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_concrete_powder',
)

LIGHT_BLUE_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_blue_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_blue_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_concrete_slab',
)

LIGHT_BLUE_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_concrete_stairs',
)

LIGHT_BLUE_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_glazed_terracotta',
)

LIGHT_BLUE_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:light_blue_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_shulker_box',
)

LIGHT_BLUE_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_stained_glass',
)

LIGHT_BLUE_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_stained_glass_pane',
)

LIGHT_BLUE_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_terracotta',
)

LIGHT_BLUE_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_wool',
)

LIGHT_BLUE_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_blue_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_blue_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_wool_slab',
)

LIGHT_BLUE_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_blue_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_blue_wool_stairs',
)

LIGHT_GRAY_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:light_gray_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_banner',
)

LIGHT_GRAY_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:light_gray_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:light_gray_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_bed',
)

LIGHT_GRAY_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_gray_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_gray_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_gray_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_gray_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_candle',
)

LIGHT_GRAY_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:light_gray_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/light_gray_candle_cake',
)

LIGHT_GRAY_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_carpet',
)

LIGHT_GRAY_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_concrete',
)

LIGHT_GRAY_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_concrete_powder',
)

LIGHT_GRAY_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_gray_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_gray_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_concrete_slab',
)

LIGHT_GRAY_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_concrete_stairs',
)

LIGHT_GRAY_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_glazed_terracotta',
)

LIGHT_GRAY_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:light_gray_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_shulker_box',
)

LIGHT_GRAY_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_stained_glass',
)

LIGHT_GRAY_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_stained_glass_pane',
)

LIGHT_GRAY_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_terracotta',
)

LIGHT_GRAY_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_wool',
)

LIGHT_GRAY_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:light_gray_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:light_gray_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_wool_slab',
)

LIGHT_GRAY_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_gray_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_gray_wool_stairs',
)

LIGHT_WEIGHTED_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:light_weighted_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/light_weighted_pressure_plate',
)

LILAC = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:lilac',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:lilac',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lilac',
)

LILY_OF_THE_VALLEY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lily_of_the_valley', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lily_of_the_valley',
)

LILY_PAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lily_pad', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lily_pad',
)

LIME_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:lime_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_banner',
)

LIME_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:lime_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:lime_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_bed',
)

LIME_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:lime_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:lime_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:lime_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:lime_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/lime_candle',
)

LIME_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:lime_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/lime_candle_cake',
)

LIME_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_carpet',
)

LIME_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_concrete',
)

LIME_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_concrete_powder',
)

LIME_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:lime_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:lime_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/lime_concrete_slab',
)

LIME_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_concrete_stairs',
)

LIME_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_glazed_terracotta',
)

LIME_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:lime_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/lime_shulker_box',
)

LIME_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/lime_stained_glass',
)

LIME_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/lime_stained_glass_pane',
)

LIME_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_terracotta',
)

LIME_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_wool',
)

LIME_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:lime_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:lime_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/lime_wool_slab',
)

LIME_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lime_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lime_wool_stairs',
)

LODESTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lodestone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/lodestone',
)

LOOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:loom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/loom',
)

MAGENTA_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:magenta_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_banner',
)

MAGENTA_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:magenta_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:magenta_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_bed',
)

MAGENTA_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:magenta_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:magenta_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:magenta_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:magenta_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/magenta_candle',
)

MAGENTA_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:magenta_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/magenta_candle_cake',
)

MAGENTA_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_carpet',
)

MAGENTA_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_concrete',
)

MAGENTA_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_concrete_powder',
)

MAGENTA_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:magenta_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:magenta_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/magenta_concrete_slab',
)

MAGENTA_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_concrete_stairs',
)

MAGENTA_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_glazed_terracotta',
)

MAGENTA_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:magenta_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/magenta_shulker_box',
)

MAGENTA_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/magenta_stained_glass',
)

MAGENTA_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/magenta_stained_glass_pane',
)

MAGENTA_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_terracotta',
)

MAGENTA_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_wool',
)

MAGENTA_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:magenta_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:magenta_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/magenta_wool_slab',
)

MAGENTA_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magenta_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magenta_wool_stairs',
)

MAGMA_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:magma_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/magma_block',
)

MANGROVE_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_button',
)

MANGROVE_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:mangrove_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:mangrove_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_door',
)

MANGROVE_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_fence',
)

MANGROVE_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_fence_gate',
)

MANGROVE_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_hanging_sign',
)

MANGROVE_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:mangrove_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            condition=LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                                type='minecraft:table_bonus',
                            ),
                            name='minecraft:stick',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_leaves',
)

MANGROVE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_log',
)

MANGROVE_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_planks',
)

MANGROVE_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_pressure_plate',
)

MANGROVE_PROPAGULE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_propagule', type='minecraft:item')],
            condition=LootConditionMatchBlock(
                blocks='minecraft:mangrove_propagule',
                state={'age': '4'},
                type='minecraft:match_block',
            ),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/mangrove_propagule',
)

MANGROVE_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_roots',
)

MANGROVE_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_shelf',
)

MANGROVE_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_sign',
)

MANGROVE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:mangrove_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:mangrove_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_slab',
)

MANGROVE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_stairs',
)

MANGROVE_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_trapdoor',
)

MANGROVE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mangrove_wood',
)

MEDIUM_AMETHYST_BUD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:medium_amethyst_bud', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/medium_amethyst_bud',
)

MELON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:melon',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=3, max=7),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(max=9), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:melon_slice',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/melon',
)

MELON_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '0'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.06666667, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '1'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.13333334, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '2'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.2, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '3'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.26666668, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '4'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.33333334, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '5'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.4, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '6'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.46666667, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:melon_stem',
                                state={'age': '7'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.53333336, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:melon_seeds',
                    type='minecraft:item',
                ),
            ],
            modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
        ),
    ],
    random_sequence='minecraft:blocks/melon_stem',
)

MOSSY_COBBLESTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_cobblestone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_cobblestone',
)

MOSSY_COBBLESTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:mossy_cobblestone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:mossy_cobblestone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mossy_cobblestone_slab',
)

MOSSY_COBBLESTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_cobblestone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_cobblestone_stairs',
)

MOSSY_COBBLESTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_cobblestone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_cobblestone_wall',
)

MOSSY_STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_stone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_stone_bricks',
)

MOSSY_STONE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:mossy_stone_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:mossy_stone_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mossy_stone_brick_slab',
)

MOSSY_STONE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_stone_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_stone_brick_stairs',
)

MOSSY_STONE_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mossy_stone_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mossy_stone_brick_wall',
)

MOSS_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:moss_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/moss_block',
)

MOSS_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:moss_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/moss_carpet',
)

MUD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mud', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mud',
)

MUDDY_MANGROVE_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:muddy_mangrove_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/muddy_mangrove_roots',
)

MUD_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mud_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mud_bricks',
)

MUD_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:mud_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:mud_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mud_brick_slab',
)

MUD_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mud_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mud_brick_stairs',
)

MUD_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mud_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/mud_brick_wall',
)

MUSHROOM_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mushroom_stem', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/mushroom_stem',
)

MYCELIUM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:mycelium',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dirt',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/mycelium',
)

NETHERITE_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:netherite_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/netherite_block',
)

NETHERRACK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:netherrack', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/netherrack',
)

NETHER_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_bricks',
)

NETHER_BRICK_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_brick_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_brick_fence',
)

NETHER_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:nether_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:nether_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/nether_brick_slab',
)

NETHER_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_brick_stairs',
)

NETHER_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_brick_wall',
)

NETHER_GOLD_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:nether_gold_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=6),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:gold_nugget',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/nether_gold_ore',
)

NETHER_PORTAL = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/nether_portal')

NETHER_QUARTZ_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:nether_quartz_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusOreDrops(
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:ore_drops',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:quartz',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/nether_quartz_ore',
)

NETHER_SPROUTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_sprouts', type='minecraft:item')],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/nether_sprouts',
)

NETHER_WART = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:nether_wart',
                                state={'age': '3'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=4),
                            type='minecraft:set_count',
                        ),
                        LootFunctionApplyBonusUniformBonusCount(
                            parameters=ParametersStruct2(bonusMultiplier=1),
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:nether_wart',
                                state={'age': '3'},
                                type='minecraft:match_block',
                            ),
                            type='minecraft:apply_bonus',
                            enchantment='minecraft:fortune',
                            formula='minecraft:uniform_bonus_count',
                        ),
                    ],
                    name='minecraft:nether_wart',
                    type='minecraft:item',
                ),
            ],
            modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_wart',
)

NETHER_WART_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:nether_wart_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/nether_wart_block',
)

NOTE_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:note_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/note_block',
)

OAK_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_button',
)

OAK_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:oak_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:oak_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_door',
)

OAK_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_fence',
)

OAK_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_fence_gate',
)

OAK_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_hanging_sign',
)

OAK_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:oak_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:oak_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionAllOf(
                        terms=[
                            LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.005, 0.0055555557, 0.00625, 0.008333334, 0.025],
                                type='minecraft:table_bonus',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    name='minecraft:apple',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/oak_leaves',
)

OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_log',
)

OAK_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_planks',
)

OAK_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_pressure_plate',
)

OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_sapling',
)

OAK_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_shelf',
)

OAK_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_sign',
)

OAK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:oak_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:oak_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/oak_slab',
)

OAK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_stairs',
)

OAK_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_trapdoor',
)

OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oak_wood',
)

OBSERVER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:observer', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/observer',
)

OBSIDIAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:obsidian', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/obsidian',
)

OCHRE_FROGLIGHT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:ochre_froglight', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/ochre_froglight',
)

OPEN_EYEBLOSSOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:open_eyeblossom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/open_eyeblossom',
)

ORANGE_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:orange_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_banner',
)

ORANGE_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:orange_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:orange_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_bed',
)

ORANGE_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:orange_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:orange_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:orange_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:orange_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/orange_candle',
)

ORANGE_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:orange_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/orange_candle_cake',
)

ORANGE_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_carpet',
)

ORANGE_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_concrete',
)

ORANGE_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_concrete_powder',
)

ORANGE_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:orange_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:orange_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/orange_concrete_slab',
)

ORANGE_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_concrete_stairs',
)

ORANGE_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_glazed_terracotta',
)

ORANGE_POPLAR_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:orange_poplar_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:poplar_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/orange_poplar_leaves',
)

ORANGE_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:orange_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/orange_shulker_box',
)

ORANGE_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/orange_stained_glass',
)

ORANGE_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/orange_stained_glass_pane',
)

ORANGE_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_terracotta',
)

ORANGE_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_tulip',
)

ORANGE_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_wool',
)

ORANGE_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:orange_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:orange_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/orange_wool_slab',
)

ORANGE_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/orange_wool_stairs',
)

OXEYE_DAISY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxeye_daisy', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxeye_daisy',
)

OXIDIZED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_chiseled_copper',
)

OXIDIZED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper',
)

OXIDIZED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_bars',
)

OXIDIZED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_bulb',
)

OXIDIZED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_chain',
)

OXIDIZED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:oxidized_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_chest',
)

OXIDIZED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:oxidized_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:oxidized_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_door',
)

OXIDIZED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:oxidized_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:oxidized_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_golem_statue',
)

OXIDIZED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_grate',
)

OXIDIZED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_lantern',
)

OXIDIZED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_copper_trapdoor',
)

OXIDIZED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_cut_copper',
)

OXIDIZED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:oxidized_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:oxidized_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_cut_copper_slab',
)

OXIDIZED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_cut_copper_stairs',
)

OXIDIZED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxidized_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/oxidized_lightning_rod',
)

PACKED_ICE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:packed_ice', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/packed_ice',
)

PACKED_MUD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:packed_mud', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/packed_mud',
)

PALE_HANGING_MOSS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_hanging_moss', type='minecraft:item')],
            condition=LootConditionAnyOf(
                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                type='minecraft:any_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/pale_hanging_moss',
)

PALE_MOSS_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_moss_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_moss_block',
)

PALE_MOSS_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:pale_moss_carpet',
                        state={'bottom': 'true'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:pale_moss_carpet',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pale_moss_carpet',
)

PALE_OAK_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_button',
)

PALE_OAK_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:pale_oak_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:pale_oak_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_door',
)

PALE_OAK_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_fence',
)

PALE_OAK_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_fence_gate',
)

PALE_OAK_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_hanging_sign',
)

PALE_OAK_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:pale_oak_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pale_oak_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_leaves',
)

PALE_OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_log',
)

PALE_OAK_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_planks',
)

PALE_OAK_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_pressure_plate',
)

PALE_OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_sapling',
)

PALE_OAK_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_shelf',
)

PALE_OAK_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_sign',
)

PALE_OAK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pale_oak_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:pale_oak_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_slab',
)

PALE_OAK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_stairs',
)

PALE_OAK_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_trapdoor',
)

PALE_OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pale_oak_wood',
)

PEARLESCENT_FROGLIGHT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pearlescent_froglight', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pearlescent_froglight',
)

PEONY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:peony',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:peony',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/peony',
)

PETRIFIED_OAK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:petrified_oak_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:petrified_oak_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/petrified_oak_slab',
)

PIGLIN_HEAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:piglin_head',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/piglin_head',
)

PINK_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:pink_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_banner',
)

PINK_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:pink_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:pink_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_bed',
)

PINK_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:pink_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pink_candle',
)

PINK_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:pink_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/pink_candle_cake',
)

PINK_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_carpet',
)

PINK_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_concrete',
)

PINK_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_concrete_powder',
)

PINK_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:pink_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pink_concrete_slab',
)

PINK_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_concrete_stairs',
)

PINK_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_glazed_terracotta',
)

PINK_PETALS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_petals',
                                state={'flower_amount': '1'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_petals',
                                state={'flower_amount': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_petals',
                                state={'flower_amount': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_petals',
                                state={'flower_amount': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:pink_petals',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pink_petals',
)

PINK_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:pink_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pink_shulker_box',
)

PINK_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/pink_stained_glass',
)

PINK_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/pink_stained_glass_pane',
)

PINK_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_terracotta',
)

PINK_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_tulip',
)

PINK_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_wool',
)

PINK_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pink_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:pink_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/pink_wool_slab',
)

PINK_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pink_wool_stairs',
)

PISTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:piston', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/piston',
)

PITCHER_CROP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'age': '0'},
                                        type='minecraft:match_block',
                                    ),
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'half': 'lower'},
                                        type='minecraft:match_block',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pitcher_pod',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'age': '1'},
                                        type='minecraft:match_block',
                                    ),
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'half': 'lower'},
                                        type='minecraft:match_block',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pitcher_pod',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'age': '2'},
                                        type='minecraft:match_block',
                                    ),
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'half': 'lower'},
                                        type='minecraft:match_block',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pitcher_pod',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'age': '3'},
                                        type='minecraft:match_block',
                                    ),
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'half': 'lower'},
                                        type='minecraft:match_block',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pitcher_pod',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'age': '4'},
                                        type='minecraft:match_block',
                                    ),
                                    LootConditionMatchBlock(
                                        blocks='minecraft:pitcher_crop',
                                        state={'half': 'lower'},
                                        type='minecraft:match_block',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:pitcher_plant',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/pitcher_crop',
)

PITCHER_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:pitcher_plant',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:pitcher_plant',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/pitcher_plant',
)

PLAYER_HEAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:profile', 'minecraft:note_block_sound', 'minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:player_head',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/player_head',
)

PODZOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:podzol',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dirt',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/podzol',
)

POINTED_DRIPSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pointed_dripstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pointed_dripstone',
)

POLISHED_ANDESITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_andesite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_andesite',
)

POLISHED_ANDESITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_andesite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_andesite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_andesite_slab',
)

POLISHED_ANDESITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_andesite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_andesite_stairs',
)

POLISHED_BASALT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_basalt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_basalt',
)

POLISHED_BLACKSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone',
)

POLISHED_BLACKSTONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_bricks',
)

POLISHED_BLACKSTONE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_blackstone_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_blackstone_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_brick_slab',
)

POLISHED_BLACKSTONE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_brick_stairs',
)

POLISHED_BLACKSTONE_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_brick_wall',
)

POLISHED_BLACKSTONE_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_button',
)

POLISHED_BLACKSTONE_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_pressure_plate',
)

POLISHED_BLACKSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_blackstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_blackstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_slab',
)

POLISHED_BLACKSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_stairs',
)

POLISHED_BLACKSTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_blackstone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_blackstone_wall',
)

POLISHED_CINNABAR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_cinnabar', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_cinnabar',
)

POLISHED_CINNABAR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_cinnabar_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_cinnabar_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_cinnabar_slab',
)

POLISHED_CINNABAR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_cinnabar_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_cinnabar_stairs',
)

POLISHED_CINNABAR_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_cinnabar_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_cinnabar_wall',
)

POLISHED_DEEPSLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_deepslate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_deepslate',
)

POLISHED_DEEPSLATE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_deepslate_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_deepslate_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_deepslate_slab',
)

POLISHED_DEEPSLATE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_deepslate_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_deepslate_stairs',
)

POLISHED_DEEPSLATE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_deepslate_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_deepslate_wall',
)

POLISHED_DIORITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_diorite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_diorite',
)

POLISHED_DIORITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_diorite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_diorite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_diorite_slab',
)

POLISHED_DIORITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_diorite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_diorite_stairs',
)

POLISHED_GRANITE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_granite', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_granite',
)

POLISHED_GRANITE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_granite_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_granite_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_granite_slab',
)

POLISHED_GRANITE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_granite_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_granite_stairs',
)

POLISHED_SULFUR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_sulfur', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_sulfur',
)

POLISHED_SULFUR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_sulfur_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_sulfur_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_sulfur_slab',
)

POLISHED_SULFUR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_sulfur_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_sulfur_stairs',
)

POLISHED_SULFUR_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_sulfur_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_sulfur_wall',
)

POLISHED_TUFF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_tuff', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_tuff',
)

POLISHED_TUFF_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:polished_tuff_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:polished_tuff_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/polished_tuff_slab',
)

POLISHED_TUFF_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_tuff_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_tuff_stairs',
)

POLISHED_TUFF_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:polished_tuff_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/polished_tuff_wall',
)

POPLAR_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_button',
)

POPLAR_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:poplar_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:poplar_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_door',
)

POPLAR_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_fence',
)

POPLAR_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_fence_gate',
)

POPLAR_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_hanging_sign',
)

POPLAR_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_log',
)

POPLAR_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_planks',
)

POPLAR_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_pressure_plate',
)

POPLAR_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_sapling',
)

POPLAR_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_shelf',
)

POPLAR_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_sign',
)

POPLAR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:poplar_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:poplar_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/poplar_slab',
)

POPLAR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_stairs',
)

POPLAR_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_trapdoor',
)

POPLAR_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poplar_wood',
)

POPPY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poppy', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/poppy',
)

POTATOES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:potato', type='minecraft:item')]),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionApplyBonusBinomialWithBonusCount(
                        parameters=ParametersStruct(extra=3, probability=0.5714286),
                        type='minecraft:apply_bonus',
                        enchantment='minecraft:fortune',
                        formula='minecraft:binomial_with_bonus_count',
                    ),
                    name='minecraft:potato',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionMatchBlock(blocks='minecraft:potatoes', state={'age': '7'}, type='minecraft:match_block'),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionRandomChance(chance=0.02, type='minecraft:random_chance'),
                    name='minecraft:poisonous_potato',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionMatchBlock(blocks='minecraft:potatoes', state={'age': '7'}, type='minecraft:match_block'),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/potatoes',
)

POTENT_SULFUR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:potent_sulfur', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potent_sulfur',
)

POTTED_ACACIA_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:acacia_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_acacia_sapling',
)

POTTED_ALLIUM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:allium', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_allium',
)

POTTED_AZALEA_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:azalea', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_azalea_bush',
)

POTTED_AZURE_BLUET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:azure_bluet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_azure_bluet',
)

POTTED_BAMBOO = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:bamboo', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_bamboo',
)

POTTED_BIRCH_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:birch_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_birch_sapling',
)

POTTED_BLUE_ORCHID = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:blue_orchid', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_blue_orchid',
)

POTTED_BROWN_MUSHROOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:brown_mushroom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_brown_mushroom',
)

POTTED_CACTUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cactus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_cactus',
)

POTTED_CHERRY_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cherry_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_cherry_sapling',
)

POTTED_CLOSED_EYEBLOSSOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:closed_eyeblossom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_closed_eyeblossom',
)

POTTED_CORNFLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cornflower', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_cornflower',
)

POTTED_CRIMSON_FUNGUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_fungus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_crimson_fungus',
)

POTTED_CRIMSON_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:crimson_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_crimson_roots',
)

POTTED_DANDELION = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dandelion', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_dandelion',
)

POTTED_DARK_OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dark_oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_dark_oak_sapling',
)

POTTED_DEAD_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:dead_bush', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_dead_bush',
)

POTTED_FERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:fern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_fern',
)

POTTED_FLOWERING_AZALEA_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flowering_azalea', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_flowering_azalea_bush',
)

POTTED_GOLDEN_DANDELION = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:golden_dandelion', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_golden_dandelion',
)

POTTED_JUNGLE_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:jungle_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_jungle_sapling',
)

POTTED_LILY_OF_THE_VALLEY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:lily_of_the_valley', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_lily_of_the_valley',
)

POTTED_MANGROVE_PROPAGULE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:mangrove_propagule', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_mangrove_propagule',
)

POTTED_OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_oak_sapling',
)

POTTED_OPEN_EYEBLOSSOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:open_eyeblossom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_open_eyeblossom',
)

POTTED_ORANGE_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:orange_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_orange_tulip',
)

POTTED_OXEYE_DAISY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:oxeye_daisy', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_oxeye_daisy',
)

POTTED_PALE_OAK_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pale_oak_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_pale_oak_sapling',
)

POTTED_PINK_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pink_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_pink_tulip',
)

POTTED_POPLAR_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poplar_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_poplar_sapling',
)

POTTED_POPPY = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:poppy', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_poppy',
)

POTTED_RED_MUSHROOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_mushroom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_red_mushroom',
)

POTTED_RED_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_red_tulip',
)

POTTED_SPRUCE_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_spruce_sapling',
)

POTTED_TORCHFLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:torchflower', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_torchflower',
)

POTTED_WARPED_FUNGUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_fungus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_warped_fungus',
)

POTTED_WARPED_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_warped_roots',
)

POTTED_WHITE_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_white_tulip',
)

POTTED_WITHER_ROSE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:flower_pot', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:wither_rose', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/potted_wither_rose',
)

POWDER_SNOW = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/powder_snow')

POWDER_SNOW_CAULDRON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cauldron', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/powder_snow_cauldron',
)

POWERED_RAIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:powered_rail', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/powered_rail',
)

PRISMARINE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:prismarine', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/prismarine',
)

PRISMARINE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:prismarine_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_bricks',
)

PRISMARINE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:prismarine_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:prismarine_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_brick_slab',
)

PRISMARINE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:prismarine_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_brick_stairs',
)

PRISMARINE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:prismarine_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:prismarine_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_slab',
)

PRISMARINE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:prismarine_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_stairs',
)

PRISMARINE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:prismarine_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/prismarine_wall',
)

PUMPKIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:pumpkin', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/pumpkin',
)

PUMPKIN_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '0'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.06666667, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '1'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.13333334, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '2'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.2, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '3'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.26666668, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '4'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.33333334, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '5'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.4, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '6'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.46666667, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:pumpkin_stem',
                                state={'age': '7'},
                                type='minecraft:match_block',
                            ),
                            count=ContextIntProviderStructBinomial(n=3, p=0.53333336, type='minecraft:binomial'),
                            type='minecraft:set_count',
                        ),
                    ],
                    name='minecraft:pumpkin_seeds',
                    type='minecraft:item',
                ),
            ],
            modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
        ),
    ],
    random_sequence='minecraft:blocks/pumpkin_stem',
)

PURPLE_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:purple_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_banner',
)

PURPLE_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:purple_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:purple_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_bed',
)

PURPLE_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purple_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purple_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purple_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:purple_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/purple_candle',
)

PURPLE_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:purple_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/purple_candle_cake',
)

PURPLE_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_carpet',
)

PURPLE_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_concrete',
)

PURPLE_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_concrete_powder',
)

PURPLE_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purple_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:purple_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/purple_concrete_slab',
)

PURPLE_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_concrete_stairs',
)

PURPLE_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_glazed_terracotta',
)

PURPLE_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:purple_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/purple_shulker_box',
)

PURPLE_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/purple_stained_glass',
)

PURPLE_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/purple_stained_glass_pane',
)

PURPLE_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_terracotta',
)

PURPLE_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_wool',
)

PURPLE_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purple_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:purple_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/purple_wool_slab',
)

PURPLE_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purple_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purple_wool_stairs',
)

PURPUR_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purpur_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purpur_block',
)

PURPUR_PILLAR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purpur_pillar', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purpur_pillar',
)

PURPUR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:purpur_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:purpur_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/purpur_slab',
)

PURPUR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:purpur_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/purpur_stairs',
)

QUARTZ_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:quartz_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/quartz_block',
)

QUARTZ_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:quartz_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/quartz_bricks',
)

QUARTZ_PILLAR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:quartz_pillar', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/quartz_pillar',
)

QUARTZ_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:quartz_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:quartz_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/quartz_slab',
)

QUARTZ_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:quartz_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/quartz_stairs',
)

RAIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:rail', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/rail',
)

RAW_COPPER_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:raw_copper_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/raw_copper_block',
)

RAW_GOLD_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:raw_gold_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/raw_gold_block',
)

RAW_IRON_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:raw_iron_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/raw_iron_block',
)

REDSTONE_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:redstone_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/redstone_block',
)

REDSTONE_LAMP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:redstone_lamp', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/redstone_lamp',
)

REDSTONE_ORE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:redstone_ore',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=4, max=5),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:redstone',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/redstone_ore',
)

REDSTONE_TORCH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:redstone_torch', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/redstone_torch',
)

REDSTONE_WIRE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:redstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/redstone_wire',
)

RED_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:red_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_banner',
)

RED_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:red_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:red_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_bed',
)

RED_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:red_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_candle',
)

RED_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:red_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/red_candle_cake',
)

RED_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_carpet',
)

RED_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_concrete',
)

RED_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_concrete_powder',
)

RED_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:red_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_concrete_slab',
)

RED_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_concrete_stairs',
)

RED_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_glazed_terracotta',
)

RED_MUSHROOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_mushroom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_mushroom',
)

RED_MUSHROOM_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:red_mushroom_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=-6, max=2),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(min=0), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:red_mushroom',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_mushroom_block',
)

RED_NETHER_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_nether_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_nether_bricks',
)

RED_NETHER_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_nether_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:red_nether_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_nether_brick_slab',
)

RED_NETHER_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_nether_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_nether_brick_stairs',
)

RED_NETHER_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_nether_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_nether_brick_wall',
)

RED_POPLAR_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:red_poplar_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:poplar_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/red_poplar_leaves',
)

RED_SAND = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_sand', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_sand',
)

RED_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_sandstone',
)

RED_SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:red_sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_sandstone_slab',
)

RED_SANDSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_sandstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_sandstone_stairs',
)

RED_SANDSTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_sandstone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_sandstone_wall',
)

RED_SHRUB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_shrub', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_shrub',
)

RED_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:red_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_shulker_box',
)

RED_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/red_stained_glass',
)

RED_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/red_stained_glass_pane',
)

RED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_terracotta',
)

RED_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_tulip',
)

RED_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_wool',
)

RED_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:red_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:red_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/red_wool_slab',
)

RED_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:red_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/red_wool_stairs',
)

REINFORCED_DEEPSLATE = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/reinforced_deepslate')

REPEATER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:repeater', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/repeater',
)

RESIN_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:resin_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/resin_block',
)

RESIN_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:resin_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/resin_bricks',
)

RESIN_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:resin_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/resin_brick_slab',
)

RESIN_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:resin_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/resin_brick_stairs',
)

RESIN_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:resin_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/resin_brick_wall',
)

RESIN_CLUMP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'down': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'up': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'north': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'south': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'west': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:resin_clump',
                                state={'east': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(count=-1, add=True, type='minecraft:set_count'),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:resin_clump',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/resin_clump',
)

RESPAWN_ANCHOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:respawn_anchor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/respawn_anchor',
)

ROOTED_DIRT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:rooted_dirt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/rooted_dirt',
)

ROSE_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:rose_bush',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:rose_bush',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/rose_bush',
)

SAND = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sand', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sand',
)

SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sandstone',
)

SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sandstone_slab',
)

SANDSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sandstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sandstone_stairs',
)

SANDSTONE_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sandstone_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sandstone_wall',
)

SCAFFOLDING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:scaffolding', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/scaffolding',
)

SCULK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sculk', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/sculk',
)

SCULK_CATALYST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sculk_catalyst', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/sculk_catalyst',
)

SCULK_SENSOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sculk_sensor', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/sculk_sensor',
)

SCULK_SHRIEKER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sculk_shrieker', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/sculk_shrieker',
)

SCULK_VEIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'down': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'up': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'north': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'south': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'west': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sculk_vein',
                                state={'east': 'true'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            add=True,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(count=-1, add=True, type='minecraft:set_count'),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition='minecraft:tool/can_silk_touch',
                    name='minecraft:sculk_vein',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sculk_vein',
)

SEAGRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:seagrass', type='minecraft:item')],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/seagrass',
)

SEA_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:sea_lantern',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(
                                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                                    type='minecraft:set_count',
                                ),
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=1),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionLimitCount(limit=LimitStruct(min=1, max=5), type='minecraft:limit_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:prismarine_crystals',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sea_lantern',
)

SEA_PICKLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sea_pickle',
                                state={'pickles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sea_pickle',
                                state={'pickles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sea_pickle',
                                state={'pickles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:sea_pickle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sea_pickle',
)

SHELF_MUSHROOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:shelf_mushroom',
                                state={'age': '1'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:shelf_mushroom',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/shelf_mushroom',
)

SHORT_DRY_GRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:short_dry_grass', type='minecraft:item')],
            condition=LootConditionAnyOf(
                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                type='minecraft:any_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/short_dry_grass',
)

SHORT_GRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_shear',
                            name='minecraft:short_grass',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionApplyBonusUniformBonusCount(
                                    parameters=ParametersStruct2(bonusMultiplier=2),
                                    type='minecraft:apply_bonus',
                                    enchantment='minecraft:fortune',
                                    formula='minecraft:uniform_bonus_count',
                                ),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            condition=LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/short_grass',
)

SHROOMLIGHT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:shroomlight', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/shroomlight',
)

SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/shulker_box',
)

SKELETON_SKULL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:skeleton_skull',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/skeleton_skull',
)

SLIME_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:slime_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/slime_block',
)

SMALL_AMETHYST_BUD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:small_amethyst_bud', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/small_amethyst_bud',
)

SMALL_DRIPLEAF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:small_dripleaf', type='minecraft:item')],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/small_dripleaf',
)

SMITHING_TABLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smithing_table', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smithing_table',
)

SMOKER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:smoker',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smoker',
)

SMOOTH_BASALT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_basalt', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_basalt',
)

SMOOTH_QUARTZ = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_quartz', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_quartz',
)

SMOOTH_QUARTZ_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:smooth_quartz_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:smooth_quartz_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/smooth_quartz_slab',
)

SMOOTH_QUARTZ_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_quartz_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_quartz_stairs',
)

SMOOTH_RED_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_red_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_red_sandstone',
)

SMOOTH_RED_SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:smooth_red_sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:smooth_red_sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/smooth_red_sandstone_slab',
)

SMOOTH_RED_SANDSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_red_sandstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_red_sandstone_stairs',
)

SMOOTH_SANDSTONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_sandstone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_sandstone',
)

SMOOTH_SANDSTONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:smooth_sandstone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:smooth_sandstone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/smooth_sandstone_slab',
)

SMOOTH_SANDSTONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_sandstone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_sandstone_stairs',
)

SMOOTH_STONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:smooth_stone', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/smooth_stone',
)

SMOOTH_STONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:smooth_stone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:smooth_stone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/smooth_stone_slab',
)

SNIFFER_EGG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sniffer_egg', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sniffer_egg',
)

SNOW = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryAlternatives(
                            condition=LootConditionInverted(term='minecraft:tool/can_silk_touch', type='minecraft:inverted'),
                            children=[
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '1'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '2'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=3, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '3'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=4, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '4'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=5, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '5'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=6, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '6'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=7, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '7'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=8, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '8'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snowball',
                                    type='minecraft:item',
                                ),
                            ],
                            type='minecraft:alternatives',
                        ),
                        LootPoolEntryAlternatives(
                            children=[
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '1'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '2'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=3, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '3'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=4, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '4'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=5, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '5'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=6, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '6'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(
                                    modifier=LootFunctionSetCount(count=7, type='minecraft:set_count'),
                                    condition=LootConditionMatchBlock(
                                        blocks='minecraft:snow',
                                        state={'layers': '7'},
                                        type='minecraft:match_block',
                                    ),
                                    name='minecraft:snow',
                                    type='minecraft:item',
                                ),
                                LootPoolEntryItem(name='minecraft:snow_block', type='minecraft:item'),
                            ],
                            type='minecraft:alternatives',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
            condition=LootConditionEntityProperties(
                entity=EntityTarget.THIS,
                predicate=EntitySubPredicateMap(),
                type='minecraft:entity_properties',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/snow',
)

SNOW_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:snow_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=[
                                LootFunctionSetCount(count=4, type='minecraft:set_count'),
                                LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                            ],
                            name='minecraft:snowball',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/snow_block',
)

SOUL_CAMPFIRE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:soul_campfire',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=1, type='minecraft:set_count'),
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:soul_soil',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/soul_campfire',
)

SOUL_FIRE = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/soul_fire')

SOUL_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:soul_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/soul_lantern',
)

SOUL_SAND = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:soul_sand', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/soul_sand',
)

SOUL_SOIL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:soul_soil', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/soul_soil',
)

SOUL_TORCH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:soul_torch', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/soul_torch',
)

SPAWNER = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/spawner')

SPONGE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sponge', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sponge',
)

SPORE_BLOSSOM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spore_blossom', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spore_blossom',
)

SPRUCE_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_button',
)

SPRUCE_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:spruce_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:spruce_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_door',
)

SPRUCE_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_fence',
)

SPRUCE_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_fence_gate',
)

SPRUCE_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_hanging_sign',
)

SPRUCE_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:spruce_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:spruce_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_leaves',
)

SPRUCE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_log',
)

SPRUCE_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_planks',
)

SPRUCE_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_pressure_plate',
)

SPRUCE_SAPLING = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_sapling', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_sapling',
)

SPRUCE_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_shelf',
)

SPRUCE_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_sign',
)

SPRUCE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:spruce_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:spruce_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/spruce_slab',
)

SPRUCE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_stairs',
)

SPRUCE_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_trapdoor',
)

SPRUCE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:spruce_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/spruce_wood',
)

STICKY_PISTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sticky_piston', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sticky_piston',
)

STONE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:stone',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:cobblestone',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/stone',
)

STONECUTTER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stonecutter', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stonecutter',
)

STONE_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_bricks',
)

STONE_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:stone_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:stone_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/stone_brick_slab',
)

STONE_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_brick_stairs',
)

STONE_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_brick_wall',
)

STONE_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_button',
)

STONE_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_pressure_plate',
)

STONE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:stone_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:stone_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/stone_slab',
)

STONE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stone_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stone_stairs',
)

STRAW_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:straw_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:straw_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/straw_bed',
)

STRIPPED_ACACIA_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_acacia_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_acacia_log',
)

STRIPPED_ACACIA_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_acacia_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_acacia_wood',
)

STRIPPED_BAMBOO_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_bamboo_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_bamboo_block',
)

STRIPPED_BIRCH_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_birch_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_birch_log',
)

STRIPPED_BIRCH_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_birch_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_birch_wood',
)

STRIPPED_CHERRY_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_cherry_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_cherry_log',
)

STRIPPED_CHERRY_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_cherry_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_cherry_wood',
)

STRIPPED_CRIMSON_HYPHAE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_crimson_hyphae', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_crimson_hyphae',
)

STRIPPED_CRIMSON_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_crimson_stem', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_crimson_stem',
)

STRIPPED_DARK_OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_dark_oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_dark_oak_log',
)

STRIPPED_DARK_OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_dark_oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_dark_oak_wood',
)

STRIPPED_JUNGLE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_jungle_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_jungle_log',
)

STRIPPED_JUNGLE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_jungle_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_jungle_wood',
)

STRIPPED_MANGROVE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_mangrove_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_mangrove_log',
)

STRIPPED_MANGROVE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_mangrove_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_mangrove_wood',
)

STRIPPED_OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_oak_log',
)

STRIPPED_OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_oak_wood',
)

STRIPPED_PALE_OAK_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_pale_oak_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_pale_oak_log',
)

STRIPPED_PALE_OAK_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_pale_oak_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_pale_oak_wood',
)

STRIPPED_POPLAR_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_poplar_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_poplar_log',
)

STRIPPED_POPLAR_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_poplar_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_poplar_wood',
)

STRIPPED_SPRUCE_LOG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_spruce_log', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_spruce_log',
)

STRIPPED_SPRUCE_WOOD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_spruce_wood', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_spruce_wood',
)

STRIPPED_WARPED_HYPHAE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_warped_hyphae', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_warped_hyphae',
)

STRIPPED_WARPED_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:stripped_warped_stem', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/stripped_warped_stem',
)

SUGAR_CANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sugar_cane', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sugar_cane',
)

SULFUR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur',
)

SULFUR_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_bricks',
)

SULFUR_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sulfur_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:sulfur_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_brick_slab',
)

SULFUR_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_brick_stairs',
)

SULFUR_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_brick_wall',
)

SULFUR_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:sulfur_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:sulfur_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_slab',
)

SULFUR_SPIKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_spike', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_spike',
)

SULFUR_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_stairs',
)

SULFUR_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sulfur_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sulfur_wall',
)

SUNFLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:sunflower',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:sunflower',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/sunflower',
)

SUSPICIOUS_GRAVEL = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/suspicious_gravel')

SUSPICIOUS_SAND = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/suspicious_sand')

SWEET_BERRY_BUSH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sweet_berries', type='minecraft:item')],
            modifier=[
                LootFunctionSetCount(
                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=2, max=3),
                    type='minecraft:set_count',
                ),
                LootFunctionApplyBonusUniformBonusCount(
                    parameters=ParametersStruct2(bonusMultiplier=1),
                    type='minecraft:apply_bonus',
                    enchantment='minecraft:fortune',
                    formula='minecraft:uniform_bonus_count',
                ),
            ],
            condition=LootConditionMatchBlock(
                blocks='minecraft:sweet_berry_bush',
                state={'age': '3'},
                type='minecraft:match_block',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:sweet_berries', type='minecraft:item')],
            modifier=[
                LootFunctionSetCount(
                    count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                    type='minecraft:set_count',
                ),
                LootFunctionApplyBonusUniformBonusCount(
                    parameters=ParametersStruct2(bonusMultiplier=1),
                    type='minecraft:apply_bonus',
                    enchantment='minecraft:fortune',
                    formula='minecraft:uniform_bonus_count',
                ),
            ],
            condition=LootConditionMatchBlock(
                blocks='minecraft:sweet_berry_bush',
                state={'age': '2'},
                type='minecraft:match_block',
            ),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/sweet_berry_bush',
)

TALL_DRY_GRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tall_dry_grass', type='minecraft:item')],
            condition=LootConditionAnyOf(
                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                type='minecraft:any_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/tall_dry_grass',
)

TALL_GRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                            condition='minecraft:tool/can_shear',
                            name='minecraft:short_grass',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionMatchBlock(
                        blocks='minecraft:tall_grass',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    LootConditionLocationCheck(
                        offsetY=1,
                        predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:tall_grass', state={'half': 'upper'})),
                        type='minecraft:location_check',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                            condition='minecraft:tool/can_shear',
                            name='minecraft:short_grass',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionRandomChance(chance=0.125, type='minecraft:random_chance'),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:wheat_seeds',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
            condition=LootConditionAllOf(
                terms=[
                    LootConditionMatchBlock(
                        blocks='minecraft:tall_grass',
                        state={'half': 'upper'},
                        type='minecraft:match_block',
                    ),
                    LootConditionLocationCheck(
                        offsetY=-1,
                        predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:tall_grass', state={'half': 'lower'})),
                        type='minecraft:location_check',
                    ),
                ],
                type='minecraft:all_of',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/tall_grass',
)

TALL_SEAGRASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionSetCount(count=2, type='minecraft:set_count'),
                    name='minecraft:seagrass',
                    type='minecraft:item',
                ),
            ],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/tall_seagrass',
)

TARGET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:target', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/target',
)

TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/terracotta',
)

TINTED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tinted_glass', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tinted_glass',
)

TNT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:tnt',
                        state={'unstable': 'false'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:tnt',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tnt',
)

TORCH = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:torch', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/torch',
)

TORCHFLOWER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:torchflower', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/torchflower',
)

TORCHFLOWER_CROP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:torchflower_seeds', type='minecraft:item')])],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/torchflower_crop',
)

TRAPPED_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:trapped_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/trapped_chest',
)

TRIAL_SPAWNER = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/trial_spawner')

TRIPWIRE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:string', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tripwire',
)

TRIPWIRE_HOOK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tripwire_hook', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tripwire_hook',
)

TUBE_CORAL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tube_coral', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/tube_coral',
)

TUBE_CORAL_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:tube_coral_block',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:dead_tube_coral_block',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/tube_coral_block',
)

TUBE_CORAL_FAN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tube_coral_fan', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/tube_coral_fan',
)

TUFF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff',
)

TUFF_BRICKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff_bricks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff_bricks',
)

TUFF_BRICK_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:tuff_brick_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:tuff_brick_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/tuff_brick_slab',
)

TUFF_BRICK_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff_brick_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff_brick_stairs',
)

TUFF_BRICK_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff_brick_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff_brick_wall',
)

TUFF_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:tuff_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:tuff_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/tuff_slab',
)

TUFF_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff_stairs',
)

TUFF_WALL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:tuff_wall', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/tuff_wall',
)

TURTLE_EGG = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:turtle_egg', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/turtle_egg',
)

TWISTING_VINES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:twisting_vines',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.33, 0.55, 0.77, 1.0],
                                type='minecraft:table_bonus',
                            ),
                            name='minecraft:twisting_vines',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/twisting_vines',
)

TWISTING_VINES_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:twisting_vines',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.33, 0.55, 0.77, 1.0],
                                type='minecraft:table_bonus',
                            ),
                            name='minecraft:twisting_vines',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/twisting_vines_plant',
)

VAULT = LootTable(type=LootContextParamSets.BLOCK, random_sequence='minecraft:blocks/vault')

VERDANT_FROGLIGHT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:verdant_froglight', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/verdant_froglight',
)

VINE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:vine', type='minecraft:item')],
            condition='minecraft:tool/can_shear',
        ),
    ],
    random_sequence='minecraft:blocks/vine',
)

WARPED_BUTTON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_button', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_button',
)

WARPED_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:warped_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:warped_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_door',
)

WARPED_FENCE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_fence', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_fence',
)

WARPED_FENCE_GATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_fence_gate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_fence_gate',
)

WARPED_FUNGUS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_fungus', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_fungus',
)

WARPED_HANGING_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_hanging_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_hanging_sign',
)

WARPED_HYPHAE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_hyphae', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_hyphae',
)

WARPED_NYLIUM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition='minecraft:tool/can_silk_touch',
                            name='minecraft:warped_nylium',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                            name='minecraft:netherrack',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/warped_nylium',
)

WARPED_PLANKS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_planks', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_planks',
)

WARPED_PRESSURE_PLATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_pressure_plate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_pressure_plate',
)

WARPED_ROOTS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_roots', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_roots',
)

WARPED_SHELF = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_shelf', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_shelf',
)

WARPED_SIGN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_sign', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_sign',
)

WARPED_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:warped_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:warped_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/warped_slab',
)

WARPED_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_stairs',
)

WARPED_STEM = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_stem', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_stem',
)

WARPED_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_trapdoor',
)

WARPED_WART_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:warped_wart_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/warped_wart_block',
)

WATER_CAULDRON = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:cauldron', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/water_cauldron',
)

WAXED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_chiseled_copper',
)

WAXED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_bars',
)

WAXED_COPPER_BLOCK = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_block', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_block',
)

WAXED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_bulb',
)

WAXED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_chain',
)

WAXED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:waxed_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_chest',
)

WAXED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:waxed_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:waxed_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_door',
)

WAXED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:waxed_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:waxed_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_golem_statue',
)

WAXED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_grate',
)

WAXED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_lantern',
)

WAXED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_copper_trapdoor',
)

WAXED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_cut_copper',
)

WAXED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:waxed_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:waxed_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/waxed_cut_copper_slab',
)

WAXED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_cut_copper_stairs',
)

WAXED_EXPOSED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_chiseled_copper',
)

WAXED_EXPOSED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper',
)

WAXED_EXPOSED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_bars',
)

WAXED_EXPOSED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_bulb',
)

WAXED_EXPOSED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_chain',
)

WAXED_EXPOSED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:waxed_exposed_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_chest',
)

WAXED_EXPOSED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:waxed_exposed_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:waxed_exposed_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_door',
)

WAXED_EXPOSED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:waxed_exposed_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:waxed_exposed_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_golem_statue',
)

WAXED_EXPOSED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_grate',
)

WAXED_EXPOSED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_lantern',
)

WAXED_EXPOSED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_copper_trapdoor',
)

WAXED_EXPOSED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_cut_copper',
)

WAXED_EXPOSED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:waxed_exposed_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:waxed_exposed_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_cut_copper_slab',
)

WAXED_EXPOSED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_cut_copper_stairs',
)

WAXED_EXPOSED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_exposed_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_exposed_lightning_rod',
)

WAXED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_lightning_rod',
)

WAXED_OXIDIZED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_chiseled_copper',
)

WAXED_OXIDIZED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper',
)

WAXED_OXIDIZED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_bars',
)

WAXED_OXIDIZED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_bulb',
)

WAXED_OXIDIZED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_chain',
)

WAXED_OXIDIZED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:waxed_oxidized_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_chest',
)

WAXED_OXIDIZED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:waxed_oxidized_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:waxed_oxidized_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_door',
)

WAXED_OXIDIZED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:waxed_oxidized_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:waxed_oxidized_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_golem_statue',
)

WAXED_OXIDIZED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_grate',
)

WAXED_OXIDIZED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_lantern',
)

WAXED_OXIDIZED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_copper_trapdoor',
)

WAXED_OXIDIZED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_cut_copper',
)

WAXED_OXIDIZED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:waxed_oxidized_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:waxed_oxidized_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_cut_copper_slab',
)

WAXED_OXIDIZED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_cut_copper_stairs',
)

WAXED_OXIDIZED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_oxidized_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_oxidized_lightning_rod',
)

WAXED_WEATHERED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_chiseled_copper',
)

WAXED_WEATHERED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper',
)

WAXED_WEATHERED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_bars',
)

WAXED_WEATHERED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_bulb',
)

WAXED_WEATHERED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_chain',
)

WAXED_WEATHERED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:waxed_weathered_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_chest',
)

WAXED_WEATHERED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:waxed_weathered_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:waxed_weathered_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_door',
)

WAXED_WEATHERED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:waxed_weathered_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:waxed_weathered_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_golem_statue',
)

WAXED_WEATHERED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_grate',
)

WAXED_WEATHERED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_lantern',
)

WAXED_WEATHERED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_copper_trapdoor',
)

WAXED_WEATHERED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_cut_copper',
)

WAXED_WEATHERED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:waxed_weathered_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:waxed_weathered_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_cut_copper_slab',
)

WAXED_WEATHERED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_cut_copper_stairs',
)

WAXED_WEATHERED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:waxed_weathered_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/waxed_weathered_lightning_rod',
)

WEATHERED_CHISELED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_chiseled_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_chiseled_copper',
)

WEATHERED_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper',
)

WEATHERED_COPPER_BARS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_bars', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_bars',
)

WEATHERED_COPPER_BULB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_bulb', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_bulb',
)

WEATHERED_COPPER_CHAIN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_chain', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_chain',
)

WEATHERED_COPPER_CHEST = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:weathered_copper_chest',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_chest',
)

WEATHERED_COPPER_DOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:weathered_copper_door',
                        state={'half': 'lower'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:weathered_copper_door',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_door',
)

WEATHERED_COPPER_GOLEM_STATUE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionCopyComponents(
                            source='block_entity',
                            include=['minecraft:custom_name'],
                            type='minecraft:copy_components',
                        ),
                        LootFunctionCopyState(
                            block='minecraft:weathered_copper_golem_statue',
                            properties=['copper_golem_pose'],
                            type='minecraft:copy_state',
                        ),
                    ],
                    name='minecraft:weathered_copper_golem_statue',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_golem_statue',
)

WEATHERED_COPPER_GRATE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_grate', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_grate',
)

WEATHERED_COPPER_LANTERN = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_lantern', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_lantern',
)

WEATHERED_COPPER_TRAPDOOR = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_copper_trapdoor', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_copper_trapdoor',
)

WEATHERED_CUT_COPPER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_cut_copper', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_cut_copper',
)

WEATHERED_CUT_COPPER_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:weathered_cut_copper_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:weathered_cut_copper_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/weathered_cut_copper_slab',
)

WEATHERED_CUT_COPPER_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_cut_copper_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_cut_copper_stairs',
)

WEATHERED_LIGHTNING_ROD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:weathered_lightning_rod', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/weathered_lightning_rod',
)

WEEPING_VINES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:weeping_vines',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.33, 0.55, 0.77, 1.0],
                                type='minecraft:table_bonus',
                            ),
                            name='minecraft:weeping_vines',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/weeping_vines',
)

WEEPING_VINES_PLANT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:weeping_vines',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionTableBonus(
                                enchantment='minecraft:fortune',
                                chances=[0.33, 0.55, 0.77, 1.0],
                                type='minecraft:table_bonus',
                            ),
                            name='minecraft:weeping_vines',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/weeping_vines_plant',
)

WET_SPONGE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:wet_sponge', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/wet_sponge',
)

WHEAT = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:wheat',
                                state={'age': '7'},
                                type='minecraft:match_block',
                            ),
                            name='minecraft:wheat',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(name='minecraft:wheat_seeds', type='minecraft:item'),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionApplyBonusBinomialWithBonusCount(
                        parameters=ParametersStruct(extra=3, probability=0.5714286),
                        type='minecraft:apply_bonus',
                        enchantment='minecraft:fortune',
                        formula='minecraft:binomial_with_bonus_count',
                    ),
                    name='minecraft:wheat_seeds',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionMatchBlock(blocks='minecraft:wheat', state={'age': '7'}, type='minecraft:match_block'),
        ),
    ],
    modifier=LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
    random_sequence='minecraft:blocks/wheat',
)

WHITE_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:white_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_banner',
)

WHITE_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:white_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:white_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_bed',
)

WHITE_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:white_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:white_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:white_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:white_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/white_candle',
)

WHITE_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:white_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/white_candle_cake',
)

WHITE_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_carpet',
)

WHITE_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_concrete',
)

WHITE_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_concrete_powder',
)

WHITE_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:white_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:white_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/white_concrete_slab',
)

WHITE_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_concrete_stairs',
)

WHITE_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_glazed_terracotta',
)

WHITE_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:white_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/white_shulker_box',
)

WHITE_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/white_stained_glass',
)

WHITE_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/white_stained_glass_pane',
)

WHITE_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_terracotta',
)

WHITE_TULIP = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_tulip', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_tulip',
)

WHITE_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_wool',
)

WHITE_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:white_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:white_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/white_wool_slab',
)

WHITE_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:white_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/white_wool_stairs',
)

WILDFLOWERS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:wildflowers',
                                state={'flower_amount': '1'},
                                type='minecraft:match_block',
                            ),
                            count=1,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:wildflowers',
                                state={'flower_amount': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:wildflowers',
                                state={'flower_amount': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:wildflowers',
                                state={'flower_amount': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:wildflowers',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/wildflowers',
)

WITHER_ROSE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:wither_rose', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/wither_rose',
)

WITHER_SKELETON_SKULL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:wither_skeleton_skull',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/wither_skeleton_skull',
)

YELLOW_BANNER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=[
                            'minecraft:custom_name',
                            'minecraft:item_name',
                            'minecraft:tooltip_display',
                            'minecraft:banner_patterns',
                            'minecraft:rarity',
                        ],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:yellow_banner',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_banner',
)

YELLOW_BED = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    condition=LootConditionMatchBlock(
                        blocks='minecraft:yellow_bed',
                        state={'part': 'head'},
                        type='minecraft:match_block',
                    ),
                    name='minecraft:yellow_bed',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_bed',
)

YELLOW_CANDLE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:yellow_candle',
                                state={'candles': '2'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:yellow_candle',
                                state={'candles': '3'},
                                type='minecraft:match_block',
                            ),
                            count=3,
                            type='minecraft:set_count',
                        ),
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:yellow_candle',
                                state={'candles': '4'},
                                type='minecraft:match_block',
                            ),
                            count=4,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:yellow_candle',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/yellow_candle',
)

YELLOW_CANDLE_CAKE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[LootPool(rolls=1, entries=[LootPoolEntryItem(name='minecraft:yellow_candle', type='minecraft:item')])],
    random_sequence='minecraft:blocks/yellow_candle_cake',
)

YELLOW_CARPET = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_carpet', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_carpet',
)

YELLOW_CONCRETE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_concrete', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_concrete',
)

YELLOW_CONCRETE_POWDER = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_concrete_powder', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_concrete_powder',
)

YELLOW_CONCRETE_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:yellow_concrete_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:yellow_concrete_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/yellow_concrete_slab',
)

YELLOW_CONCRETE_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_concrete_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_concrete_stairs',
)

YELLOW_GLAZED_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_glazed_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_glazed_terracotta',
)

YELLOW_POPLAR_LEAVES = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryAlternatives(
                    children=[
                        LootPoolEntryItem(
                            condition=LootConditionAnyOf(
                                terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                                type='minecraft:any_of',
                            ),
                            name='minecraft:yellow_poplar_leaves',
                            type='minecraft:item',
                        ),
                        LootPoolEntryItem(
                            condition=LootConditionAllOf(
                                terms=[
                                    LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
                                    LootConditionTableBonus(
                                        enchantment='minecraft:fortune',
                                        chances=[0.05, 0.0625, 0.083333336, 0.1],
                                        type='minecraft:table_bonus',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            name='minecraft:poplar_sapling',
                            type='minecraft:item',
                        ),
                    ],
                    type='minecraft:alternatives',
                ),
            ],
        ),
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            count=ContextIntProviderStructUniform(type='minecraft:uniform', min=1, max=2),
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    condition=LootConditionTableBonus(
                        enchantment='minecraft:fortune',
                        chances=[0.02, 0.022222223, 0.025, 0.033333335, 0.1],
                        type='minecraft:table_bonus',
                    ),
                    name='minecraft:stick',
                    type='minecraft:item',
                ),
            ],
            condition=LootConditionInverted(
                term=LootConditionAnyOf(
                    terms=['minecraft:tool/can_shear', 'minecraft:tool/can_silk_touch'],
                    type='minecraft:any_of',
                ),
                type='minecraft:inverted',
            ),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_poplar_leaves',
)

YELLOW_SHULKER_BOX = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name', 'minecraft:container', 'minecraft:lock', 'minecraft:container_loot'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:yellow_shulker_box',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/yellow_shulker_box',
)

YELLOW_STAINED_GLASS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_stained_glass', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/yellow_stained_glass',
)

YELLOW_STAINED_GLASS_PANE = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_stained_glass_pane', type='minecraft:item')],
            condition='minecraft:tool/can_silk_touch',
        ),
    ],
    random_sequence='minecraft:blocks/yellow_stained_glass_pane',
)

YELLOW_TERRACOTTA = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_terracotta', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_terracotta',
)

YELLOW_WOOL = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_wool', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_wool',
)

YELLOW_WOOL_SLAB = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=[
                        LootFunctionSetCount(
                            condition=LootConditionMatchBlock(
                                blocks='minecraft:yellow_wool_slab',
                                state={'type': 'double'},
                                type='minecraft:match_block',
                            ),
                            count=2,
                            type='minecraft:set_count',
                        ),
                        LootFunctionExplosionDecay(type='minecraft:explosion_decay'),
                    ],
                    name='minecraft:yellow_wool_slab',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/yellow_wool_slab',
)

YELLOW_WOOL_STAIRS = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[LootPoolEntryItem(name='minecraft:yellow_wool_stairs', type='minecraft:item')],
            condition=LootConditionSurvivesExplosion(type='minecraft:survives_explosion'),
        ),
    ],
    random_sequence='minecraft:blocks/yellow_wool_stairs',
)

ZOMBIE_HEAD = LootTable(
    type=LootContextParamSets.BLOCK,
    pools=[
        LootPool(
            rolls=1,
            entries=[
                LootPoolEntryItem(
                    modifier=LootFunctionCopyComponents(
                        source='block_entity',
                        include=['minecraft:custom_name'],
                        type='minecraft:copy_components',
                    ),
                    name='minecraft:zombie_head',
                    type='minecraft:item',
                ),
            ],
        ),
    ],
    random_sequence='minecraft:blocks/zombie_head',
)
