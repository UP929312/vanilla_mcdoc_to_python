"""Vanilla's data/worldgen/placed_feature/ files"""
from typing import Any
from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProviderStructTrapezoid, HeightProviderStructUniform, HeightProviderStructVeryBiasedToBottom
from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType
from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchorStruct1, VerticalAnchorStruct2, VerticalAnchorStruct3
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateAllOf, BlockPredicateAnyOf, BlockPredicateBelowHeightmap, BlockPredicateHasSturdyFace, BlockPredicateInsideWorldBounds, BlockPredicateMatchingBlockTag, BlockPredicateMatchingBlocks, BlockPredicateMatchingFluids, BlockPredicateNot, BlockPredicateReplaceable, BlockPredicateSolid, BlockPredicateVolumeMatch, BlockPredicateWouldSurvive
from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
from vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier import PlacementModifierBiome, PlacementModifierBlockPredicateFilter, PlacementModifierCount, PlacementModifierCountOnEveryLayer, PlacementModifierEnvironmentScan, PlacementModifierFixedPlacement, PlacementModifierHeightRange, PlacementModifierHeightmap, PlacementModifierInSquare, PlacementModifierNoiseBasedCount, PlacementModifierNoiseThresholdCount, PlacementModifierOffset, PlacementModifierRarityFilter, PlacementModifierSurfaceRelativeThresholdFilter, PlacementModifierSurfaceWaterDepthFilter
from vanilla_mcdoc.util.direction.Direction import Direction
from vanilla_mcdoc.util.direction.VerticalDirection import VerticalDirection

ACACIA = PlacedFeature(
    feature='minecraft:acacia',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:acacia_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ACACIA_CHECKED = PlacedFeature(
    feature='minecraft:acacia',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:acacia_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

AMETHYST_GEODE = PlacedFeature(
    feature='minecraft:amethyst_geode',
    placement=[
        PlacementModifierRarityFilter(chance=24, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=6),
                max_inclusive=VerticalAnchorStruct1(absolute=30),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BAMBOO = PlacedFeature(
    feature='minecraft:bamboo_some_podzol',
    placement=[
        PlacementModifierNoiseBasedCount(
            noise_to_count_ratio=160,
            noise_factor=80.0,
            noise_offset=0.3,
            type='minecraft:noise_based_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BAMBOO_IN_STRUCTURE = PlacedFeature(
    feature='minecraft:bamboo_no_podzol',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BAMBOO_LIGHT = PlacedFeature(
    feature='minecraft:bamboo_no_podzol',
    placement=[
        PlacementModifierRarityFilter(chance=4, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BAMBOO_VEGETATION = PlacedFeature(
    feature='minecraft:bamboo_vegetation',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 30, 'weight': 9}, {'data': 31, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BASALT_BLOBS = PlacedFeature(
    feature='minecraft:basalt_blobs',
    placement=[
        PlacementModifierCount(count=75, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BASALT_PILLAR = PlacedFeature(
    feature='minecraft:basalt_pillar',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateNot(
                        predicate=BlockPredicateMatchingBlockTag(
                            offset=(0, 1, 0),
                            tag='minecraft:air',
                            type='minecraft:matching_block_tag',
                        ),
                        type='minecraft:not',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BIRCH_BEES_0002 = PlacedFeature(
    feature='minecraft:birch_bees_0002',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BIRCH_BEES_0002_LEAF_LITTER = PlacedFeature(
    feature='minecraft:birch_bees_0002_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BIRCH_BEES_002 = PlacedFeature(
    feature='minecraft:birch_bees_002',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BIRCH_CHECKED = PlacedFeature(
    feature='minecraft:birch',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BIRCH_LEAF_LITTER = PlacedFeature(
    feature='minecraft:birch_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BIRCH_TALL = PlacedFeature(
    feature='minecraft:birch_tall',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BLACKSTONE_BLOBS = PlacedFeature(
    feature='minecraft:blackstone_blobs',
    placement=[
        PlacementModifierCount(count=25, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BLUE_ICE = PlacedFeature(
    feature='minecraft:blue_ice',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 19, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=30),
                max_inclusive=VerticalAnchorStruct1(absolute=61),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

BROWN_MUSHROOM_DAPPLED_FOREST = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BROWN_MUSHROOM_NETHER = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BROWN_MUSHROOM_NORMAL = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=256, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BROWN_MUSHROOM_OLD_GROWTH = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierRarityFilter(chance=4, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BROWN_MUSHROOM_SWAMP = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

BROWN_MUSHROOM_TAIGA = PlacedFeature(
    feature='minecraft:brown_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=4, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

CAVE_VINES = PlacedFeature(
    feature='minecraft:cave_vine',
    placement=[
        PlacementModifierCount(count=188, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=12,
            target_condition=BlockPredicateHasSturdyFace(direction=Direction.DOWN, type='minecraft:has_sturdy_face'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

CHERRY_BEES_005 = PlacedFeature(
    feature='minecraft:cherry_bees_005',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:cherry_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

CHERRY_CHECKED = PlacedFeature(
    feature='minecraft:cherry',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:cherry_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

CHORUS_PLANT = PlacedFeature(
    feature='minecraft:chorus_plant',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

CLASSIC_VINES_CAVE_FEATURE = PlacedFeature(
    feature='minecraft:vines',
    placement=[
        PlacementModifierCount(count=256, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

CRIMSON_FOREST_VEGETATION = PlacedFeature(
    feature='minecraft:crimson_forest_vegetation',
    placement=[
        PlacementModifierCountOnEveryLayer(count=6, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(
                offset=(0, -1, 0),
                tag='minecraft:nylium',
                type='minecraft:matching_block_tag',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

CRIMSON_FUNGI = PlacedFeature(
    feature='minecraft:crimson_fungus',
    placement=[
        PlacementModifierCountOnEveryLayer(count=8, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DARK_FOREST_VEGETATION = PlacedFeature(
    feature='minecraft:dark_forest_vegetation',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DARK_OAK_CHECKED = PlacedFeature(
    feature='minecraft:dark_oak',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:dark_oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

DARK_OAK_LEAF_LITTER = PlacedFeature(
    feature='minecraft:dark_oak_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:dark_oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

DELTA = PlacedFeature(
    feature='minecraft:delta',
    placement=[
        PlacementModifierCountOnEveryLayer(count=40, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DESERT_WELL = PlacedFeature(
    feature='minecraft:desert_well',
    placement=[
        PlacementModifierRarityFilter(chance=1000, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlocks(blocks='minecraft:sand', type='minecraft:matching_blocks'),
                    BlockPredicateVolumeMatch(
                        min=(-2, -2, -2),
                        max=(2, -1, 2),
                        match=BlockPredicateNot(
                            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            type='minecraft:not',
                        ),
                        type='minecraft:volume_match',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DISK_CLAY = PlacedFeature(
    feature='minecraft:disk_clay',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOORWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingFluids(
                fluids='minecraft:water',
                state={'source': 'true'},
                type='minecraft:matching_fluids',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DISK_GRASS = PlacedFeature(
    feature='minecraft:disk_grass',
    placement=[
        PlacementModifierCount(count=1, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOORWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:mud', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DISK_GRAVEL = PlacedFeature(
    feature='minecraft:disk_gravel',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOORWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingFluids(
                fluids='minecraft:water',
                state={'source': 'true'},
                type='minecraft:matching_fluids',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DISK_SAND = PlacedFeature(
    feature='minecraft:disk_sand',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOORWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingFluids(
                fluids='minecraft:water',
                state={'source': 'true'},
                type='minecraft:matching_fluids',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

DRIPSTONE_CLUSTER = PlacedFeature(
    feature='minecraft:dripstone_cluster',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 96, 'min_inclusive': 48})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

END_GATEWAY_RETURN = PlacedFeature(
    feature='minecraft:end_gateway_return',
    placement=[
        PlacementModifierRarityFilter(chance=700, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierOffset(
            x=0,
            y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 9, 'min_inclusive': 3})),
            z=0,
            type='minecraft:offset',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

END_ISLAND_DECORATED = PlacedFeature(
    feature='minecraft:end_island',
    placement=[
        PlacementModifierRarityFilter(chance=14, type='minecraft:rarity_filter'),
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 1, 'weight': 3}, {'data': 2, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=55),
                max_inclusive=VerticalAnchorStruct1(absolute=70),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

END_PLATFORM = PlacedFeature(
    feature='minecraft:end_platform',
    placement=[
        PlacementModifierFixedPlacement(positions=[(100, 49, 0)], type='minecraft:fixed_placement'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

END_SPIKE = PlacedFeature(feature='minecraft:end_spike', placement=[PlacementModifierBiome(type='minecraft:biome')])

FALLEN_BIRCH_TREE = PlacedFeature(
    feature='minecraft:fallen_birch_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FALLEN_JUNGLE_TREE = PlacedFeature(
    feature='minecraft:fallen_jungle_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:jungle_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FALLEN_OAK_TREE = PlacedFeature(
    feature='minecraft:fallen_oak_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FALLEN_POPLAR_TREE = PlacedFeature(
    feature='minecraft:fallen_poplar_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FALLEN_SPRUCE_TREE = PlacedFeature(
    feature='minecraft:fallen_spruce_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FALLEN_SUPER_BIRCH_TREE = PlacedFeature(
    feature='minecraft:fallen_super_birch_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FANCY_OAK_BEES = PlacedFeature(
    feature='minecraft:fancy_oak_bees',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FANCY_OAK_BEES_0002_LEAF_LITTER = PlacedFeature(
    feature='minecraft:fancy_oak_bees_0002_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FANCY_OAK_BEES_002 = PlacedFeature(
    feature='minecraft:fancy_oak_bees_002',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FANCY_OAK_CHECKED = PlacedFeature(
    feature='minecraft:fancy_oak',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FANCY_OAK_LEAF_LITTER = PlacedFeature(
    feature='minecraft:fancy_oak_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_CHERRY = PlacedFeature(
    feature='minecraft:flower_cherry',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=5,
            above_noise=10,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_DEFAULT = PlacedFeature(
    feature='minecraft:flower_default',
    placement=[
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_FLOWER_FOREST = PlacedFeature(
    feature='minecraft:flower_flower_forest',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_FOREST_FLOWERS = PlacedFeature(
    feature='minecraft:forest_flowers',
    placement=[
        PlacementModifierRarityFilter(chance=7, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:clamped',
                **dict[str, Any]({
                    'max_inclusive': 3,
                    'min_inclusive': 0,
                    'source': {'type': 'minecraft:uniform', 'max_inclusive': 3, 'min_inclusive': -1},
                }),
            ),
            type='minecraft:count',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FLOWER_MEADOW = PlacedFeature(
    feature='minecraft:flower_meadow',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_PALE_GARDEN = PlacedFeature(
    feature='minecraft:flower_pale_garden',
    placement=[
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FLOWER_PLAIN = PlacedFeature(
    feature='minecraft:flower_plain',
    placement=[
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_PLAINS = PlacedFeature(
    feature='minecraft:flower_plain',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=15,
            above_noise=4,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_SWAMP = PlacedFeature(
    feature='minecraft:flower_swamp',
    placement=[
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FLOWER_WARM = PlacedFeature(
    feature='minecraft:flower_default',
    placement=[
        PlacementModifierRarityFilter(chance=16, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

FOREST_FLOWERS = PlacedFeature(
    feature='minecraft:forest_flowers',
    placement=[
        PlacementModifierRarityFilter(chance=7, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:clamped',
                **dict[str, Any]({
                    'max_inclusive': 1,
                    'min_inclusive': 0,
                    'source': {'type': 'minecraft:uniform', 'max_inclusive': 1, 'min_inclusive': -3},
                }),
            ),
            type='minecraft:count',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FOREST_ROCK = PlacedFeature(
    feature='minecraft:forest_rock',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FOSSIL_LOWER = PlacedFeature(
    feature='minecraft:fossil_diamonds',
    placement=[
        PlacementModifierRarityFilter(chance=64, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=-8),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FOSSIL_UPPER = PlacedFeature(
    feature='minecraft:fossil_coal',
    placement=[
        PlacementModifierRarityFilter(chance=64, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

FREEZE_TOP_LAYER = PlacedFeature(feature='minecraft:freeze_top_layer', placement=[PlacementModifierBiome(type='minecraft:biome')])

GLOWSTONE = PlacedFeature(
    feature='minecraft:glowstone_extra',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, 1, 0),
                        blocks=['minecraft:netherrack', 'minecraft:basalt', 'minecraft:blackstone'],
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

GLOWSTONE_EXTRA = PlacedFeature(
    feature='minecraft:glowstone_extra',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:biased_to_bottom', **dict[str, Any]({'max_inclusive': 9, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=4),
                max_inclusive=VerticalAnchorStruct3(below_top=4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, 1, 0),
                        blocks=['minecraft:netherrack', 'minecraft:basalt', 'minecraft:blackstone'],
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

GLOW_LICHEN = PlacedFeature(
    feature='minecraft:glow_lichen',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 157, 'min_inclusive': 104})),
            type='minecraft:count',
        ),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceRelativeThresholdFilter(
            heightmap=HeightmapType.OCEANFLOORWORLDGEN,
            max_inclusive=-13,
            type='minecraft:surface_relative_threshold_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

GRASS_BONEMEAL = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ICEBERG_BLUE = PlacedFeature(
    feature='minecraft:iceberg_blue',
    placement=[
        PlacementModifierRarityFilter(chance=200, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICEBERG_PACKED = PlacedFeature(
    feature='minecraft:iceberg_packed',
    placement=[
        PlacementModifierRarityFilter(chance=16, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_ANDESITE_LOWER = PlacedFeature(
    feature='minecraft:ice_cave_ore_andesite',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=60),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_ANDESITE_UPPER = PlacedFeature(
    feature='minecraft:ice_cave_ore_andesite',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=128),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_COAL_LOWER = PlacedFeature(
    feature='minecraft:ice_cave_ore_coal_buried',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=192),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_COAL_UPPER = PlacedFeature(
    feature='minecraft:ice_cave_ore_coal',
    placement=[
        PlacementModifierCount(count=30, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=136),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_COPPER = PlacedFeature(
    feature='minecraft:ice_cave_ore_copper_small',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-16),
                max_inclusive=VerticalAnchorStruct1(absolute=112),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIAMOND = PlacedFeature(
    feature='minecraft:ice_cave_ore_diamond_small',
    placement=[
        PlacementModifierCount(count=7, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIAMOND_BURIED = PlacedFeature(
    feature='minecraft:ice_cave_ore_diamond_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIAMOND_LARGE = PlacedFeature(
    feature='minecraft:ice_cave_ore_diamond_large',
    placement=[
        PlacementModifierRarityFilter(chance=9, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIAMOND_MEDIUM = PlacedFeature(
    feature='minecraft:ice_cave_ore_diamond_medium',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=-4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIORITE_LOWER = PlacedFeature(
    feature='minecraft:ice_cave_ore_diorite',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=60),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_DIORITE_UPPER = PlacedFeature(
    feature='minecraft:ice_cave_ore_diorite',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=128),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_GOLD = PlacedFeature(
    feature='minecraft:ice_cave_ore_gold_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_GOLD_LOWER = PlacedFeature(
    feature='minecraft:ice_cave_ore_gold_buried',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 1, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=-48),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_GRAVEL = PlacedFeature(
    feature='minecraft:ice_cave_ore_gravel',
    placement=[
        PlacementModifierCount(count=14, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_IRON_MIDDLE = PlacedFeature(
    feature='minecraft:ice_cave_ore_iron',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-24),
                max_inclusive=VerticalAnchorStruct1(absolute=56),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_IRON_SMALL = PlacedFeature(
    feature='minecraft:ice_cave_ore_iron_small',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=72),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_IRON_UPPER = PlacedFeature(
    feature='minecraft:ice_cave_ore_iron',
    placement=[
        PlacementModifierCount(count=90, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=80),
                max_inclusive=VerticalAnchorStruct1(absolute=384),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_LAPIS = PlacedFeature(
    feature='minecraft:ice_cave_ore_lapis',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-32),
                max_inclusive=VerticalAnchorStruct1(absolute=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_LAPIS_BURIED = PlacedFeature(
    feature='minecraft:ice_cave_ore_lapis_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=64),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_REDSTONE = PlacedFeature(
    feature='minecraft:ice_cave_ore_redstone',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=15),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CAVE_ORE_REDSTONE_LOWER = PlacedFeature(
    feature='minecraft:ice_cave_ore_redstone',
    placement=[
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-32),
                max_inclusive=VerticalAnchorStruct2(above_bottom=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CREVASSE = PlacedFeature(
    feature='minecraft:ice_crevasse',
    placement=[
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=24),
                max_inclusive=VerticalAnchorStruct3(below_top=64),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=32,
            target_condition=BlockPredicateMatchingBlockTag(
                tag='minecraft:ice_crevasse_replaceables',
                type='minecraft:matching_block_tag',
            ),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_CRYSTALS = PlacedFeature(
    feature='minecraft:ice_crystal',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 64, 'min_inclusive': 48})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=32,
            target_condition=BlockPredicateMatchingBlocks(blocks='minecraft:packed_ice', type='minecraft:matching_blocks'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_PATCH = PlacedFeature(
    feature='minecraft:ice_patch',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:snow_block', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICE_SPIKE = PlacedFeature(
    feature='minecraft:ice_spike',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ICICLE_CLUSTER = PlacedFeature(
    feature='minecraft:icicle_cluster',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 64, 'min_inclusive': 24})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

JUNGLE_BUSH = PlacedFeature(
    feature='minecraft:jungle_bush',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

JUNGLE_TREE = PlacedFeature(
    feature='minecraft:jungle_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:jungle_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

KELP_COLD = PlacedFeature(
    feature='minecraft:kelp',
    placement=[
        PlacementModifierNoiseBasedCount(
            noise_to_count_ratio=120,
            noise_factor=80.0,
            type='minecraft:noise_based_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, 1, 0),
                        blocks='minecraft:water',
                        type='minecraft:matching_blocks',
                    ),
                    BlockPredicateHasSturdyFace(
                        offset=(0, -1, 0),
                        direction=Direction.UP,
                        type='minecraft:has_sturdy_face',
                    ),
                    BlockPredicateNot(
                        predicate=BlockPredicateMatchingBlockTag(
                            offset=(0, -1, 0),
                            tag='minecraft:cannot_support_kelp',
                            type='minecraft:matching_block_tag',
                        ),
                        type='minecraft:not',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

KELP_WARM = PlacedFeature(
    feature='minecraft:kelp',
    placement=[
        PlacementModifierNoiseBasedCount(noise_to_count_ratio=80, noise_factor=80.0, type='minecraft:noise_based_count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, 1, 0),
                        blocks='minecraft:water',
                        type='minecraft:matching_blocks',
                    ),
                    BlockPredicateHasSturdyFace(
                        offset=(0, -1, 0),
                        direction=Direction.UP,
                        type='minecraft:has_sturdy_face',
                    ),
                    BlockPredicateNot(
                        predicate=BlockPredicateMatchingBlockTag(
                            offset=(0, -1, 0),
                            tag='minecraft:cannot_support_kelp',
                            type='minecraft:matching_block_tag',
                        ),
                        type='minecraft:not',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LAKE_LAVA_SURFACE = PlacedFeature(
    feature='minecraft:lake_lava',
    placement=[
        PlacementModifierRarityFilter(chance=200, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LAKE_LAVA_UNDERGROUND = PlacedFeature(
    feature='minecraft:lake_lava',
    placement=[
        PlacementModifierRarityFilter(chance=9, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=32,
            target_condition=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateNot(
                        predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                        type='minecraft:not',
                    ),
                    BlockPredicateInsideWorldBounds(offset=(0, -5, 0), type='minecraft:inside_world_bounds'),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:environment_scan',
        ),
        PlacementModifierSurfaceRelativeThresholdFilter(
            heightmap=HeightmapType.OCEANFLOORWORLDGEN,
            max_inclusive=-5,
            type='minecraft:surface_relative_threshold_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LARGE_BASALT_COLUMNS = PlacedFeature(
    feature='minecraft:large_basalt_columns',
    placement=[
        PlacementModifierCountOnEveryLayer(count=2, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LARGE_DRIPSTONE = PlacedFeature(
    feature='minecraft:large_dripstone',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 48, 'min_inclusive': 10})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LARGE_ICICLE = PlacedFeature(
    feature='minecraft:large_icicle',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 64, 'min_inclusive': 48})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LUSH_CAVES_CEILING_VEGETATION = PlacedFeature(
    feature='minecraft:moss_patch_ceiling',
    placement=[
        PlacementModifierCount(count=125, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LUSH_CAVES_CLAY = PlacedFeature(
    feature='minecraft:lush_caves_clay',
    placement=[
        PlacementModifierCount(count=62, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

LUSH_CAVES_VEGETATION = PlacedFeature(
    feature='minecraft:moss_patch',
    placement=[
        PlacementModifierCount(count=125, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

MANGROVE_CHECKED = PlacedFeature(
    feature='minecraft:mangrove',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:mangrove_propagule', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

MEGA_JUNGLE_TREE_CHECKED = PlacedFeature(
    feature='minecraft:mega_jungle_tree',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:jungle_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

MEGA_PINE_CHECKED = PlacedFeature(
    feature='minecraft:mega_pine',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

MEGA_SPRUCE_CHECKED = PlacedFeature(
    feature='minecraft:mega_spruce',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

MONSTER_ROOM = PlacedFeature(
    feature='minecraft:monster_room',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

MONSTER_ROOM_DEEP = PlacedFeature(
    feature='minecraft:monster_room',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=6),
                max_inclusive=VerticalAnchorStruct1(absolute=-1),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

MUSHROOM_ISLAND_VEGETATION = PlacedFeature(
    feature='minecraft:mushroom_island_vegetation',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

NETHER_SPROUTS = PlacedFeature(
    feature='minecraft:nether_sprouts',
    placement=[
        PlacementModifierCountOnEveryLayer(count=4, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(
                offset=(0, -1, 0),
                tag='minecraft:nylium',
                type='minecraft:matching_block_tag',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

OAK = PlacedFeature(
    feature='minecraft:oak',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

OAK_BEES_0002_LEAF_LITTER = PlacedFeature(
    feature='minecraft:oak_bees_0002_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

OAK_BEES_002 = PlacedFeature(
    feature='minecraft:oak_bees_002',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

OAK_CHECKED = PlacedFeature(
    feature='minecraft:oak',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

OAK_LEAF_LITTER = PlacedFeature(
    feature='minecraft:oak_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ORANGE_POPLAR = PlacedFeature(
    feature='minecraft:orange_poplar',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ORANGE_POPLAR_LEAF_LITTER = PlacedFeature(
    feature='minecraft:orange_poplar_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ORE_ANCIENT_DEBRIS_LARGE = PlacedFeature(
    feature='minecraft:ore_ancient_debris_large',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=8),
                max_inclusive=VerticalAnchorStruct1(absolute=24),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_ANDESITE_LOWER = PlacedFeature(
    feature='minecraft:ore_andesite',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=60),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_ANDESITE_UPPER = PlacedFeature(
    feature='minecraft:ore_andesite',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=128),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_BLACKSTONE = PlacedFeature(
    feature='minecraft:ore_blackstone',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=5),
                max_inclusive=VerticalAnchorStruct1(absolute=31),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_CLAY = PlacedFeature(
    feature='minecraft:ore_clay',
    placement=[
        PlacementModifierCount(count=46, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_COAL_LOWER = PlacedFeature(
    feature='minecraft:ore_coal_buried',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=192),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_COAL_UPPER = PlacedFeature(
    feature='minecraft:ore_coal',
    placement=[
        PlacementModifierCount(count=30, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=136),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_COPPER = PlacedFeature(
    feature='minecraft:ore_copper_small',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-16),
                max_inclusive=VerticalAnchorStruct1(absolute=112),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_COPPER_LARGE = PlacedFeature(
    feature='minecraft:ore_copper_large',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-16),
                max_inclusive=VerticalAnchorStruct1(absolute=112),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DEBRIS_SMALL = PlacedFeature(
    feature='minecraft:ore_ancient_debris_small',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=8),
                max_inclusive=VerticalAnchorStruct3(below_top=8),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIAMOND = PlacedFeature(
    feature='minecraft:ore_diamond_small',
    placement=[
        PlacementModifierCount(count=7, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIAMOND_BURIED = PlacedFeature(
    feature='minecraft:ore_diamond_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIAMOND_LARGE = PlacedFeature(
    feature='minecraft:ore_diamond_large',
    placement=[
        PlacementModifierRarityFilter(chance=9, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-80),
                max_inclusive=VerticalAnchorStruct2(above_bottom=80),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIAMOND_MEDIUM = PlacedFeature(
    feature='minecraft:ore_diamond_medium',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=-4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIORITE_LOWER = PlacedFeature(
    feature='minecraft:ore_diorite',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=60),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIORITE_UPPER = PlacedFeature(
    feature='minecraft:ore_diorite',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=128),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_DIRT = PlacedFeature(
    feature='minecraft:ore_dirt',
    placement=[
        PlacementModifierCount(count=7, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=160),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_EMERALD = PlacedFeature(
    feature='minecraft:ore_emerald',
    placement=[
        PlacementModifierCount(count=100, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-16),
                max_inclusive=VerticalAnchorStruct1(absolute=480),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GOLD = PlacedFeature(
    feature='minecraft:ore_gold_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GOLD_DELTAS = PlacedFeature(
    feature='minecraft:ore_nether_gold',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GOLD_EXTRA = PlacedFeature(
    feature='minecraft:ore_gold',
    placement=[
        PlacementModifierCount(count=50, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=32),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GOLD_LOWER = PlacedFeature(
    feature='minecraft:ore_gold_buried',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 1, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=-64),
                max_inclusive=VerticalAnchorStruct1(absolute=-48),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GOLD_NETHER = PlacedFeature(
    feature='minecraft:ore_nether_gold',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GRANITE_LOWER = PlacedFeature(
    feature='minecraft:ore_granite',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=0),
                max_inclusive=VerticalAnchorStruct1(absolute=60),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GRANITE_UPPER = PlacedFeature(
    feature='minecraft:ore_granite',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=128),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GRAVEL = PlacedFeature(
    feature='minecraft:ore_gravel',
    placement=[
        PlacementModifierCount(count=14, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_GRAVEL_NETHER = PlacedFeature(
    feature='minecraft:ore_gravel_nether',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=5),
                max_inclusive=VerticalAnchorStruct1(absolute=41),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_INFESTED = PlacedFeature(
    feature='minecraft:ore_infested',
    placement=[
        PlacementModifierCount(count=14, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=63),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_IRON_MIDDLE = PlacedFeature(
    feature='minecraft:ore_iron',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-24),
                max_inclusive=VerticalAnchorStruct1(absolute=56),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_IRON_SMALL = PlacedFeature(
    feature='minecraft:ore_iron_small',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=72),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_IRON_UPPER = PlacedFeature(
    feature='minecraft:ore_iron',
    placement=[
        PlacementModifierCount(count=90, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=80),
                max_inclusive=VerticalAnchorStruct1(absolute=384),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_LAPIS = PlacedFeature(
    feature='minecraft:ore_lapis',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct1(absolute=-32),
                max_inclusive=VerticalAnchorStruct1(absolute=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_LAPIS_BURIED = PlacedFeature(
    feature='minecraft:ore_lapis_buried',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=64),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_MAGMA = PlacedFeature(
    feature='minecraft:ore_magma',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=27),
                max_inclusive=VerticalAnchorStruct1(absolute=36),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_QUARTZ_DELTAS = PlacedFeature(
    feature='minecraft:ore_quartz',
    placement=[
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_QUARTZ_NETHER = PlacedFeature(
    feature='minecraft:ore_quartz',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_REDSTONE = PlacedFeature(
    feature='minecraft:ore_redstone',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=15),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_REDSTONE_LOWER = PlacedFeature(
    feature='minecraft:ore_redstone',
    placement=[
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructTrapezoid(
                min_inclusive=VerticalAnchorStruct2(above_bottom=-32),
                max_inclusive=VerticalAnchorStruct2(above_bottom=32),
                type='minecraft:trapezoid',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_SOUL_SAND = PlacedFeature(
    feature='minecraft:ore_soul_sand',
    placement=[
        PlacementModifierCount(count=12, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=31),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ORE_TUFF = PlacedFeature(
    feature='minecraft:ore_tuff',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

PALE_GARDEN_FLOWERS = PlacedFeature(
    feature='minecraft:pale_forest_flower',
    placement=[
        PlacementModifierRarityFilter(chance=8, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKINGNOLEAVES, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PALE_GARDEN_VEGETATION = PlacedFeature(
    feature='minecraft:pale_garden_vegetation',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

PALE_MOSS_PATCH = PlacedFeature(
    feature='minecraft:pale_moss_patch',
    placement=[
        PlacementModifierCount(count=1, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKINGNOLEAVES, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

PALE_OAK_CHECKED = PlacedFeature(
    feature='minecraft:pale_oak',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:pale_oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PALE_OAK_CREAKING_CHECKED = PlacedFeature(
    feature='minecraft:pale_oak_creaking',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:pale_oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_BERRY_BUSH = PlacedFeature(
    feature='minecraft:berry_bush',
    placement=[
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_BERRY_COMMON = PlacedFeature(
    feature='minecraft:berry_bush',
    placement=[
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_BERRY_RARE = PlacedFeature(
    feature='minecraft:berry_bush',
    placement=[
        PlacementModifierRarityFilter(chance=384, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_BUSH = PlacedFeature(
    feature='minecraft:bush',
    placement=[
        PlacementModifierRarityFilter(chance=4, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=24, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 5, 'min': -5, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 5, 'min': -5, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_CACTUS = PlacedFeature(
    feature='minecraft:cactus',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:cactus', type='minecraft:would_survive'),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_CACTUS_DECORATED = PlacedFeature(
    feature='minecraft:cactus',
    placement=[
        PlacementModifierRarityFilter(chance=13, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:cactus', type='minecraft:would_survive'),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_CACTUS_DESERT = PlacedFeature(
    feature='minecraft:cactus',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:cactus', type='minecraft:would_survive'),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_CRIMSON_ROOTS = PlacedFeature(
    feature='minecraft:crimson_roots',
    placement=[
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_DEAD_BUSH = PlacedFeature(
    feature='minecraft:dead_bush',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_DEAD_BUSH_2 = PlacedFeature(
    feature='minecraft:dead_bush',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_DEAD_BUSH_BADLANDS = PlacedFeature(
    feature='minecraft:dead_bush',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_DRY_GRASS_BADLANDS = PlacedFeature(
    feature='minecraft:dry_grass',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_DRY_GRASS_DESERT = PlacedFeature(
    feature='minecraft:dry_grass',
    placement=[
        PlacementModifierRarityFilter(chance=3, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_FIRE = PlacedFeature(
    feature='minecraft:patch_fire',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=4),
                max_inclusive=VerticalAnchorStruct3(below_top=4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:netherrack',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_FIREFLY_BUSH_NEAR_WATER = PlacedFeature(
    feature='minecraft:firefly_bush',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKINGNOLEAVES, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:firefly_bush', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_FIREFLY_BUSH_NEAR_WATER_SWAMP = PlacedFeature(
    feature='minecraft:firefly_bush',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:firefly_bush', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_FIREFLY_BUSH_SWAMP = PlacedFeature(
    feature='minecraft:firefly_bush',
    placement=[
        PlacementModifierRarityFilter(chance=8, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_BADLANDS = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_FOREST = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_JUNGLE = PlacedFeature(
    feature='minecraft:grass_jungle',
    placement=[
        PlacementModifierCount(count=25, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateNot(
                        predicate=BlockPredicateMatchingBlocks(
                            offset=(0, -1, 0),
                            blocks='minecraft:podzol',
                            type='minecraft:matching_blocks',
                        ),
                        type='minecraft:not',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_MEADOW = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=5,
            above_noise=10,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_NORMAL = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierCount(count=5, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_PLAIN = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=5,
            above_noise=10,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_SAVANNA = PlacedFeature(
    feature='minecraft:grass',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_TAIGA = PlacedFeature(
    feature='minecraft:taiga_grass',
    placement=[
        PlacementModifierCount(count=7, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_GRASS_TAIGA_2 = PlacedFeature(
    feature='minecraft:taiga_grass',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_LARGE_FERN = PlacedFeature(
    feature='minecraft:large_fern',
    placement=[
        PlacementModifierRarityFilter(chance=5, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_LEAF_LITTER = PlacedFeature(
    feature='minecraft:leaf_litter',
    placement=[
        PlacementModifierCount(count=2, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_MELON = PlacedFeature(
    feature='minecraft:melon',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateReplaceable(type='minecraft:replaceable'),
                    BlockPredicateMatchingFluids(fluids='minecraft:empty', type='minecraft:matching_fluids'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_MELON_SPARSE = PlacedFeature(
    feature='minecraft:melon',
    placement=[
        PlacementModifierRarityFilter(chance=64, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateReplaceable(type='minecraft:replaceable'),
                    BlockPredicateMatchingFluids(fluids='minecraft:empty', type='minecraft:matching_fluids'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_PUMPKIN = PlacedFeature(
    feature='minecraft:pumpkin',
    placement=[
        PlacementModifierRarityFilter(chance=300, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:grass_block',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_RED_SHRUB = PlacedFeature(
    feature='minecraft:red_shrub',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SOUL_FIRE = PlacedFeature(
    feature='minecraft:patch_soul_fire',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 0})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=4),
                max_inclusive=VerticalAnchorStruct3(below_top=4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:soul_soil',
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SUGAR_CANE = PlacedFeature(
    feature='minecraft:sugar_cane',
    placement=[
        PlacementModifierRarityFilter(chance=6, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:sugar_cane', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SUGAR_CANE_BADLANDS = PlacedFeature(
    feature='minecraft:sugar_cane',
    placement=[
        PlacementModifierRarityFilter(chance=5, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:sugar_cane', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SUGAR_CANE_DESERT = PlacedFeature(
    feature='minecraft:sugar_cane',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:sugar_cane', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SUGAR_CANE_SWAMP = PlacedFeature(
    feature='minecraft:sugar_cane',
    placement=[
        PlacementModifierRarityFilter(chance=3, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateWouldSurvive(state='minecraft:sugar_cane', type='minecraft:would_survive'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingFluids(
                                offset=(1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(-1, -1, 0),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, 1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                            BlockPredicateMatchingFluids(
                                offset=(0, -1, -1),
                                fluids='minecraft:water',
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_SUNFLOWER = PlacedFeature(
    feature='minecraft:sunflower',
    placement=[
        PlacementModifierRarityFilter(chance=3, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_TAIGA_GRASS = PlacedFeature(
    feature='minecraft:taiga_grass',
    placement=[
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_TALL_GRASS = PlacedFeature(
    feature='minecraft:tall_grass',
    placement=[
        PlacementModifierRarityFilter(chance=5, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_TALL_GRASS_2 = PlacedFeature(
    feature='minecraft:tall_grass',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=0,
            above_noise=7,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierRarityFilter(chance=32, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PATCH_WATERLILY = PlacedFeature(
    feature='minecraft:waterlily',
    placement=[
        PlacementModifierCount(count=4, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.WORLDSURFACEWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PILE_HAY = PlacedFeature(feature='minecraft:pile_hay', placement=[])

PILE_ICE = PlacedFeature(feature='minecraft:pile_ice', placement=[])

PILE_MELON = PlacedFeature(feature='minecraft:pile_melon', placement=[])

PILE_PUMPKIN = PlacedFeature(feature='minecraft:pile_pumpkin', placement=[])

PILE_SNOW = PlacedFeature(feature='minecraft:pile_snow', placement=[])

PINE = PlacedFeature(
    feature='minecraft:pine',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PINE_CHECKED = PlacedFeature(
    feature='minecraft:pine',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

PINE_ON_SNOW = PlacedFeature(
    feature='minecraft:pine',
    placement=[
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=8,
            target_condition=BlockPredicateNot(
                predicate=BlockPredicateMatchingBlocks(blocks='minecraft:powder_snow', type='minecraft:matching_blocks'),
                type='minecraft:not',
            ),
            type='minecraft:environment_scan',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(
                offset=(0, -1, 0),
                blocks=['minecraft:snow_block', 'minecraft:powder_snow'],
                type='minecraft:matching_blocks',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

POINTED_DRIPSTONE = PlacedFeature(
    feature='minecraft:pointed_dripstone',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 256, 'min_inclusive': 192})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 1})),
            type='minecraft:count',
        ),
        PlacementModifierOffset(
            x=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 3.0, 'max_inclusive': 10, 'mean': 0.0, 'min_inclusive': -10}),
            ),
            y=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 0.6, 'max_inclusive': 2, 'mean': 0.0, 'min_inclusive': -2}),
            ),
            z=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 3.0, 'max_inclusive': 10, 'mean': 0.0, 'min_inclusive': -10}),
            ),
            type='minecraft:offset',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

RED_MUSHROOM_NETHER = PlacedFeature(
    feature='minecraft:red_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_MUSHROOM_NORMAL = PlacedFeature(
    feature='minecraft:red_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=512, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_MUSHROOM_OLD_GROWTH = PlacedFeature(
    feature='minecraft:red_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=171, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_MUSHROOM_SWAMP = PlacedFeature(
    feature='minecraft:red_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=64, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_MUSHROOM_TAIGA = PlacedFeature(
    feature='minecraft:red_mushroom',
    placement=[
        PlacementModifierRarityFilter(chance=256, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=96, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateBelowHeightmap(
                                heightmap=HeightmapType.MOTIONBLOCKING,
                                type='minecraft:below_heightmap',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, -1, 0),
                                tag='minecraft:overrides_mushroom_light_requirement',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_POPLAR = PlacedFeature(
    feature='minecraft:red_poplar',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

RED_POPLAR_LEAF_LITTER = PlacedFeature(
    feature='minecraft:red_poplar_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

ROOTED_AZALEA_TREE = PlacedFeature(
    feature='minecraft:rooted_azalea_tree',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

ROOTED_SULFUR_SPRING = PlacedFeature(
    feature='minecraft:rooted_sulfur_spring',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SCULK_PATCH_ANCIENT_CITY = PlacedFeature(feature='minecraft:sculk_patch_ancient_city', placement=[])

SCULK_PATCH_DEEP_DARK = PlacedFeature(
    feature='minecraft:sculk_patch_deep_dark',
    placement=[
        PlacementModifierCount(count=256, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SCULK_VEIN = PlacedFeature(
    feature='minecraft:sculk_vein',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 250, 'min_inclusive': 204})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_COLD = PlacedFeature(
    feature='minecraft:seagrass_short',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_DEEP = PlacedFeature(
    feature='minecraft:seagrass_tall',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=48, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_DEEP_COLD = PlacedFeature(
    feature='minecraft:seagrass_tall',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=40, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_DEEP_WARM = PlacedFeature(
    feature='minecraft:seagrass_tall',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=80, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_NORMAL = PlacedFeature(
    feature='minecraft:seagrass_short',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=48, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_RIVER = PlacedFeature(
    feature='minecraft:seagrass_slightly_less_short',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=48, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_SWAMP = PlacedFeature(
    feature='minecraft:seagrass_mid',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEAGRASS_WARM = PlacedFeature(
    feature='minecraft:seagrass_short',
    placement=[
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=80, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SEA_PICKLE = PlacedFeature(
    feature='minecraft:sea_pickle',
    placement=[
        PlacementModifierRarityFilter(chance=16, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SMALL_BASALT_COLUMNS = PlacedFeature(
    feature='minecraft:small_basalt_columns',
    placement=[
        PlacementModifierCountOnEveryLayer(count=4, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SNOW_LAYERS = PlacedFeature(
    feature='minecraft:snow_layer',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 24, 'min_inclusive': 16})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 4, 'min': -4, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=32,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPORE_BLOSSOM = PlacedFeature(
    feature='minecraft:spore_blossom',
    placement=[
        PlacementModifierCount(count=25, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=12,
            target_condition=BlockPredicateSolid(type='minecraft:solid'),
            allowed_search_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_CLOSED = PlacedFeature(
    feature='minecraft:spring_nether_closed',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_CLOSED_DOUBLE = PlacedFeature(
    feature='minecraft:spring_nether_closed',
    placement=[
        PlacementModifierCount(count=32, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=10),
                max_inclusive=VerticalAnchorStruct3(below_top=10),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_DELTA = PlacedFeature(
    feature='minecraft:spring_lava_nether',
    placement=[
        PlacementModifierCount(count=16, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=4),
                max_inclusive=VerticalAnchorStruct3(below_top=4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_LAVA = PlacedFeature(
    feature='minecraft:spring_lava_overworld',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructVeryBiasedToBottom(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=8),
                inner=8,
                type='minecraft:very_biased_to_bottom',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_LAVA_FROZEN = PlacedFeature(
    feature='minecraft:spring_lava_frozen',
    placement=[
        PlacementModifierCount(count=20, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructVeryBiasedToBottom(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=8),
                inner=8,
                type='minecraft:very_biased_to_bottom',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_OPEN = PlacedFeature(
    feature='minecraft:spring_nether_open',
    placement=[
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=4),
                max_inclusive=VerticalAnchorStruct3(below_top=4),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRING_WATER = PlacedFeature(
    feature='minecraft:spring_water',
    placement=[
        PlacementModifierCount(count=25, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=192),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SPRUCE = PlacedFeature(
    feature='minecraft:spruce',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

SPRUCE_CHECKED = PlacedFeature(
    feature='minecraft:spruce',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

SPRUCE_ON_SNOW = PlacedFeature(
    feature='minecraft:spruce',
    placement=[
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=8,
            target_condition=BlockPredicateNot(
                predicate=BlockPredicateMatchingBlocks(blocks='minecraft:powder_snow', type='minecraft:matching_blocks'),
                type='minecraft:not',
            ),
            type='minecraft:environment_scan',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(
                offset=(0, -1, 0),
                blocks=['minecraft:snow_block', 'minecraft:powder_snow'],
                type='minecraft:matching_blocks',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

SULFUR_POOL = PlacedFeature(
    feature='minecraft:sulfur_pool',
    placement=[
        PlacementModifierCount(count=256, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateSolid(type='minecraft:solid'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.UP,
            max_steps=32,
            target_condition=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlocks(blocks='minecraft:sulfur', type='minecraft:matching_blocks'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SULFUR_SPIKE = PlacedFeature(
    feature='minecraft:sulfur_spike',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 256, 'min_inclusive': 192})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 1})),
            type='minecraft:count',
        ),
        PlacementModifierOffset(
            x=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 3.0, 'max_inclusive': 10, 'mean': 0.0, 'min_inclusive': -10}),
            ),
            y=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 0.6, 'max_inclusive': 2, 'mean': 0.0, 'min_inclusive': -2}),
            ),
            z=IntProvider(
                type='minecraft:clamped_normal',
                **dict[str, Any]({'deviation': 3.0, 'max_inclusive': 10, 'mean': 0.0, 'min_inclusive': -10}),
            ),
            type='minecraft:offset',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SULFUR_SPIKE_CLUSTER = PlacedFeature(
    feature='minecraft:sulfur_spike_cluster',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 96, 'min_inclusive': 48})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

SUPER_BIRCH_BEES = PlacedFeature(
    feature='minecraft:super_birch_bees',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

SUPER_BIRCH_BEES_0002 = PlacedFeature(
    feature='minecraft:super_birch_bees_0002',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TALL_MANGROVE_CHECKED = PlacedFeature(
    feature='minecraft:tall_mangrove',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:mangrove_propagule', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_BADLANDS = PlacedFeature(
    feature='minecraft:trees_badlands',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 5, 'weight': 9}, {'data': 6, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_BIRCH = PlacedFeature(
    feature='minecraft:trees_birch',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:birch_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_BIRCH_AND_OAK_LEAF_LITTER = PlacedFeature(
    feature='minecraft:trees_birch_and_oak_leaf_litter',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_CHERRY = PlacedFeature(
    feature='minecraft:cherry_bees_005',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:cherry_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_DAPPLED_FOREST = PlacedFeature(
    feature='minecraft:trees_dappled_forest',
    placement=[
        PlacementModifierCount(count=6, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_FLOWER_FOREST = PlacedFeature(
    feature='minecraft:trees_flower_forest',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 6, 'weight': 9}, {'data': 7, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_GROVE = PlacedFeature(
    feature='minecraft:trees_grove',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_JUNGLE = PlacedFeature(
    feature='minecraft:trees_jungle',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 50, 'weight': 9}, {'data': 51, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_MANGROVE = PlacedFeature(
    feature='minecraft:mangrove_vegetation',
    placement=[
        PlacementModifierCount(count=25, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=5, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_MEADOW = PlacedFeature(
    feature='minecraft:meadow_trees',
    placement=[
        PlacementModifierRarityFilter(chance=100, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_OLD_GROWTH_PINE_TAIGA = PlacedFeature(
    feature='minecraft:trees_old_growth_pine_taiga',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_OLD_GROWTH_SPRUCE_TAIGA = PlacedFeature(
    feature='minecraft:trees_old_growth_spruce_taiga',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_PLAINS = PlacedFeature(
    feature='minecraft:trees_plains',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 0, 'weight': 19}, {'data': 1, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_SAVANNA = PlacedFeature(
    feature='minecraft:trees_savanna',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 1, 'weight': 9}, {'data': 2, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_SNOWY = PlacedFeature(
    feature='minecraft:trees_snowy',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 0, 'weight': 9}, {'data': 1, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:spruce_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_SPARSE_JUNGLE = PlacedFeature(
    feature='minecraft:trees_sparse_jungle',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 2, 'weight': 9}, {'data': 3, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_SWAMP = PlacedFeature(
    feature='minecraft:swamp_oak',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 2, 'weight': 9}, {'data': 3, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=2, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:oak_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

TREES_TAIGA = PlacedFeature(
    feature='minecraft:trees_taiga',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 10, 'weight': 9}, {'data': 11, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_WATER = PlacedFeature(
    feature='minecraft:trees_water',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 0, 'weight': 9}, {'data': 1, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_WINDSWEPT_FOREST = PlacedFeature(
    feature='minecraft:trees_windswept_hills',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 3, 'weight': 9}, {'data': 4, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_WINDSWEPT_HILLS = PlacedFeature(
    feature='minecraft:trees_windswept_hills',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 0, 'weight': 9}, {'data': 1, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TREES_WINDSWEPT_SAVANNA = PlacedFeature(
    feature='minecraft:trees_savanna',
    placement=[
        PlacementModifierCount(
            count=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 2, 'weight': 9}, {'data': 3, 'weight': 1}]}),
            ),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierSurfaceWaterDepthFilter(max_water_depth=0, type='minecraft:surface_water_depth_filter'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOOR, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

TWISTING_VINES = PlacedFeature(
    feature='minecraft:twisting_vines',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks=['minecraft:netherrack', 'minecraft:warped_nylium', 'minecraft:warped_wart_block'],
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 8, 'min_inclusive': -8})),
            y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': -4})),
            z=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 8, 'min_inclusive': -8})),
            type='minecraft:offset',
        ),
        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
        PlacementModifierEnvironmentScan(
            direction_of_search=VerticalDirection.DOWN,
            max_steps=32,
            target_condition=BlockPredicateNot(
                predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                type='minecraft:not',
            ),
            type='minecraft:environment_scan',
        ),
        PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks=['minecraft:netherrack', 'minecraft:warped_nylium', 'minecraft:warped_wart_block'],
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

UNDERWATER_MAGMA = PlacedFeature(
    feature='minecraft:underwater_magma',
    placement=[
        PlacementModifierCount(
            count=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 52, 'min_inclusive': 44})),
            type='minecraft:count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct1(absolute=256),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierSurfaceRelativeThresholdFilter(
            heightmap=HeightmapType.OCEANFLOORWORLDGEN,
            max_inclusive=-2,
            type='minecraft:surface_relative_threshold_filter',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

VINES = PlacedFeature(
    feature='minecraft:vines',
    placement=[
        PlacementModifierCount(count=127, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct1(absolute=64),
                max_inclusive=VerticalAnchorStruct1(absolute=100),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

VOID_START_PLATFORM = PlacedFeature(feature='minecraft:void_start_platform', placement=[PlacementModifierBiome(type='minecraft:biome')])

WARM_OCEAN_VEGETATION = PlacedFeature(
    feature='minecraft:warm_ocean_vegetation',
    placement=[
        PlacementModifierNoiseBasedCount(
            noise_to_count_ratio=20,
            noise_factor=400.0,
            type='minecraft:noise_based_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.OCEANFLOORWORLDGEN, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

WARPED_FOREST_VEGETATION = PlacedFeature(
    feature='minecraft:warped_forest_vegetation',
    placement=[
        PlacementModifierCountOnEveryLayer(count=5, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(
                offset=(0, -1, 0),
                tag='minecraft:nylium',
                type='minecraft:matching_block_tag',
            ),
            type='minecraft:block_predicate_filter',
        ),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

WARPED_FUNGI = PlacedFeature(
    feature='minecraft:warped_fungus',
    placement=[
        PlacementModifierCountOnEveryLayer(count=8, type='minecraft:count_on_every_layer'),
        PlacementModifierBiome(type='minecraft:biome'),
    ],
)

WEEPING_VINES = PlacedFeature(
    feature='minecraft:weeping_vines',
    placement=[
        PlacementModifierCount(count=10, type='minecraft:count'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightRange(
            height=HeightProviderStructUniform(
                min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                max_inclusive=VerticalAnchorStruct3(below_top=0),
                type='minecraft:uniform',
            ),
            type='minecraft:height_range',
        ),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateAllOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlocks(
                        offset=(0, 1, 0),
                        blocks=['minecraft:netherrack', 'minecraft:nether_wart_block'],
                        type='minecraft:matching_blocks',
                    ),
                ],
                type='minecraft:all_of',
            ),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

WILDFLOWERS_BIRCH_FOREST = PlacedFeature(
    feature='minecraft:wildflower',
    placement=[
        PlacementModifierCount(count=3, type='minecraft:count'),
        PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=64, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

WILDFLOWERS_MEADOW = PlacedFeature(
    feature='minecraft:wildflower',
    placement=[
        PlacementModifierNoiseThresholdCount(
            noise_level=-0.8,
            below_noise=5,
            above_noise=10,
            type='minecraft:noise_threshold_count',
        ),
        PlacementModifierInSquare(type='minecraft:in_square'),
        PlacementModifierHeightmap(heightmap=HeightmapType.MOTIONBLOCKING, type='minecraft:heightmap'),
        PlacementModifierBiome(type='minecraft:biome'),
        PlacementModifierCount(count=8, type='minecraft:count'),
        PlacementModifierOffset(
            x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0})),
            z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 6, 'min': -6, 'plateau': 0})),
            type='minecraft:offset',
        ),
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

YELLOW_POPLAR = PlacedFeature(
    feature='minecraft:yellow_poplar',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)

YELLOW_POPLAR_LEAF_LITTER = PlacedFeature(
    feature='minecraft:yellow_poplar_leaf_litter',
    placement=[
        PlacementModifierBlockPredicateFilter(
            predicate=BlockPredicateWouldSurvive(state='minecraft:poplar_sapling', type='minecraft:would_survive'),
            type='minecraft:block_predicate_filter',
        ),
    ],
)
