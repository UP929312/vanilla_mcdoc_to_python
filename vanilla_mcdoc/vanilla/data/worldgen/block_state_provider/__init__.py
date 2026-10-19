"""Vanilla's data/worldgen/block_state_provider/ files"""
from typing import Any
from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters
from vanilla_mcdoc.data.worldgen.feature.RuleBasedBlockStateProvider import RulesStruct
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateMatchingBlockTag, BlockPredicateNot
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.TypedBlockStateProvider import TypedBlockStateProviderDualNoise, TypedBlockStateProviderNoise, TypedBlockStateProviderNoiseThreshold, TypedBlockStateProviderRandomizedInt, TypedBlockStateProviderRuleBased, TypedBlockStateProviderWeighted
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState

CAVE_VINES_BODY = TypedBlockStateProviderWeighted(
    entries=[
        WeightedEntry(weight=4, data='minecraft:cave_vines_plant'),
        WeightedEntry(weight=1, data=FullBlockState(id='minecraft:cave_vines_plant', properties={'berries': 'true'})),
    ],
    type='minecraft:weighted',
)

CAVE_VINES_HEAD = TypedBlockStateProviderRandomizedInt(
    property='age',
    values=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 25, 'min_inclusive': 23})),
    source=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=4, data='minecraft:cave_vines'),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:cave_vines', properties={'age': '0', 'berries': 'true'}),
            ),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:randomized_int',
)

FLOWER_FLOWER_FOREST = TypedBlockStateProviderNoise(
    seed=2345,
    noise=NoiseParameters(base_octave=0, base_amplitude=0.955388882960065),
    scale=0.020833334,
    states=[
        'minecraft:dandelion',
        'minecraft:poppy',
        'minecraft:allium',
        'minecraft:azure_bluet',
        'minecraft:red_tulip',
        'minecraft:orange_tulip',
        'minecraft:white_tulip',
        'minecraft:pink_tulip',
        'minecraft:oxeye_daisy',
        'minecraft:cornflower',
        'minecraft:lily_of_the_valley',
    ],
    type='minecraft:noise',
)

FLOWER_MEADOW = TypedBlockStateProviderDualNoise(
    seed=2345,
    noise=NoiseParameters(base_octave=-3, base_amplitude=0.955388882960065),
    scale=1.0,
    variety=(1, 3),
    slow_noise=NoiseParameters(base_octave=-10, base_amplitude=0.955388882960065),
    slow_scale=1.0,
    states=[
        'minecraft:tall_grass',
        'minecraft:allium',
        'minecraft:poppy',
        'minecraft:azure_bluet',
        'minecraft:dandelion',
        'minecraft:cornflower',
        'minecraft:oxeye_daisy',
        'minecraft:short_grass',
    ],
    type='minecraft:dual_noise',
)

FLOWER_PLAIN = TypedBlockStateProviderNoiseThreshold(
    seed=2345,
    noise=NoiseParameters(base_octave=0, base_amplitude=0.955388882960065),
    scale=0.005,
    threshold=-0.8,
    high_chance=0.33333334,
    default_state='minecraft:dandelion',
    low_states=['minecraft:orange_tulip', 'minecraft:red_tulip', 'minecraft:pink_tulip', 'minecraft:white_tulip'],
    high_states=['minecraft:poppy', 'minecraft:azure_bluet', 'minecraft:oxeye_daisy', 'minecraft:cornflower'],
    type='minecraft:noise_threshold',
)

MANGROVE_PROPAGULE = TypedBlockStateProviderRandomizedInt(
    property='age',
    values=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 0})),
    source=FullBlockState(
        id='minecraft:mangrove_propagule',
        properties={'age': '0', 'hanging': 'true', 'stage': '0', 'waterlogged': 'false'},
    ),
    type='minecraft:randomized_int',
)

PODZOL_BENEATH_TREE = TypedBlockStateProviderRuleBased(
    rules=[
        RulesStruct(
            if_true=BlockPredicateMatchingBlockTag(
                tag='minecraft:beneath_tree_podzol_replaceable',
                type='minecraft:matching_block_tag',
            ),
            then=FullBlockState(id='minecraft:podzol', properties={'snowy': 'false'}),
        ),
    ],
    type='minecraft:rule_based',
)

SOIL_BENEATH_TREE = TypedBlockStateProviderRuleBased(
    rules=[
        RulesStruct(
            if_true=BlockPredicateNot(
                predicate=BlockPredicateMatchingBlockTag(
                    tag='minecraft:cannot_replace_below_tree_trunk',
                    type='minecraft:matching_block_tag',
                ),
                type='minecraft:not',
            ),
            then=FullBlockState(id='minecraft:dirt'),
        ),
    ],
    type='minecraft:rule_based',
)
