"""Vanilla's data/worldgen/feature/coral/ files"""
from vanilla_mcdoc.data.worldgen.feature.ConfiguredFeature import ConfiguredFeatureNoOp, ConfiguredFeatureOverlay, ConfiguredFeatureSimpleBlock, ConfiguredFeatureWeightedRandomSelector
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateMatchingBlocks
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.TypedBlockStateProvider import TypedBlockStateProviderRandomBlock, TypedBlockStateProviderRotated
from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
from vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier import PlacementModifierBlockPredicateFilter, PlacementModifierOffset, PlacementModifierRandomChance
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState
from vanilla_mcdoc.util.direction.Direction import Direction

BLOCK_DECORATION = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureWeightedRandomSelector(
                features=[
                    WeightedEntry(
                        weight=20,
                        data=PlacedFeature(
                            feature=ConfiguredFeatureSimpleBlock(
                                to_place=TypedBlockStateProviderRandomBlock(
                                    blocks='#minecraft:corals',
                                    type='minecraft:random_block',
                                ),
                                type='minecraft:simple_block',
                            ),
                            placement=[],
                        ),
                    ),
                    WeightedEntry(weight=3, data=PlacedFeature(feature='minecraft:sea_pickle', placement=[])),
                    WeightedEntry(
                        weight=57,
                        data=PlacedFeature(feature=ConfiguredFeatureNoOp(type='minecraft:no_op'), placement=[]),
                    ),
                ],
                type='minecraft:weighted_random_selector',
            ),
            placement=[PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset')],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=TypedBlockStateProviderRotated(
                    state=TypedBlockStateProviderRandomBlock(blocks='#minecraft:wall_corals', type='minecraft:random_block'),
                    direction=Direction.NORTH,
                    type='minecraft:rotated',
                ),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierRandomChance(chance=0.2, type='minecraft:random_chance'),
                PlacementModifierOffset(x=0, y=0, z=-1, type='minecraft:offset'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=TypedBlockStateProviderRotated(
                    state=TypedBlockStateProviderRandomBlock(blocks='#minecraft:wall_corals', type='minecraft:random_block'),
                    direction=Direction.EAST,
                    type='minecraft:rotated',
                ),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierRandomChance(chance=0.2, type='minecraft:random_chance'),
                PlacementModifierOffset(x=1, y=0, z=0, type='minecraft:offset'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=TypedBlockStateProviderRotated(
                    state=TypedBlockStateProviderRandomBlock(blocks='#minecraft:wall_corals', type='minecraft:random_block'),
                    direction=Direction.SOUTH,
                    type='minecraft:rotated',
                ),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierRandomChance(chance=0.2, type='minecraft:random_chance'),
                PlacementModifierOffset(x=0, y=0, z=1, type='minecraft:offset'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=TypedBlockStateProviderRotated(
                    state=TypedBlockStateProviderRandomBlock(blocks='#minecraft:wall_corals', type='minecraft:random_block'),
                    direction=Direction.WEST,
                    type='minecraft:rotated',
                ),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierRandomChance(chance=0.2, type='minecraft:random_chance'),
                PlacementModifierOffset(x=-1, y=0, z=0, type='minecraft:offset'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
    ],
    type='minecraft:overlay',
)

BRAIN_BLOCK = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:brain_coral_block'),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(feature='minecraft:coral/block_decoration', placement=[]),
    ],
    type='minecraft:overlay',
)

BUBBLE_BLOCK = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:bubble_coral_block'),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(feature='minecraft:coral/block_decoration', placement=[]),
    ],
    type='minecraft:overlay',
)

FIRE_BLOCK = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:fire_coral_block'),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(feature='minecraft:coral/block_decoration', placement=[]),
    ],
    type='minecraft:overlay',
)

HORN_BLOCK = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:horn_coral_block'),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(feature='minecraft:coral/block_decoration', placement=[]),
    ],
    type='minecraft:overlay',
)

TUBE_BLOCK = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:tube_coral_block'),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(feature='minecraft:coral/block_decoration', placement=[]),
    ],
    type='minecraft:overlay',
)
