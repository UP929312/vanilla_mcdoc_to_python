"""Vanilla's data/worldgen/feature/ files"""
from typing import Any
from vanilla_mcdoc.data.worldgen.CaveSurface import CaveSurface
from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
from vanilla_mcdoc.data.worldgen.UniformIntProvider import UniformIntProvider
from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchorStruct2, VerticalAnchorStruct4
from vanilla_mcdoc.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
from vanilla_mcdoc.data.worldgen.feature.ConfiguredFeature import ConfiguredFeatureBamboo, ConfiguredFeatureBlockBlob, ConfiguredFeatureBlockColumn, ConfiguredFeatureBlockPile, ConfiguredFeatureBlueIce, ConfiguredFeatureBonusChest, ConfiguredFeatureChorusPlant, ConfiguredFeatureCoralClaw, ConfiguredFeatureCoralTree, ConfiguredFeatureCrevasse, ConfiguredFeatureDeltaFeature, ConfiguredFeatureDisk, ConfiguredFeatureEndGateway, ConfiguredFeatureEndIsland, ConfiguredFeatureEndPlatform, ConfiguredFeatureEndPodium, ConfiguredFeatureEndSpike, ConfiguredFeatureFallenTree, ConfiguredFeatureFossil, ConfiguredFeatureFreezeTopLayer, ConfiguredFeatureGeode, ConfiguredFeatureHugeBrownMushroom, ConfiguredFeatureHugeFungus, ConfiguredFeatureHugeRedMushroom, ConfiguredFeatureIceberg, ConfiguredFeatureLake, ConfiguredFeatureLargeSpeleothem, ConfiguredFeatureMonsterRoom, ConfiguredFeatureMultifaceGrowth, ConfiguredFeatureNetherrackReplaceBlobs, ConfiguredFeatureNoOp, ConfiguredFeatureOre, ConfiguredFeatureOverlay, ConfiguredFeatureProjectedRandomPatchySquare, ConfiguredFeatureRandomBooleanSelector, ConfiguredFeatureRandomNeighborSpread, ConfiguredFeatureRandomSelector, ConfiguredFeatureRootSystem, ConfiguredFeatureScatteredOre, ConfiguredFeatureSculkPatch, ConfiguredFeatureSequence, ConfiguredFeatureSimpleBlock, ConfiguredFeatureSimpleRandomSelector, ConfiguredFeatureSingleBlockPillar, ConfiguredFeatureSpeleothem, ConfiguredFeatureSpeleothemCluster, ConfiguredFeatureSpike, ConfiguredFeatureSpringFeature, ConfiguredFeatureSteppedColumnCluster, ConfiguredFeatureTemplate, ConfiguredFeatureTree, ConfiguredFeatureUnderwaterMagma, ConfiguredFeatureVegetationPatch, ConfiguredFeatureVines, ConfiguredFeatureVoidStartPlatform, ConfiguredFeatureWaterloggedVegetationPatch, ConfiguredFeatureWeightedRandomSelector
from vanilla_mcdoc.data.worldgen.feature.GeodeBlockSettings import GeodeBlockSettings
from vanilla_mcdoc.data.worldgen.feature.GeodeCrackSettings import GeodeCrackSettings
from vanilla_mcdoc.data.worldgen.feature.GeodeLayerSettings import GeodeLayerSettings
from vanilla_mcdoc.data.worldgen.feature.MultifaceBlock import MultifaceBlock
from vanilla_mcdoc.data.worldgen.feature.RandomSelector import FeaturesStruct
from vanilla_mcdoc.data.worldgen.feature.RuleBasedBlockStateProvider import RulesStruct
from vanilla_mcdoc.data.worldgen.feature.SpeleothemBaseBlockTransformer import SpeleothemBaseBlockTransformer
from vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterConfig import PlacementOptionsStruct
from vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementMode import SpeleothemClusterPlacementMode
from vanilla_mcdoc.data.worldgen.feature.TargetBlock import TargetBlock
from vanilla_mcdoc.data.worldgen.feature.TemplateEntry import TemplateEntry
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateAllOf, BlockPredicateAnyOf, BlockPredicateHasSturdyFace, BlockPredicateHeightRange, BlockPredicateMatchingBlockTag, BlockPredicateMatchingBlocks, BlockPredicateMatchingFluids, BlockPredicateNot, BlockPredicateSolid, BlockPredicateTrue
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.TypedBlockStateProvider import TypedBlockStateProviderRandomizedInt, TypedBlockStateProviderRotated, TypedBlockStateProviderRuleBased, TypedBlockStateProviderWeighted
from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature
from vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier import PlacementModifierBlockPredicateFilter, PlacementModifierCount, PlacementModifierCuboid, PlacementModifierEnvironmentScan, PlacementModifierOffset, PlacementModifierRandomChance, PlacementModifierRandomlySelected, PlacementModifierRarityFilter
from vanilla_mcdoc.data.worldgen.feature.tree.AboveRootPlacement import AboveRootPlacement
from vanilla_mcdoc.data.worldgen.feature.tree.FeatureSize import FeatureSizeThreeLayersFeatureSize, FeatureSizeTwoLayersFeatureSize
from vanilla_mcdoc.data.worldgen.feature.tree.FoliagePlacer import FoliagePlacerAcaciaFoliagePlacer, FoliagePlacerBlobFoliagePlacer, FoliagePlacerBushFoliagePlacer, FoliagePlacerCherryFoliagePlacer, FoliagePlacerDarkOakFoliagePlacer, FoliagePlacerFancyFoliagePlacer, FoliagePlacerJungleFoliagePlacer, FoliagePlacerMegaPineFoliagePlacer, FoliagePlacerPineFoliagePlacer, FoliagePlacerPoplarFoliagePlacer, FoliagePlacerRandomSpreadFoliagePlacer, FoliagePlacerSpruceFoliagePlacer
from vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacement import MangroveRootPlacement
from vanilla_mcdoc.data.worldgen.feature.tree.RootPlacer import RootPlacerMangroveRootPlacer
from vanilla_mcdoc.data.worldgen.feature.tree.TreeDecorator import TreeDecoratorAlterGround, TreeDecoratorAttachedToLeaves, TreeDecoratorAttachedToLogs, TreeDecoratorBeehive, TreeDecoratorCocoa, TreeDecoratorCreakingHeart, TreeDecoratorLeaveVine, TreeDecoratorPaleMoss, TreeDecoratorPlaceOnGround, TreeDecoratorShelfMushroom, TreeDecoratorTrunkVine
from vanilla_mcdoc.data.worldgen.feature.tree.TrunkPlacer import TrunkPlacerBendingTrunkPlacer, TrunkPlacerCherryTrunkPlacer, TrunkPlacerDarkOakTrunkPlacer, TrunkPlacerFancyTrunkPlacer, TrunkPlacerForkingTrunkPlacer, TrunkPlacerGiantTrunkPlacer, TrunkPlacerMegaJungleTrunkPlacer, TrunkPlacerPoplarTrunkPlacer, TrunkPlacerStraightTrunkPlacer, TrunkPlacerUpwardsBranchingTrunkPlacer
from vanilla_mcdoc.data.worldgen.processor_list.BlockEntityModifier import BlockEntityModifierAppendLoot
from vanilla_mcdoc.data.worldgen.processor_list.Processor import ProcessorRule2
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorListStruct
from vanilla_mcdoc.data.worldgen.processor_list.ProcessorRule import ProcessorRule
from vanilla_mcdoc.data.worldgen.processor_list.RuleTest import RuleTestAllOf, RuleTestAlwaysTrue, RuleTestAnyOf, RuleTestBlockMatch, RuleTestHeightMatch, RuleTestNot, RuleTestTagMatch
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState
from vanilla_mcdoc.util.direction.Direction import Direction
from vanilla_mcdoc.util.direction.VerticalDirection import VerticalDirection
from vanilla_mcdoc.util.fluid_state.FluidState import FluidStateStruct

ACACIA = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:acacia_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:acacia_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerForkingTrunkPlacer(
        type='minecraft:forking_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=2,
    ),
    foliage_placer=FoliagePlacerAcaciaFoliagePlacer(type='minecraft:acacia_foliage_placer', radius=2, offset=0),
    decorators=[],
    type='minecraft:tree',
)

AMETHYST_GEODE = ConfiguredFeatureGeode(
    blocks=GeodeBlockSettings(
        filling_provider=FullBlockState(id='minecraft:air'),
        inner_layer_provider=FullBlockState(id='minecraft:amethyst_block'),
        alternate_inner_layer_provider=FullBlockState(id='minecraft:budding_amethyst'),
        middle_layer_provider=FullBlockState(id='minecraft:calcite'),
        outer_layer_provider=FullBlockState(id='minecraft:smooth_basalt'),
        inner_placements=[
            'minecraft:small_amethyst_bud',
            'minecraft:medium_amethyst_bud',
            'minecraft:large_amethyst_bud',
            'minecraft:amethyst_cluster',
        ],
        cannot_replace='#minecraft:features_cannot_replace',
        invalid_blocks='#minecraft:geode_invalid_blocks',
    ),
    layers=GeodeLayerSettings(),
    crack=GeodeCrackSettings(generate_crack_chance=0.95),
    use_alternate_layer0_chance=0.083,
    outer_wall_distance=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
    invalid_blocks_threshold=1,
    type='minecraft:geode',
)

AZALEA_TREE = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider=FullBlockState(id='minecraft:rooted_dirt'),
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=3, data='minecraft:azalea_leaves'),
            WeightedEntry(weight=1, data='minecraft:flowering_azalea_leaves'),
        ],
        type='minecraft:weighted',
    ),
    trunk_placer=TrunkPlacerBendingTrunkPlacer(
        bend_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
        min_height_for_leaves=3,
        type='minecraft:bending_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerRandomSpreadFoliagePlacer(
        foliage_height=2,
        leaf_placement_attempts=50,
        type='minecraft:random_spread_foliage_placer',
        radius=3,
        offset=0,
    ),
    decorators=[],
    type='minecraft:tree',
)

BAMBOO_NO_PODZOL = ConfiguredFeatureBamboo(probability=0.0, type='minecraft:bamboo')

BAMBOO_SOME_PODZOL = ConfiguredFeatureBamboo(probability=0.2, type='minecraft:bamboo')

BAMBOO_VEGETATION = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.05, feature='minecraft:fancy_oak_checked'),
        FeaturesStruct(chance=0.15, feature='minecraft:jungle_bush'),
        FeaturesStruct(chance=0.7, feature='minecraft:mega_jungle_tree_checked'),
    ],
    default=PlacedFeature(
        feature='minecraft:grass_jungle',
        placement=[
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
    ),
    type='minecraft:random_selector',
)

BASALT_BLOBS = ConfiguredFeatureNetherrackReplaceBlobs(
    state='minecraft:basalt',
    target='minecraft:netherrack',
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 3})),
    type='minecraft:netherrack_replace_blobs',
)

BASALT_PILLAR = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSingleBlockPillar(
                block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                direction=VerticalDirection.DOWN,
                cap_feature=PlacedFeature(
                    feature=ConfiguredFeatureOverlay(
                        features=[
                            PlacedFeature(
                                feature=ConfiguredFeatureProjectedRandomPatchySquare(
                                    block=TypedBlockStateProviderRuleBased(
                                        rules=[
                                            RulesStruct(
                                                if_true=BlockPredicateNot(
                                                    predicate=BlockPredicateMatchingBlockTag(
                                                        offset=(0, -1, 0),
                                                        tag='minecraft:air',
                                                        type='minecraft:matching_block_tag',
                                                    ),
                                                    type='minecraft:not',
                                                ),
                                                then=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                                            ),
                                        ],
                                        type='minecraft:rule_based',
                                    ),
                                    project_through=BlockPredicateMatchingBlockTag(
                                        tag='minecraft:air',
                                        type='minecraft:matching_block_tag',
                                    ),
                                    size=3,
                                    max_projection_height=3,
                                    type='minecraft:projected_random_patchy_square',
                                ),
                                placement=[PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset')],
                            ),
                            PlacedFeature(
                                feature=ConfiguredFeatureSimpleBlock(
                                    to_place=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                                    type='minecraft:simple_block',
                                ),
                                placement=[
                                    PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
                                    PlacementModifierOffset(x=1, y=0, z=0, type='minecraft:offset'),
                                ],
                            ),
                            PlacedFeature(
                                feature=ConfiguredFeatureSimpleBlock(
                                    to_place=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                                    type='minecraft:simple_block',
                                ),
                                placement=[
                                    PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
                                    PlacementModifierOffset(x=-1, y=0, z=0, type='minecraft:offset'),
                                ],
                            ),
                            PlacedFeature(
                                feature=ConfiguredFeatureSimpleBlock(
                                    to_place=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                                    type='minecraft:simple_block',
                                ),
                                placement=[
                                    PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
                                    PlacementModifierOffset(x=0, y=0, z=1, type='minecraft:offset'),
                                ],
                            ),
                            PlacedFeature(
                                feature=ConfiguredFeatureSimpleBlock(
                                    to_place=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                                    type='minecraft:simple_block',
                                ),
                                placement=[
                                    PlacementModifierRarityFilter(chance=2, type='minecraft:rarity_filter'),
                                    PlacementModifierOffset(x=0, y=0, z=-1, type='minecraft:offset'),
                                ],
                            ),
                        ],
                        type='minecraft:overlay',
                    ),
                    placement=[],
                ),
                type='minecraft:single_block_pillar',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSingleBlockPillar(
                block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                direction=VerticalDirection.DOWN,
                chance_to_continue=0.9,
                type='minecraft:single_block_pillar',
            ),
            placement=[PlacementModifierOffset(x=1, y=0, z=0, type='minecraft:offset')],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSingleBlockPillar(
                block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                direction=VerticalDirection.DOWN,
                chance_to_continue=0.9,
                type='minecraft:single_block_pillar',
            ),
            placement=[PlacementModifierOffset(x=-1, y=0, z=0, type='minecraft:offset')],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSingleBlockPillar(
                block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                direction=VerticalDirection.DOWN,
                chance_to_continue=0.9,
                type='minecraft:single_block_pillar',
            ),
            placement=[PlacementModifierOffset(x=0, y=0, z=1, type='minecraft:offset')],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSingleBlockPillar(
                block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                direction=VerticalDirection.DOWN,
                chance_to_continue=0.9,
                type='minecraft:single_block_pillar',
            ),
            placement=[PlacementModifierOffset(x=0, y=0, z=-1, type='minecraft:offset')],
        ),
    ],
    type='minecraft:overlay',
)

BERRY_BUSH = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:sweet_berry_bush', properties={'age': '3'}),
    type='minecraft:simple_block',
)

BIRCH = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[],
    type='minecraft:tree',
)

BIRCH_BEES_0002 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.002, type='minecraft:beehive')],
    type='minecraft:tree',
)

BIRCH_BEES_0002_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorBeehive(probability=0.002, type='minecraft:beehive'),
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

BIRCH_BEES_002 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.02, type='minecraft:beehive')],
    type='minecraft:tree',
)

BIRCH_BEES_005 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.05, type='minecraft:beehive')],
    type='minecraft:tree',
)

BIRCH_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

BIRCH_TALL = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.00625, feature='minecraft:fallen_super_birch_tree'),
        FeaturesStruct(chance=0.5, feature='minecraft:super_birch_bees_0002'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_birch_tree'),
    ],
    default='minecraft:birch_bees_0002',
    type='minecraft:random_selector',
)

BLACKSTONE_BLOBS = ConfiguredFeatureNetherrackReplaceBlobs(
    state='minecraft:blackstone',
    target='minecraft:netherrack',
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 3})),
    type='minecraft:netherrack_replace_blobs',
)

BLUE_ICE = ConfiguredFeatureBlueIce(type='minecraft:blue_ice')

BONUS_CHEST = ConfiguredFeatureBonusChest(type='minecraft:bonus_chest')

BROWN_MUSHROOM = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:brown_mushroom'), type='minecraft:simple_block')

BUSH = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:bush'), type='minecraft:simple_block')

CACTUS = ConfiguredFeatureBlockColumn(
    direction=Direction.UP,
    allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    prioritize_tip=False,
    layers=[
        BlockColumnLayer(
            height=IntProvider(type='minecraft:biased_to_bottom', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 1})),
            provider=FullBlockState(id='minecraft:cactus', properties={'age': '0'}),
        ),
        BlockColumnLayer(
            height=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({'distribution': [{'data': 0, 'weight': 3}, {'data': 1, 'weight': 1}]}),
            ),
            provider=FullBlockState(id='minecraft:cactus_flower'),
        ),
    ],
    type='minecraft:block_column',
)

CAVE_VINE = ConfiguredFeatureBlockColumn(
    direction=Direction.DOWN,
    allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    prioritize_tip=True,
    layers=[
        BlockColumnLayer(
            height=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({
                    'distribution': [
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 19, 'min_inclusive': 0}, 'weight': 2},
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 2, 'min_inclusive': 0}, 'weight': 3},
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 6, 'min_inclusive': 0}, 'weight': 10},
                    ],
                }),
            ),
            provider='minecraft:cave_vines_body',
        ),
        BlockColumnLayer(height=1, provider='minecraft:cave_vines_head'),
    ],
    type='minecraft:block_column',
)

CAVE_VINE_IN_MOSS = ConfiguredFeatureBlockColumn(
    direction=Direction.DOWN,
    allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    prioritize_tip=True,
    layers=[
        BlockColumnLayer(
            height=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({
                    'distribution': [
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 3, 'min_inclusive': 0}, 'weight': 5},
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 7, 'min_inclusive': 1}, 'weight': 1},
                    ],
                }),
            ),
            provider='minecraft:cave_vines_body',
        ),
        BlockColumnLayer(height=1, provider='minecraft:cave_vines_head'),
    ],
    type='minecraft:block_column',
)

CHERRY = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:cherry_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:cherry_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerCherryTrunkPlacer(
        branch_count=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({'distribution': [{'data': 1, 'weight': 1}, {'data': 2, 'weight': 1}, {'data': 3, 'weight': 1}]}),
        ),
        branch_horizontal_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
        branch_start_offset_from_top=UniformIntProvider(min_inclusive=-4, max_inclusive=-3),
        branch_end_offset_from_top=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 0, 'min_inclusive': -1})),
        type='minecraft:cherry_trunk_placer',
        base_height=7,
        height_rand_a=1,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerCherryFoliagePlacer(
        height=5,
        wide_bottom_layer_hole_chance=0.25,
        corner_hole_chance=0.25,
        hanging_leaves_chance=0.16666667,
        hanging_leaves_extension_chance=0.33333334,
        type='minecraft:cherry_foliage_placer',
        radius=4,
        offset=0,
    ),
    decorators=[],
    type='minecraft:tree',
)

CHERRY_BEES_005 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:cherry_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:cherry_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerCherryTrunkPlacer(
        branch_count=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({'distribution': [{'data': 1, 'weight': 1}, {'data': 2, 'weight': 1}, {'data': 3, 'weight': 1}]}),
        ),
        branch_horizontal_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
        branch_start_offset_from_top=UniformIntProvider(min_inclusive=-4, max_inclusive=-3),
        branch_end_offset_from_top=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 0, 'min_inclusive': -1})),
        type='minecraft:cherry_trunk_placer',
        base_height=7,
        height_rand_a=1,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerCherryFoliagePlacer(
        height=5,
        wide_bottom_layer_hole_chance=0.25,
        corner_hole_chance=0.25,
        hanging_leaves_chance=0.16666667,
        hanging_leaves_extension_chance=0.33333334,
        type='minecraft:cherry_foliage_placer',
        radius=4,
        offset=0,
    ),
    decorators=[TreeDecoratorBeehive(probability=0.05, type='minecraft:beehive')],
    type='minecraft:tree',
)

CHORUS_PLANT = ConfiguredFeatureChorusPlant(type='minecraft:chorus_plant')

CLAY_POOL_WITH_DRIPLEAVES = ConfiguredFeatureWaterloggedVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=3,
    vertical_range=5,
    extra_bottom_block_chance=0.8,
    extra_edge_column_chance=0.7,
    vegetation_chance=0.1,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    replaceable='#minecraft:lush_ground_replaceable',
    ground_state=FullBlockState(id='minecraft:clay'),
    vegetation_feature=PlacedFeature(feature='minecraft:dripleaf', placement=[]),
    type='minecraft:waterlogged_vegetation_patch',
)

CLAY_WITH_DRIPLEAVES = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=3,
    vertical_range=2,
    extra_bottom_block_chance=0.8,
    extra_edge_column_chance=0.7,
    vegetation_chance=0.05,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    replaceable='#minecraft:lush_ground_replaceable',
    ground_state=FullBlockState(id='minecraft:clay'),
    vegetation_feature=PlacedFeature(feature='minecraft:dripleaf', placement=[]),
    type='minecraft:vegetation_patch',
)

CRIMSON_FOREST_VEGETATION = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=87, data='minecraft:crimson_roots'),
            WeightedEntry(weight=11, data='minecraft:crimson_fungus'),
            WeightedEntry(weight=1, data='minecraft:warped_fungus'),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

CRIMSON_FUNGUS = ConfiguredFeatureHugeFungus(
    hat_state='minecraft:nether_wart_block',
    decor_state='minecraft:shroomlight',
    stem_state='minecraft:crimson_stem',
    valid_base_block='minecraft:crimson_nylium',
    replaceable_blocks=BlockPredicateMatchingBlocks(
        blocks=[
            'minecraft:oak_sapling',
            'minecraft:spruce_sapling',
            'minecraft:birch_sapling',
            'minecraft:jungle_sapling',
            'minecraft:acacia_sapling',
            'minecraft:cherry_sapling',
            'minecraft:dark_oak_sapling',
            'minecraft:pale_oak_sapling',
            'minecraft:mangrove_propagule',
            'minecraft:dandelion',
            'minecraft:torchflower',
            'minecraft:poppy',
            'minecraft:blue_orchid',
            'minecraft:allium',
            'minecraft:azure_bluet',
            'minecraft:red_tulip',
            'minecraft:orange_tulip',
            'minecraft:white_tulip',
            'minecraft:pink_tulip',
            'minecraft:oxeye_daisy',
            'minecraft:cornflower',
            'minecraft:wither_rose',
            'minecraft:lily_of_the_valley',
            'minecraft:brown_mushroom',
            'minecraft:red_mushroom',
            'minecraft:wheat',
            'minecraft:sugar_cane',
            'minecraft:attached_pumpkin_stem',
            'minecraft:attached_melon_stem',
            'minecraft:pumpkin_stem',
            'minecraft:melon_stem',
            'minecraft:lily_pad',
            'minecraft:nether_wart',
            'minecraft:cocoa',
            'minecraft:carrots',
            'minecraft:potatoes',
            'minecraft:chorus_plant',
            'minecraft:chorus_flower',
            'minecraft:torchflower_crop',
            'minecraft:pitcher_crop',
            'minecraft:beetroots',
            'minecraft:sweet_berry_bush',
            'minecraft:warped_fungus',
            'minecraft:crimson_fungus',
            'minecraft:weeping_vines',
            'minecraft:weeping_vines_plant',
            'minecraft:twisting_vines',
            'minecraft:twisting_vines_plant',
            'minecraft:cave_vines',
            'minecraft:cave_vines_plant',
            'minecraft:spore_blossom',
            'minecraft:azalea',
            'minecraft:flowering_azalea',
            'minecraft:moss_carpet',
            'minecraft:pink_petals',
            'minecraft:wildflowers',
            'minecraft:big_dripleaf',
            'minecraft:big_dripleaf_stem',
            'minecraft:small_dripleaf',
        ],
        type='minecraft:matching_blocks',
    ),
    type='minecraft:huge_fungus',
)

CRIMSON_FUNGUS_PLANTED = ConfiguredFeatureHugeFungus(
    hat_state='minecraft:nether_wart_block',
    decor_state='minecraft:shroomlight',
    stem_state='minecraft:crimson_stem',
    valid_base_block='minecraft:crimson_nylium',
    planted=True,
    replaceable_blocks=BlockPredicateMatchingBlocks(
        blocks=[
            'minecraft:oak_sapling',
            'minecraft:spruce_sapling',
            'minecraft:birch_sapling',
            'minecraft:jungle_sapling',
            'minecraft:acacia_sapling',
            'minecraft:cherry_sapling',
            'minecraft:dark_oak_sapling',
            'minecraft:pale_oak_sapling',
            'minecraft:mangrove_propagule',
            'minecraft:dandelion',
            'minecraft:torchflower',
            'minecraft:poppy',
            'minecraft:blue_orchid',
            'minecraft:allium',
            'minecraft:azure_bluet',
            'minecraft:red_tulip',
            'minecraft:orange_tulip',
            'minecraft:white_tulip',
            'minecraft:pink_tulip',
            'minecraft:oxeye_daisy',
            'minecraft:cornflower',
            'minecraft:wither_rose',
            'minecraft:lily_of_the_valley',
            'minecraft:brown_mushroom',
            'minecraft:red_mushroom',
            'minecraft:wheat',
            'minecraft:sugar_cane',
            'minecraft:attached_pumpkin_stem',
            'minecraft:attached_melon_stem',
            'minecraft:pumpkin_stem',
            'minecraft:melon_stem',
            'minecraft:lily_pad',
            'minecraft:nether_wart',
            'minecraft:cocoa',
            'minecraft:carrots',
            'minecraft:potatoes',
            'minecraft:chorus_plant',
            'minecraft:chorus_flower',
            'minecraft:torchflower_crop',
            'minecraft:pitcher_crop',
            'minecraft:beetroots',
            'minecraft:sweet_berry_bush',
            'minecraft:warped_fungus',
            'minecraft:crimson_fungus',
            'minecraft:weeping_vines',
            'minecraft:weeping_vines_plant',
            'minecraft:twisting_vines',
            'minecraft:twisting_vines_plant',
            'minecraft:cave_vines',
            'minecraft:cave_vines_plant',
            'minecraft:spore_blossom',
            'minecraft:azalea',
            'minecraft:flowering_azalea',
            'minecraft:moss_carpet',
            'minecraft:pink_petals',
            'minecraft:wildflowers',
            'minecraft:big_dripleaf',
            'minecraft:big_dripleaf_stem',
            'minecraft:small_dripleaf',
        ],
        type='minecraft:matching_blocks',
    ),
    type='minecraft:huge_fungus',
)

CRIMSON_ROOTS = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:crimson_roots'), type='minecraft:simple_block')

DARK_FOREST_VEGETATION = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.025, feature=PlacedFeature(feature='minecraft:huge_brown_mushroom', placement=[])),
        FeaturesStruct(chance=0.05, feature=PlacedFeature(feature='minecraft:huge_red_mushroom', placement=[])),
        FeaturesStruct(chance=0.6666667, feature='minecraft:dark_oak_leaf_litter'),
        FeaturesStruct(chance=0.0025, feature='minecraft:fallen_birch_tree'),
        FeaturesStruct(chance=0.2, feature='minecraft:birch_leaf_litter'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree'),
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_leaf_litter'),
    ],
    default='minecraft:oak_leaf_litter',
    type='minecraft:random_selector',
)

DARK_OAK = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeThreeLayersFeatureSize(upper_size=2, type='minecraft:three_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:dark_oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:dark_oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerDarkOakTrunkPlacer(
        type='minecraft:dark_oak_trunk_placer',
        base_height=6,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerDarkOakFoliagePlacer(type='minecraft:dark_oak_foliage_placer', radius=0, offset=0),
    decorators=[],
    type='minecraft:tree',
)

DARK_OAK_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeThreeLayersFeatureSize(upper_size=2, type='minecraft:three_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:dark_oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:dark_oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerDarkOakTrunkPlacer(
        type='minecraft:dark_oak_trunk_placer',
        base_height=6,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerDarkOakFoliagePlacer(type='minecraft:dark_oak_foliage_placer', radius=0, offset=0),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

DEAD_BUSH = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:dead_bush'), type='minecraft:simple_block')

DELTA = ConfiguredFeatureDeltaFeature(
    contents='minecraft:lava',
    rim='minecraft:magma_block',
    size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 3})),
    rim_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 0})),
    type='minecraft:delta_feature',
)

DESERT_WELL = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureTemplate(
                templates=[WeightedEntry(weight=1, data=TemplateEntry(id='minecraft:desert_well/well'))],
                type='minecraft:template',
            ),
            placement=[PlacementModifierOffset(x=0, y=-2, z=0, type='minecraft:offset')],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureTemplate(
                templates=[WeightedEntry(weight=1, data=TemplateEntry(id='minecraft:desert_well/suspicious_sand'))],
                processors=ProcessorListStruct(
                    processors=[
                        ProcessorRule2(
                            rules=[
                                ProcessorRule(
                                    location_predicate=RuleTestAlwaysTrue(predicate_type='minecraft:always_true'),
                                    input_predicate=RuleTestBlockMatch(
                                        block='minecraft:suspicious_sand',
                                        predicate_type='minecraft:block_match',
                                    ),
                                    output_state='minecraft:suspicious_sand',
                                    block_entity_modifier=BlockEntityModifierAppendLoot(
                                        loot_table='minecraft:archaeology/desert_well',
                                        type='minecraft:append_loot',
                                    ),
                                ),
                            ],
                            processor_type='minecraft:rule',
                        ),
                    ],
                ),
                type='minecraft:template',
            ),
            placement=[
                PlacementModifierRandomlySelected(
                    placements=[
                        PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=-1, y=-1, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=0, y=-1, z=1, type='minecraft:offset'),
                        PlacementModifierOffset(x=1, y=-1, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=0, y=-1, z=-1, type='minecraft:offset'),
                    ],
                    type='minecraft:randomly_selected',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureTemplate(
                templates=[WeightedEntry(weight=1, data=TemplateEntry(id='minecraft:desert_well/suspicious_sand'))],
                processors=ProcessorListStruct(
                    processors=[
                        ProcessorRule2(
                            rules=[
                                ProcessorRule(
                                    location_predicate=RuleTestAlwaysTrue(predicate_type='minecraft:always_true'),
                                    input_predicate=RuleTestBlockMatch(
                                        block='minecraft:suspicious_sand',
                                        predicate_type='minecraft:block_match',
                                    ),
                                    output_state='minecraft:suspicious_sand',
                                    block_entity_modifier=BlockEntityModifierAppendLoot(
                                        loot_table='minecraft:archaeology/desert_well',
                                        type='minecraft:append_loot',
                                    ),
                                ),
                            ],
                            processor_type='minecraft:rule',
                        ),
                    ],
                ),
                type='minecraft:template',
            ),
            placement=[
                PlacementModifierRandomlySelected(
                    placements=[
                        PlacementModifierOffset(x=0, y=-2, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=-1, y=-2, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=0, y=-2, z=1, type='minecraft:offset'),
                        PlacementModifierOffset(x=1, y=-2, z=0, type='minecraft:offset'),
                        PlacementModifierOffset(x=0, y=-2, z=-1, type='minecraft:offset'),
                    ],
                    type='minecraft:randomly_selected',
                ),
            ],
        ),
    ],
    type='minecraft:overlay',
)

DISK_CLAY = ConfiguredFeatureDisk(
    state_provider=FullBlockState(id='minecraft:clay'),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
    half_height=1,
    target=BlockPredicateMatchingBlocks(blocks=['minecraft:dirt', 'minecraft:clay'], type='minecraft:matching_blocks'),
    type='minecraft:disk',
)

DISK_GRASS = ConfiguredFeatureDisk(
    state_provider=TypedBlockStateProviderRuleBased(
        fallback=FullBlockState(id='minecraft:dirt'),
        rules=[
            RulesStruct(
                if_true=BlockPredicateNot(
                    predicate=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateSolid(type='minecraft:solid', **dict[str, Any]({'offset': [0, 1, 0]})),
                            BlockPredicateMatchingFluids(
                                offset=(0, 1, 0),
                                fluids='minecraft:water',
                                state={'source': 'true'},
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:not',
                ),
                then=FullBlockState(id='minecraft:grass_block', properties={'snowy': 'false'}),
            ),
        ],
        type='minecraft:rule_based',
    ),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 2})),
    half_height=2,
    target=BlockPredicateMatchingBlocks(blocks=['minecraft:dirt', 'minecraft:mud'], type='minecraft:matching_blocks'),
    type='minecraft:disk',
)

DISK_GRAVEL = ConfiguredFeatureDisk(
    state_provider=FullBlockState(id='minecraft:gravel'),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 2})),
    half_height=2,
    target=BlockPredicateMatchingBlocks(blocks=['minecraft:dirt', 'minecraft:grass_block'], type='minecraft:matching_blocks'),
    type='minecraft:disk',
)

DISK_SAND = ConfiguredFeatureDisk(
    state_provider=TypedBlockStateProviderRuleBased(
        fallback=FullBlockState(id='minecraft:sand'),
        rules=[
            RulesStruct(
                if_true=BlockPredicateMatchingBlocks(
                    offset=(0, -1, 0),
                    blocks='minecraft:air',
                    type='minecraft:matching_blocks',
                ),
                then=FullBlockState(id='minecraft:sandstone'),
            ),
        ],
        type='minecraft:rule_based',
    ),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 2})),
    half_height=2,
    target=BlockPredicateMatchingBlocks(blocks=['minecraft:dirt', 'minecraft:grass_block'], type='minecraft:matching_blocks'),
    type='minecraft:disk',
)

DRIPLEAF = ConfiguredFeatureSimpleRandomSelector(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=TypedBlockStateProviderWeighted(
                    entries=[
                        WeightedEntry(
                            weight=1,
                            data=FullBlockState(
                                id='minecraft:small_dripleaf',
                                properties={'facing': 'east', 'half': 'lower', 'waterlogged': 'false'},
                            ),
                        ),
                        WeightedEntry(
                            weight=1,
                            data=FullBlockState(
                                id='minecraft:small_dripleaf',
                                properties={'facing': 'west', 'half': 'lower', 'waterlogged': 'false'},
                            ),
                        ),
                        WeightedEntry(weight=1, data='minecraft:small_dripleaf'),
                        WeightedEntry(
                            weight=1,
                            data=FullBlockState(
                                id='minecraft:small_dripleaf',
                                properties={'facing': 'south', 'half': 'lower', 'waterlogged': 'false'},
                            ),
                        ),
                    ],
                    type='minecraft:weighted',
                ),
                type='minecraft:simple_block',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureBlockColumn(
                direction=Direction.UP,
                allowed_placement=BlockPredicateAnyOf(
                    predicates=[
                        BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                        BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    ],
                    type='minecraft:any_of',
                ),
                prioritize_tip=True,
                layers=[
                    BlockColumnLayer(
                        height=IntProvider(
                            type='minecraft:weighted_list',
                            **dict[str, Any]({
                                'distribution': [
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 4, 'min_inclusive': 0},
                                        'weight': 2,
                                    },
                                    {'data': 0, 'weight': 1},
                                ],
                            }),
                        ),
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf_stem',
                            properties={'facing': 'east', 'waterlogged': 'false'},
                        ),
                    ),
                    BlockColumnLayer(
                        height=1,
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf',
                            properties={'facing': 'east', 'tilt': 'none', 'waterlogged': 'false'},
                        ),
                    ),
                ],
                type='minecraft:block_column',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureBlockColumn(
                direction=Direction.UP,
                allowed_placement=BlockPredicateAnyOf(
                    predicates=[
                        BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                        BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    ],
                    type='minecraft:any_of',
                ),
                prioritize_tip=True,
                layers=[
                    BlockColumnLayer(
                        height=IntProvider(
                            type='minecraft:weighted_list',
                            **dict[str, Any]({
                                'distribution': [
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 4, 'min_inclusive': 0},
                                        'weight': 2,
                                    },
                                    {'data': 0, 'weight': 1},
                                ],
                            }),
                        ),
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf_stem',
                            properties={'facing': 'west', 'waterlogged': 'false'},
                        ),
                    ),
                    BlockColumnLayer(
                        height=1,
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf',
                            properties={'facing': 'west', 'tilt': 'none', 'waterlogged': 'false'},
                        ),
                    ),
                ],
                type='minecraft:block_column',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureBlockColumn(
                direction=Direction.UP,
                allowed_placement=BlockPredicateAnyOf(
                    predicates=[
                        BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                        BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    ],
                    type='minecraft:any_of',
                ),
                prioritize_tip=True,
                layers=[
                    BlockColumnLayer(
                        height=IntProvider(
                            type='minecraft:weighted_list',
                            **dict[str, Any]({
                                'distribution': [
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 4, 'min_inclusive': 0},
                                        'weight': 2,
                                    },
                                    {'data': 0, 'weight': 1},
                                ],
                            }),
                        ),
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf_stem',
                            properties={'facing': 'south', 'waterlogged': 'false'},
                        ),
                    ),
                    BlockColumnLayer(
                        height=1,
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf',
                            properties={'facing': 'south', 'tilt': 'none', 'waterlogged': 'false'},
                        ),
                    ),
                ],
                type='minecraft:block_column',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureBlockColumn(
                direction=Direction.UP,
                allowed_placement=BlockPredicateAnyOf(
                    predicates=[
                        BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                        BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                    ],
                    type='minecraft:any_of',
                ),
                prioritize_tip=True,
                layers=[
                    BlockColumnLayer(
                        height=IntProvider(
                            type='minecraft:weighted_list',
                            **dict[str, Any]({
                                'distribution': [
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 4, 'min_inclusive': 0},
                                        'weight': 2,
                                    },
                                    {'data': 0, 'weight': 1},
                                ],
                            }),
                        ),
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf_stem',
                            properties={'facing': 'north', 'waterlogged': 'false'},
                        ),
                    ),
                    BlockColumnLayer(
                        height=1,
                        provider=FullBlockState(
                            id='minecraft:big_dripleaf',
                            properties={'facing': 'north', 'tilt': 'none', 'waterlogged': 'false'},
                        ),
                    ),
                ],
                type='minecraft:block_column',
            ),
            placement=[],
        ),
    ],
    type='minecraft:simple_random_selector',
)

DRIPSTONE_CLUSTER = ConfiguredFeatureSpeleothemCluster(
    base_block='minecraft:dripstone_block',
    pointed_block='minecraft:pointed_dripstone',
    replaceable_blocks='#minecraft:dripstone_replaceable_blocks',
    floor_to_ceiling_search_range=12,
    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 3})),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 8, 'min_inclusive': 2})),
    max_stalagmite_stalactite_height_diff=1,
    height_deviation=3,
    speleothem_block_layer_thickness=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
    density=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.7, 'min_inclusive': 0.3})),
    wetness=FloatProvider(
        type='minecraft:clamped_normal',
        **dict[str, Any]({'deviation': 0.3, 'max': 0.9, 'mean': 0.1, 'min': 0.1}),
    ),
    chance_of_speleothem_at_max_distance_from_center=0.1,
    max_distance_from_edge_affecting_chance_of_speleothem=3,
    max_distance_from_center_affecting_height_bias=8,
    type='minecraft:speleothem_cluster',
)

DRY_GRASS = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=1, data='minecraft:short_dry_grass'),
            WeightedEntry(weight=1, data='minecraft:tall_dry_grass'),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

END_GATEWAY_DELAYED = ConfiguredFeatureEndGateway(exact=False, type='minecraft:end_gateway')

END_GATEWAY_RETURN = ConfiguredFeatureEndGateway(exact=True, exit=(100, 50, 0), type='minecraft:end_gateway')

END_ISLAND = ConfiguredFeatureEndIsland(type='minecraft:end_island')

END_PLATFORM = ConfiguredFeatureEndPlatform(type='minecraft:end_platform')

END_PODIUM_ACTIVE = ConfiguredFeatureEndPodium(active=True, type='minecraft:end_podium')

END_PODIUM_INACTIVE = ConfiguredFeatureEndPodium(type='minecraft:end_podium')

END_SPIKE = ConfiguredFeatureEndSpike(spikes=[], type='minecraft:end_spike')

FALLEN_BIRCH_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 8, 'min_inclusive': 5})),
    stump_decorators=[],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=2, data='minecraft:red_mushroom'),
                    WeightedEntry(weight=1, data='minecraft:brown_mushroom'),
                ],
                type='minecraft:weighted',
            ),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
    ],
    type='minecraft:fallen_tree',
)

FALLEN_JUNGLE_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:jungle_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 11, 'min_inclusive': 4})),
    stump_decorators=[TreeDecoratorTrunkVine(type='minecraft:trunk_vine')],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=2, data='minecraft:red_mushroom'),
                    WeightedEntry(weight=1, data='minecraft:brown_mushroom'),
                ],
                type='minecraft:weighted',
            ),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
    ],
    type='minecraft:fallen_tree',
)

FALLEN_OAK_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    stump_decorators=[TreeDecoratorTrunkVine(type='minecraft:trunk_vine')],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=2, data='minecraft:red_mushroom'),
                    WeightedEntry(weight=1, data='minecraft:brown_mushroom'),
                ],
                type='minecraft:weighted',
            ),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
    ],
    type='minecraft:fallen_tree',
)

FALLEN_POPLAR_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    stump_decorators=[],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=FullBlockState(id='minecraft:brown_mushroom'),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
        TreeDecoratorShelfMushroom(probability=0.8, type='minecraft:shelf_mushroom'),
    ],
    type='minecraft:fallen_tree',
)

FALLEN_SPRUCE_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:spruce_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 10, 'min_inclusive': 6})),
    stump_decorators=[],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=2, data='minecraft:red_mushroom'),
                    WeightedEntry(weight=1, data='minecraft:brown_mushroom'),
                ],
                type='minecraft:weighted',
            ),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
    ],
    type='minecraft:fallen_tree',
)

FALLEN_SUPER_BIRCH_TREE = ConfiguredFeatureFallenTree(
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    log_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 15, 'min_inclusive': 5})),
    stump_decorators=[],
    log_decorators=[
        TreeDecoratorAttachedToLogs(
            probability=0.1,
            block_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=2, data='minecraft:red_mushroom'),
                    WeightedEntry(weight=1, data='minecraft:brown_mushroom'),
                ],
                type='minecraft:weighted',
            ),
            directions=[Direction.UP],
            type='minecraft:attached_to_logs',
        ),
    ],
    type='minecraft:fallen_tree',
)

FANCY_OAK = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[],
    type='minecraft:tree',
)

FANCY_OAK_BEES = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[TreeDecoratorBeehive(probability=1.0, type='minecraft:beehive')],
    type='minecraft:tree',
)

FANCY_OAK_BEES_0002_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[
        TreeDecoratorBeehive(probability=0.002, type='minecraft:beehive'),
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

FANCY_OAK_BEES_002 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[TreeDecoratorBeehive(probability=0.02, type='minecraft:beehive')],
    type='minecraft:tree',
)

FANCY_OAK_BEES_005 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[TreeDecoratorBeehive(probability=0.05, type='minecraft:beehive')],
    type='minecraft:tree',
)

FANCY_OAK_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(
        min_clipped_height=4.0,
        limit=0,
        upper_size=0,
        type='minecraft:two_layers_feature_size',
    ),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerFancyTrunkPlacer(type='minecraft:fancy_trunk_placer', base_height=3, height_rand_a=11, height_rand_b=0),
    foliage_placer=FoliagePlacerFancyFoliagePlacer(height=4, type='minecraft:fancy_foliage_placer', radius=2, offset=4),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

FIREFLY_BUSH = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:firefly_bush'), type='minecraft:simple_block')

FLOWER_CHERRY = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=1, data='minecraft:pink_petals'),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'east', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'south', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'west', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'north', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'east', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'south', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'west', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'north', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'east', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'south', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'west', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'north', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'east', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'south', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:pink_petals', properties={'facing': 'west', 'flower_amount': '4'}),
            ),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

FLOWER_DEFAULT = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[WeightedEntry(weight=2, data='minecraft:poppy'), WeightedEntry(weight=1, data='minecraft:dandelion')],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

FLOWER_FLOWER_FOREST = ConfiguredFeatureSimpleBlock(to_place='minecraft:flower_flower_forest', type='minecraft:simple_block')

FLOWER_MEADOW = ConfiguredFeatureSimpleBlock(to_place='minecraft:flower_meadow', type='minecraft:simple_block')

FLOWER_PALE_GARDEN = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:closed_eyeblossom'),
    schedule_tick=True,
    type='minecraft:simple_block',
)

FLOWER_PLAIN = ConfiguredFeatureSimpleBlock(to_place='minecraft:flower_plain', type='minecraft:simple_block')

FLOWER_SWAMP = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:blue_orchid'), type='minecraft:simple_block')

FOREST_FLOWERS = ConfiguredFeatureSimpleRandomSelector(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:lilac', properties={'half': 'lower'}),
                type='minecraft:simple_block',
            ),
            placement=[
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
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:rose_bush', properties={'half': 'lower'}),
                type='minecraft:simple_block',
            ),
            placement=[
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
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:peony', properties={'half': 'lower'}),
                type='minecraft:simple_block',
            ),
            placement=[
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
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:lily_of_the_valley'),
                type='minecraft:simple_block',
            ),
            placement=[
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
        ),
    ],
    type='minecraft:simple_random_selector',
)

FOREST_ROCK = ConfiguredFeatureBlockBlob(
    state='minecraft:mossy_cobblestone',
    can_place_on=BlockPredicateMatchingBlockTag(tag='minecraft:forest_rock_can_place_on', type='minecraft:matching_block_tag'),
    type='minecraft:block_blob',
)

FOSSIL_COAL = ConfiguredFeatureFossil(
    max_empty_corners_allowed=4,
    fossil_structures=[
        'minecraft:fossil/spine_1',
        'minecraft:fossil/spine_2',
        'minecraft:fossil/spine_3',
        'minecraft:fossil/spine_4',
        'minecraft:fossil/skull_1',
        'minecraft:fossil/skull_2',
        'minecraft:fossil/skull_3',
        'minecraft:fossil/skull_4',
    ],
    overlay_structures=[
        'minecraft:fossil/spine_1_coal',
        'minecraft:fossil/spine_2_coal',
        'minecraft:fossil/spine_3_coal',
        'minecraft:fossil/spine_4_coal',
        'minecraft:fossil/skull_1_coal',
        'minecraft:fossil/skull_2_coal',
        'minecraft:fossil/skull_3_coal',
        'minecraft:fossil/skull_4_coal',
    ],
    fossil_processors='minecraft:fossil_rot',
    overlay_processors='minecraft:fossil_coal',
    type='minecraft:fossil',
)

FOSSIL_DIAMONDS = ConfiguredFeatureFossil(
    max_empty_corners_allowed=4,
    fossil_structures=[
        'minecraft:fossil/spine_1',
        'minecraft:fossil/spine_2',
        'minecraft:fossil/spine_3',
        'minecraft:fossil/spine_4',
        'minecraft:fossil/skull_1',
        'minecraft:fossil/skull_2',
        'minecraft:fossil/skull_3',
        'minecraft:fossil/skull_4',
    ],
    overlay_structures=[
        'minecraft:fossil/spine_1_coal',
        'minecraft:fossil/spine_2_coal',
        'minecraft:fossil/spine_3_coal',
        'minecraft:fossil/spine_4_coal',
        'minecraft:fossil/skull_1_coal',
        'minecraft:fossil/skull_2_coal',
        'minecraft:fossil/skull_3_coal',
        'minecraft:fossil/skull_4_coal',
    ],
    fossil_processors='minecraft:fossil_rot',
    overlay_processors='minecraft:fossil_diamonds',
    type='minecraft:fossil',
)

FREEZE_TOP_LAYER = ConfiguredFeatureFreezeTopLayer(type='minecraft:freeze_top_layer')

GLOWSTONE_EXTRA = ConfiguredFeatureRandomNeighborSpread(
    block=FullBlockState(id='minecraft:glowstone'),
    accepted_neighbors='minecraft:glowstone',
    can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    attempts=1500,
    xz_offset=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
    y_offset=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 0, 'min_inclusive': -11})),
    type='minecraft:random_neighbor_spread',
)

GLOW_LICHEN = ConfiguredFeatureMultifaceGrowth(
    block=MultifaceBlock.GLOWLICHEN,
    search_range=20,
    can_place_on_ceiling=True,
    can_place_on_wall=True,
    can_be_placed_on=[
        'minecraft:stone',
        'minecraft:andesite',
        'minecraft:diorite',
        'minecraft:granite',
        'minecraft:dripstone_block',
        'minecraft:calcite',
        'minecraft:tuff',
        'minecraft:deepslate',
        'minecraft:sulfur',
        'minecraft:cinnabar',
    ],
    type='minecraft:multiface_growth',
)

GRASS = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:short_grass'), type='minecraft:simple_block')

GRASS_JUNGLE = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[WeightedEntry(weight=3, data='minecraft:short_grass'), WeightedEntry(weight=1, data='minecraft:fern')],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

HUGE_BROWN_MUSHROOM = ConfiguredFeatureHugeBrownMushroom(
    cap_provider=FullBlockState(
        id='minecraft:brown_mushroom_block',
        properties={'down': 'false', 'east': 'true', 'north': 'true', 'south': 'true', 'up': 'true', 'west': 'true'},
    ),
    stem_provider=FullBlockState(
        id='minecraft:mushroom_stem',
        properties={'down': 'false', 'east': 'true', 'north': 'true', 'south': 'true', 'up': 'false', 'west': 'true'},
    ),
    foliage_radius=3,
    can_place_on=BlockPredicateMatchingBlockTag(
        tag='minecraft:huge_brown_mushroom_can_place_on',
        type='minecraft:matching_block_tag',
    ),
    type='minecraft:huge_brown_mushroom',
)

HUGE_RED_MUSHROOM = ConfiguredFeatureHugeRedMushroom(
    cap_provider=FullBlockState(
        id='minecraft:red_mushroom_block',
        properties={'down': 'false', 'east': 'true', 'north': 'true', 'south': 'true', 'up': 'true', 'west': 'true'},
    ),
    stem_provider=FullBlockState(
        id='minecraft:mushroom_stem',
        properties={'down': 'false', 'east': 'true', 'north': 'true', 'south': 'true', 'up': 'false', 'west': 'true'},
    ),
    can_place_on=BlockPredicateMatchingBlockTag(tag='minecraft:huge_red_mushroom_can_place_on', type='minecraft:matching_block_tag'),
    type='minecraft:huge_red_mushroom',
)

ICEBERG_BLUE = ConfiguredFeatureIceberg(state='minecraft:blue_ice', type='minecraft:iceberg')

ICEBERG_PACKED = ConfiguredFeatureIceberg(state='minecraft:packed_ice', type='minecraft:iceberg')

ICE_CAVE_ORE_ANDESITE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
                    RuleTestTagMatch(tag='minecraft:ice_cave_ore_replaceables', predicate_type='minecraft:tag_match'),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:andesite',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ICE_CAVE_ORE_COAL = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:coal_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_coal_ore',
                    ),
                ],
                size=17,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_COAL_BURIED = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:coal_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_coal_ore',
                    ),
                ],
                size=17,
                discard_chance_on_air_exposure=0.5,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_COPPER_SMALL = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:copper_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_copper_ore',
                    ),
                ],
                size=10,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_DIAMOND_BURIED = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:diamond_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_diamond_ore',
                    ),
                ],
                size=8,
                discard_chance_on_air_exposure=1.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_DIAMOND_LARGE = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:diamond_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_diamond_ore',
                    ),
                ],
                size=12,
                discard_chance_on_air_exposure=0.7,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_DIAMOND_MEDIUM = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:diamond_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_diamond_ore',
                    ),
                ],
                size=8,
                discard_chance_on_air_exposure=0.5,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_DIAMOND_SMALL = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:diamond_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_diamond_ore',
                    ),
                ],
                size=4,
                discard_chance_on_air_exposure=0.5,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_DIORITE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
                    RuleTestTagMatch(tag='minecraft:ice_cave_ore_replaceables', predicate_type='minecraft:tag_match'),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:diorite',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ICE_CAVE_ORE_GOLD_BURIED = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:gold_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_gold_ore',
                    ),
                ],
                size=9,
                discard_chance_on_air_exposure=0.5,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_GRAVEL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
                    RuleTestTagMatch(tag='minecraft:ice_cave_ore_replaceables', predicate_type='minecraft:tag_match'),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:gravel',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ICE_CAVE_ORE_IRON = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:iron_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_iron_ore',
                    ),
                ],
                size=9,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_IRON_SMALL = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:iron_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_iron_ore',
                    ),
                ],
                size=4,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_LAPIS = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:lapis_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_lapis_ore',
                    ),
                ],
                size=7,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_LAPIS_BURIED = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:lapis_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_lapis_ore',
                    ),
                ],
                size=7,
                discard_chance_on_air_exposure=1.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_ORE_REDSTONE = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=0,
                                                    max_inclusive=2031,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:stone_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:stone',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAnyOf(
                                    rules=[
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestTagMatch(
                                                    tag='minecraft:height_specific_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                                RuleTestHeightMatch(
                                                    min_inclusive=-2032,
                                                    max_inclusive=8,
                                                    predicate_type='minecraft:height_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                        RuleTestAllOf(
                                            rules=[
                                                RuleTestNot(
                                                    rule=RuleTestTagMatch(
                                                        tag='minecraft:height_specific_ore_replaceables',
                                                        predicate_type='minecraft:tag_match',
                                                    ),
                                                    predicate_type='minecraft:not',
                                                ),
                                                RuleTestTagMatch(
                                                    tag='minecraft:deepslate_ore_replaceables',
                                                    predicate_type='minecraft:tag_match',
                                                ),
                                            ],
                                            predicate_type='minecraft:all_of',
                                        ),
                                    ],
                                    predicate_type='minecraft:any_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:ice_cave_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate',
                    ),
                ],
                size=20,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOre(
                targets=[
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=0,
                                            max_inclusive=2031,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:stone_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:redstone_ore',
                    ),
                    TargetBlock(
                        target=RuleTestAnyOf(
                            rules=[
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestTagMatch(
                                            tag='minecraft:height_specific_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                        RuleTestHeightMatch(
                                            min_inclusive=-2032,
                                            max_inclusive=8,
                                            predicate_type='minecraft:height_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                                RuleTestAllOf(
                                    rules=[
                                        RuleTestNot(
                                            rule=RuleTestTagMatch(
                                                tag='minecraft:height_specific_ore_replaceables',
                                                predicate_type='minecraft:tag_match',
                                            ),
                                            predicate_type='minecraft:not',
                                        ),
                                        RuleTestTagMatch(
                                            tag='minecraft:deepslate_ore_replaceables',
                                            predicate_type='minecraft:tag_match',
                                        ),
                                    ],
                                    predicate_type='minecraft:all_of',
                                ),
                            ],
                            predicate_type='minecraft:any_of',
                        ),
                        state='minecraft:deepslate_redstone_ore',
                    ),
                ],
                size=8,
                discard_chance_on_air_exposure=0.0,
                type='minecraft:ore',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

ICE_CREVASSE = ConfiguredFeatureCrevasse(
    max_width=4,
    max_length=16,
    min_footprint=10,
    cursor_surface_search_range=8,
    column_surface_search_range=8,
    twistiness=4.0,
    tapering=0.6,
    turn_factor=0.05,
    carve_depth=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 10, 'min_inclusive': 6})),
    fill_depth=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
    surface_block=FullBlockState(id='minecraft:brittle_ice', properties={'age': '0'}),
    fill_block=FullBlockState(id='minecraft:water', properties={'level': '0'}),
    carvable_blocks=BlockPredicateMatchingBlockTag(tag='minecraft:ice_crevasse_replaceables', type='minecraft:matching_block_tag'),
    acceptable_barrier=BlockPredicateMatchingBlockTag(tag='minecraft:blocks_fluid_flow', type='minecraft:matching_block_tag'),
    type='minecraft:crevasse',
)

ICE_CRYSTAL = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:ice_crystal', properties={'facing': 'up', 'waterlogged': 'false'}),
    type='minecraft:simple_block',
)

ICE_PATCH = ConfiguredFeatureDisk(
    state_provider=FullBlockState(id='minecraft:packed_ice'),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
    half_height=1,
    target=BlockPredicateMatchingBlocks(
        blocks=[
            'minecraft:dirt',
            'minecraft:grass_block',
            'minecraft:podzol',
            'minecraft:coarse_dirt',
            'minecraft:mycelium',
            'minecraft:snow_block',
            'minecraft:ice',
        ],
        type='minecraft:matching_blocks',
    ),
    type='minecraft:disk',
)

ICE_SPIKE = ConfiguredFeatureSpike(
    state='minecraft:packed_ice',
    can_place_on=BlockPredicateMatchingBlocks(blocks='minecraft:snow_block', type='minecraft:matching_blocks'),
    can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:ice_spike_replaceable', type='minecraft:matching_block_tag'),
    type='minecraft:spike',
)

ICICLE_CLUSTER = ConfiguredFeatureSpeleothemCluster(
    base_block='minecraft:packed_ice',
    pointed_block='minecraft:icicle',
    replaceable_blocks=[],
    floor_to_ceiling_search_range=32,
    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 5, 'min_inclusive': 3})),
    radius=6,
    max_stalagmite_stalactite_height_diff=1,
    height_deviation=3,
    speleothem_block_layer_thickness=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
    density=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.7, 'min_inclusive': 0.3})),
    wetness=0.0,
    chance_of_speleothem_at_max_distance_from_center=0.1,
    max_distance_from_edge_affecting_chance_of_speleothem=3,
    max_distance_from_center_affecting_height_bias=8,
    placement_options=PlacementOptionsStruct(
        placement_mode=SpeleothemClusterPlacementMode.CEILING,
        base_block_transformer=SpeleothemBaseBlockTransformer.SETATTACHED,
        allow_water_placement=False,
    ),
    type='minecraft:speleothem_cluster',
)

JUNGLE_BUSH = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(limit=0, upper_size=0, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:jungle_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=1,
        height_rand_a=0,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBushFoliagePlacer(height=2, type='minecraft:bush_foliage_placer', radius=2, offset=1),
    decorators=[],
    type='minecraft:tree',
)

JUNGLE_TREE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:jungle_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:jungle_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=8,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorCocoa(probability=0.2, type='minecraft:cocoa'),
        TreeDecoratorTrunkVine(type='minecraft:trunk_vine'),
        TreeDecoratorLeaveVine(probability=0.25, type='minecraft:leave_vine'),
    ],
    type='minecraft:tree',
)

JUNGLE_TREE_NO_VINE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:jungle_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:jungle_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=8,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[],
    type='minecraft:tree',
)

KELP = ConfiguredFeatureBlockColumn(
    direction=Direction.UP,
    allowed_placement=BlockPredicateAllOf(
        predicates=[
            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
            BlockPredicateMatchingBlocks(offset=(0, 1, 0), blocks='minecraft:water', type='minecraft:matching_blocks'),
        ],
        type='minecraft:all_of',
    ),
    prioritize_tip=True,
    layers=[
        BlockColumnLayer(
            height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 9, 'min_inclusive': 0})),
            provider=FullBlockState(id='minecraft:kelp_plant'),
        ),
        BlockColumnLayer(
            height=1,
            provider=TypedBlockStateProviderRandomizedInt(
                property='age',
                values=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 23, 'min_inclusive': 20})),
                source=FullBlockState(id='minecraft:kelp', properties={'age': '0'}),
                type='minecraft:randomized_int',
            ),
        ),
    ],
    type='minecraft:block_column',
)

LAKE_LAVA = ConfiguredFeatureLake(
    fluid=FullBlockState(id='minecraft:lava', properties={'level': '0'}),
    barrier=FullBlockState(id='minecraft:stone'),
    can_place_feature=BlockPredicateTrue(type='minecraft:true'),
    can_replace_with_air_or_fluid=BlockPredicateNot(
        predicate=BlockPredicateMatchingBlockTag(tag='minecraft:features_cannot_replace', type='minecraft:matching_block_tag'),
        type='minecraft:not',
    ),
    can_replace_with_barrier=BlockPredicateNot(
        predicate=BlockPredicateMatchingBlockTag(
            tag='minecraft:lava_pool_stone_cannot_replace',
            type='minecraft:matching_block_tag',
        ),
        type='minecraft:not',
    ),
    type='minecraft:lake',
)

LARGE_BASALT_COLUMNS = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=9,
            data=PlacedFeature(
                feature=ConfiguredFeatureSteppedColumnCluster(
                    block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                    can_replace=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:lava',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateHeightRange(
                                        min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                                        max_inclusive=VerticalAnchorStruct4(relative_to_sea_level=0),
                                        type='minecraft:height_range',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    continue_through=BlockPredicateMatchingBlocks(blocks='minecraft:basalt', type='minecraft:matching_blocks'),
                    cannot_place_on='#minecraft:cannot_place_basalt_pillar_on',
                    column_reach=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
                    column_count=50,
                    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 10, 'min_inclusive': 5})),
                    cluster_reach=5,
                    type='minecraft:stepped_column_cluster',
                ),
                placement=[],
            ),
        ),
        WeightedEntry(
            weight=1,
            data=PlacedFeature(
                feature=ConfiguredFeatureSteppedColumnCluster(
                    block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                    can_replace=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:lava',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateHeightRange(
                                        min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                                        max_inclusive=VerticalAnchorStruct4(relative_to_sea_level=0),
                                        type='minecraft:height_range',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    continue_through=BlockPredicateMatchingBlocks(blocks='minecraft:basalt', type='minecraft:matching_blocks'),
                    cannot_place_on='#minecraft:cannot_place_basalt_pillar_on',
                    column_reach=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
                    column_count=15,
                    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 10, 'min_inclusive': 5})),
                    cluster_reach=8,
                    type='minecraft:stepped_column_cluster',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

LARGE_DRIPSTONE = ConfiguredFeatureLargeSpeleothem(
    base_block='minecraft:dripstone_block',
    replaceable_blocks='#minecraft:dripstone_replaceable_blocks',
    column_radius=IntProvider(
        type='minecraft:clamped',
        **dict[str, Any]({
            'max_inclusive': 16,
            'min_inclusive': 3,
            'source': {'type': 'minecraft:uniform', 'max_inclusive': 19, 'min_inclusive': 3},
        }),
    ),
    height_scale=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 2.0, 'min_inclusive': 0.4})),
    max_column_radius_to_cave_height_ratio=0.33,
    stalactite_bluntness=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.9, 'min_inclusive': 0.3})),
    stalagmite_bluntness=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.0, 'min_inclusive': 0.4})),
    wind_speed=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.3, 'min_inclusive': 0.0})),
    min_radius_for_wind=4,
    min_bluntness_for_wind=0.6,
    type='minecraft:large_speleothem',
)

LARGE_FERN = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:large_fern', properties={'half': 'lower'}),
    type='minecraft:simple_block',
)

LARGE_ICICLE = ConfiguredFeatureLargeSpeleothem(
    base_block='minecraft:packed_ice',
    replaceable_blocks='#minecraft:large_icicle_replaceable',
    column_radius=IntProvider(
        type='minecraft:clamped',
        **dict[str, Any]({
            'max_inclusive': 16,
            'min_inclusive': 3,
            'source': {'type': 'minecraft:uniform', 'max_inclusive': 19, 'min_inclusive': 3},
        }),
    ),
    height_scale=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 2.0, 'min_inclusive': 0.4})),
    max_column_radius_to_cave_height_ratio=0.33,
    stalactite_bluntness=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.9, 'min_inclusive': 0.3})),
    stalagmite_bluntness=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 1.0, 'min_inclusive': 0.4})),
    wind_speed=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.3, 'min_inclusive': 0.0})),
    min_radius_for_wind=4,
    min_bluntness_for_wind=0.6,
    type='minecraft:large_speleothem',
)

LEAF_LITTER = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=1, data='minecraft:leaf_litter'),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'south', 'segment_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'north', 'segment_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'south', 'segment_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'north', 'segment_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'south', 'segment_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
            ),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

LUSH_CAVES_CLAY = ConfiguredFeatureRandomBooleanSelector(
    feature_false=PlacedFeature(feature='minecraft:clay_pool_with_dripleaves', placement=[]),
    feature_true=PlacedFeature(feature='minecraft:clay_with_dripleaves', placement=[]),
    type='minecraft:random_boolean_selector',
)

MANGROVE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(limit=2, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:mangrove_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:mangrove_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    root_placer=RootPlacerMangroveRootPlacer(
        mangrove_root_placement=MangroveRootPlacement(
            max_root_width=8,
            max_root_length=15,
            random_skew_chance=0.2,
            can_grow_through='#minecraft:mangrove_roots_can_grow_through',
            muddy_roots_in=['minecraft:mud', 'minecraft:muddy_mangrove_roots'],
            muddy_roots_provider=FullBlockState(id='minecraft:muddy_mangrove_roots', properties={'axis': 'y'}),
        ),
        type='minecraft:mangrove_root_placer',
        root_provider=FullBlockState(id='minecraft:mangrove_roots', properties={'waterlogged': 'false'}),
        trunk_offset_y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 1})),
        above_root_placement=AboveRootPlacement(
            above_root_provider=FullBlockState(id='minecraft:moss_carpet'),
            above_root_placement_chance=0.5,
        ),
    ),
    trunk_placer=TrunkPlacerUpwardsBranchingTrunkPlacer(
        extra_branch_steps=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        extra_branch_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 1, 'min_inclusive': 0})),
        place_branch_per_log_probability=0.5,
        can_grow_through='#minecraft:mangrove_logs_can_grow_through',
        type='minecraft:upwards_branching_trunk_placer',
        base_height=2,
        height_rand_a=1,
        height_rand_b=4,
    ),
    foliage_placer=FoliagePlacerRandomSpreadFoliagePlacer(
        foliage_height=2,
        leaf_placement_attempts=70,
        type='minecraft:random_spread_foliage_placer',
        radius=3,
        offset=0,
    ),
    decorators=[
        TreeDecoratorLeaveVine(probability=0.125, type='minecraft:leave_vine'),
        TreeDecoratorAttachedToLeaves(
            probability=0.14,
            exclusion_radius_xz=1,
            exclusion_radius_y=0,
            required_empty_blocks=2,
            block_provider='minecraft:mangrove_propagule',
            directions=[Direction.DOWN],
            type='minecraft:attached_to_leaves',
        ),
        TreeDecoratorBeehive(probability=0.01, type='minecraft:beehive'),
    ],
    type='minecraft:tree',
)

MANGROVE_VEGETATION = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.85, feature='minecraft:tall_mangrove_checked')],
    default='minecraft:mangrove_checked',
    type='minecraft:random_selector',
)

MEADOW_TREES = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.5, feature='minecraft:fancy_oak_bees')],
    default='minecraft:super_birch_bees',
    type='minecraft:random_selector',
)

MEGA_JUNGLE_TREE = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(lower_size=1, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:jungle_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:jungle_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerMegaJungleTrunkPlacer(
        type='minecraft:mega_jungle_trunk_placer',
        base_height=10,
        height_rand_a=2,
        height_rand_b=19,
    ),
    foliage_placer=FoliagePlacerJungleFoliagePlacer(height=2, type='minecraft:jungle_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorTrunkVine(type='minecraft:trunk_vine'),
        TreeDecoratorLeaveVine(probability=0.25, type='minecraft:leave_vine'),
    ],
    type='minecraft:tree',
)

MEGA_PINE = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(lower_size=1, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:spruce_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:spruce_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerGiantTrunkPlacer(type='minecraft:giant_trunk_placer', base_height=13, height_rand_a=2, height_rand_b=14),
    foliage_placer=FoliagePlacerMegaPineFoliagePlacer(
        crown_height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 3})),
        type='minecraft:mega_pine_foliage_placer',
        radius=0,
        offset=0,
    ),
    decorators=[TreeDecoratorAlterGround(provider='minecraft:podzol_beneath_tree', type='minecraft:alter_ground')],
    type='minecraft:tree',
)

MEGA_SPRUCE = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(lower_size=1, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:spruce_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:spruce_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerGiantTrunkPlacer(type='minecraft:giant_trunk_placer', base_height=13, height_rand_a=2, height_rand_b=14),
    foliage_placer=FoliagePlacerMegaPineFoliagePlacer(
        crown_height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 17, 'min_inclusive': 13})),
        type='minecraft:mega_pine_foliage_placer',
        radius=0,
        offset=0,
    ),
    decorators=[TreeDecoratorAlterGround(provider='minecraft:podzol_beneath_tree', type='minecraft:alter_ground')],
    type='minecraft:tree',
)

MELON = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:melon'), type='minecraft:simple_block')

MONSTER_ROOM = ConfiguredFeatureMonsterRoom(type='minecraft:monster_room')

MOSS_PATCH = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=1,
    vertical_range=5,
    extra_bottom_block_chance=0.0,
    extra_edge_column_chance=0.3,
    vegetation_chance=0.8,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    replaceable='#minecraft:moss_replaceable',
    ground_state=FullBlockState(id='minecraft:moss_block'),
    vegetation_feature=PlacedFeature(feature='minecraft:moss_vegetation', placement=[]),
    type='minecraft:vegetation_patch',
)

MOSS_PATCH_BONEMEAL = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=1,
    vertical_range=5,
    extra_bottom_block_chance=0.0,
    extra_edge_column_chance=0.75,
    vegetation_chance=0.6,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
    replaceable='#minecraft:moss_replaceable',
    ground_state=FullBlockState(id='minecraft:moss_block'),
    vegetation_feature=PlacedFeature(feature='minecraft:moss_vegetation', placement=[]),
    type='minecraft:vegetation_patch',
)

MOSS_PATCH_CEILING = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.CEILING,
    depth=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
    vertical_range=5,
    extra_bottom_block_chance=0.0,
    extra_edge_column_chance=0.3,
    vegetation_chance=0.08,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 4})),
    replaceable='#minecraft:moss_replaceable',
    ground_state=FullBlockState(id='minecraft:moss_block'),
    vegetation_feature=PlacedFeature(feature='minecraft:cave_vine_in_moss', placement=[]),
    type='minecraft:vegetation_patch',
)

MOSS_VEGETATION = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=4, data='minecraft:flowering_azalea'),
            WeightedEntry(weight=7, data='minecraft:azalea'),
            WeightedEntry(weight=25, data='minecraft:moss_carpet'),
            WeightedEntry(weight=50, data='minecraft:short_grass'),
            WeightedEntry(weight=10, data='minecraft:tall_grass'),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

MUSHROOM_ISLAND_VEGETATION = ConfiguredFeatureRandomBooleanSelector(
    feature_false=PlacedFeature(feature='minecraft:huge_brown_mushroom', placement=[]),
    feature_true=PlacedFeature(feature='minecraft:huge_red_mushroom', placement=[]),
    type='minecraft:random_boolean_selector',
)

NETHER_SPROUTS = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:nether_sprouts'), type='minecraft:simple_block')

NYLIUM_BONEMEAL = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureOverlay(
                features=PlacedFeature(
                    feature=ConfiguredFeatureSimpleBlock(
                        to_place=TypedBlockStateProviderWeighted(
                            entries=[
                                WeightedEntry(weight=87, data='minecraft:crimson_roots'),
                                WeightedEntry(weight=11, data='minecraft:crimson_fungus'),
                                WeightedEntry(weight=1, data='minecraft:warped_fungus'),
                            ],
                            type='minecraft:weighted',
                        ),
                        type='minecraft:simple_block',
                    ),
                    placement=[
                        PlacementModifierCount(count=9, type='minecraft:count'),
                        PlacementModifierOffset(
                            x=IntProvider(
                                type='minecraft:trapezoid',
                                **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                            ),
                            y=IntProvider(
                                type='minecraft:trapezoid',
                                **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0}),
                            ),
                            z=IntProvider(
                                type='minecraft:trapezoid',
                                **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                            ),
                            type='minecraft:offset',
                        ),
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:overlay',
            ),
            placement=[
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:crimson_nylium',
                        type='minecraft:matching_blocks',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOverlay(
                features=[
                    PlacedFeature(
                        feature=ConfiguredFeatureSimpleBlock(
                            to_place=TypedBlockStateProviderWeighted(
                                entries=[
                                    WeightedEntry(weight=85, data='minecraft:warped_roots'),
                                    WeightedEntry(weight=1, data='minecraft:crimson_roots'),
                                    WeightedEntry(weight=13, data='minecraft:warped_fungus'),
                                    WeightedEntry(weight=1, data='minecraft:crimson_fungus'),
                                ],
                                type='minecraft:weighted',
                            ),
                            type='minecraft:simple_block',
                        ),
                        placement=[
                            PlacementModifierCount(count=9, type='minecraft:count'),
                            PlacementModifierOffset(
                                x=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                                ),
                                y=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0}),
                                ),
                                z=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                                ),
                                type='minecraft:offset',
                            ),
                            PlacementModifierBlockPredicateFilter(
                                predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                                type='minecraft:block_predicate_filter',
                            ),
                        ],
                    ),
                    PlacedFeature(
                        feature=ConfiguredFeatureSimpleBlock(
                            to_place=FullBlockState(id='minecraft:nether_sprouts'),
                            type='minecraft:simple_block',
                        ),
                        placement=[
                            PlacementModifierCount(count=9, type='minecraft:count'),
                            PlacementModifierOffset(
                                x=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                                ),
                                y=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 0, 'min': 0, 'plateau': 0}),
                                ),
                                z=IntProvider(
                                    type='minecraft:trapezoid',
                                    **dict[str, Any]({'max': 2, 'min': -2, 'plateau': 0}),
                                ),
                                type='minecraft:offset',
                            ),
                            PlacementModifierBlockPredicateFilter(
                                predicate=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                                type='minecraft:block_predicate_filter',
                            ),
                        ],
                    ),
                    PlacedFeature(
                        feature=ConfiguredFeatureWeightedRandomSelector(
                            features=[
                                WeightedEntry(
                                    weight=1,
                                    data=PlacedFeature(
                                        feature=ConfiguredFeatureBlockColumn(
                                            direction=Direction.UP,
                                            allowed_placement=BlockPredicateMatchingBlockTag(
                                                tag='minecraft:air',
                                                type='minecraft:matching_block_tag',
                                            ),
                                            prioritize_tip=True,
                                            layers=[
                                                BlockColumnLayer(
                                                    height=IntProvider(
                                                        type='minecraft:weighted_list',
                                                        **dict[str, Any]({
                                                            'distribution': [
                                                                {
                                                                    'data': {
                                                                        'type': 'minecraft:uniform',
                                                                        'max_inclusive': 1,
                                                                        'min_inclusive': 0,
                                                                    },
                                                                    'weight': 10,
                                                                },
                                                                {
                                                                    'data': {
                                                                        'type': 'minecraft:uniform',
                                                                        'max_inclusive': 3,
                                                                        'min_inclusive': 1,
                                                                    },
                                                                    'weight': 2,
                                                                },
                                                                {'data': 0, 'weight': 3},
                                                            ],
                                                        }),
                                                    ),
                                                    provider=FullBlockState(id='minecraft:twisting_vines_plant'),
                                                ),
                                                BlockColumnLayer(
                                                    height=1,
                                                    provider=TypedBlockStateProviderRandomizedInt(
                                                        property='age',
                                                        values=IntProvider(
                                                            type='minecraft:uniform',
                                                            **dict[str, Any]({'max_inclusive': 25, 'min_inclusive': 17}),
                                                        ),
                                                        source=FullBlockState(
                                                            id='minecraft:twisting_vines',
                                                            properties={'age': '0'},
                                                        ),
                                                        type='minecraft:randomized_int',
                                                    ),
                                                ),
                                            ],
                                            type='minecraft:block_column',
                                        ),
                                        placement=[
                                            PlacementModifierBlockPredicateFilter(
                                                predicate=BlockPredicateAllOf(
                                                    predicates=[
                                                        BlockPredicateMatchingBlockTag(
                                                            tag='minecraft:air',
                                                            type='minecraft:matching_block_tag',
                                                        ),
                                                        BlockPredicateMatchingBlocks(
                                                            offset=(0, -1, 0),
                                                            blocks=[
                                                                'minecraft:netherrack',
                                                                'minecraft:warped_nylium',
                                                                'minecraft:warped_wart_block',
                                                            ],
                                                            type='minecraft:matching_blocks',
                                                        ),
                                                    ],
                                                    type='minecraft:all_of',
                                                ),
                                                type='minecraft:block_predicate_filter',
                                            ),
                                            PlacementModifierCount(count=9, type='minecraft:count'),
                                            PlacementModifierOffset(
                                                x=IntProvider(
                                                    type='minecraft:uniform',
                                                    **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': -3}),
                                                ),
                                                y=IntProvider(
                                                    type='minecraft:uniform',
                                                    **dict[str, Any]({'max_inclusive': 1, 'min_inclusive': -1}),
                                                ),
                                                z=IntProvider(
                                                    type='minecraft:uniform',
                                                    **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': -3}),
                                                ),
                                                type='minecraft:offset',
                                            ),
                                            PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
                                            PlacementModifierEnvironmentScan(
                                                direction_of_search=VerticalDirection.DOWN,
                                                max_steps=32,
                                                target_condition=BlockPredicateNot(
                                                    predicate=BlockPredicateMatchingBlockTag(
                                                        tag='minecraft:air',
                                                        type='minecraft:matching_block_tag',
                                                    ),
                                                    type='minecraft:not',
                                                ),
                                                type='minecraft:environment_scan',
                                            ),
                                            PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
                                            PlacementModifierBlockPredicateFilter(
                                                predicate=BlockPredicateAllOf(
                                                    predicates=[
                                                        BlockPredicateMatchingBlockTag(
                                                            tag='minecraft:air',
                                                            type='minecraft:matching_block_tag',
                                                        ),
                                                        BlockPredicateMatchingBlocks(
                                                            offset=(0, -1, 0),
                                                            blocks=[
                                                                'minecraft:netherrack',
                                                                'minecraft:warped_nylium',
                                                                'minecraft:warped_wart_block',
                                                            ],
                                                            type='minecraft:matching_blocks',
                                                        ),
                                                    ],
                                                    type='minecraft:all_of',
                                                ),
                                                type='minecraft:block_predicate_filter',
                                            ),
                                        ],
                                    ),
                                ),
                                WeightedEntry(
                                    weight=7,
                                    data=PlacedFeature(feature=ConfiguredFeatureNoOp(type='minecraft:no_op'), placement=[]),
                                ),
                            ],
                            type='minecraft:weighted_random_selector',
                        ),
                        placement=[],
                    ),
                ],
                type='minecraft:overlay',
            ),
            placement=[
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateMatchingBlocks(
                        offset=(0, -1, 0),
                        blocks='minecraft:warped_nylium',
                        type='minecraft:matching_blocks',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
    ],
    type='minecraft:overlay',
)

OAK = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[],
    type='minecraft:tree',
)

OAK_BEES_0002_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorBeehive(probability=0.002, type='minecraft:beehive'),
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

OAK_BEES_002 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.02, type='minecraft:beehive')],
    type='minecraft:tree',
)

OAK_BEES_005 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.05, type='minecraft:beehive')],
    type='minecraft:tree',
)

OAK_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=4,
        height_rand_a=2,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
    ],
    type='minecraft:tree',
)

ORANGE_POPLAR = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:orange_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom')],
    type='minecraft:tree',
)

ORANGE_POPLAR_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:orange_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom'),
    ],
    type='minecraft:tree',
)

ORE_ANCIENT_DEBRIS_LARGE = ConfiguredFeatureScatteredOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_nether', predicate_type='minecraft:tag_match'),
            state='minecraft:ancient_debris',
        ),
    ],
    size=3,
    discard_chance_on_air_exposure=1.0,
    type='minecraft:scattered_ore',
)

ORE_ANCIENT_DEBRIS_SMALL = ConfiguredFeatureScatteredOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_nether', predicate_type='minecraft:tag_match'),
            state='minecraft:ancient_debris',
        ),
    ],
    size=2,
    discard_chance_on_air_exposure=1.0,
    type='minecraft:scattered_ore',
)

ORE_ANDESITE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:andesite',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_BLACKSTONE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:blackstone',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_CLAY = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:clay',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_COAL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:coal_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_coal_ore',
        ),
    ],
    size=17,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_COAL_BURIED = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:coal_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_coal_ore',
        ),
    ],
    size=17,
    discard_chance_on_air_exposure=0.5,
    type='minecraft:ore',
)

ORE_COPPER_LARGE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:copper_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_copper_ore',
        ),
    ],
    size=20,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_COPPER_SMALL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:copper_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_copper_ore',
        ),
    ],
    size=10,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_DIAMOND_BURIED = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:diamond_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_diamond_ore',
        ),
    ],
    size=8,
    discard_chance_on_air_exposure=1.0,
    type='minecraft:ore',
)

ORE_DIAMOND_LARGE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:diamond_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_diamond_ore',
        ),
    ],
    size=12,
    discard_chance_on_air_exposure=0.7,
    type='minecraft:ore',
)

ORE_DIAMOND_MEDIUM = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:diamond_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_diamond_ore',
        ),
    ],
    size=8,
    discard_chance_on_air_exposure=0.5,
    type='minecraft:ore',
)

ORE_DIAMOND_SMALL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:diamond_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_diamond_ore',
        ),
    ],
    size=4,
    discard_chance_on_air_exposure=0.5,
    type='minecraft:ore',
)

ORE_DIORITE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:diorite',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_DIRT = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:dirt',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_EMERALD = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:emerald_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_emerald_ore',
        ),
    ],
    size=3,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_GOLD = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:gold_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_gold_ore',
        ),
    ],
    size=9,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_GOLD_BURIED = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:gold_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_gold_ore',
        ),
    ],
    size=9,
    discard_chance_on_air_exposure=0.5,
    type='minecraft:ore',
)

ORE_GRANITE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:granite',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_GRAVEL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:gravel',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_GRAVEL_NETHER = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:gravel',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_INFESTED = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:infested_stone',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:infested_deepslate',
        ),
    ],
    size=9,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_IRON = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:iron_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_iron_ore',
        ),
    ],
    size=9,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_IRON_SMALL = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:iron_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_iron_ore',
        ),
    ],
    size=4,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_LAPIS = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:lapis_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_lapis_ore',
        ),
    ],
    size=7,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_LAPIS_BURIED = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:lapis_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_lapis_ore',
        ),
    ],
    size=7,
    discard_chance_on_air_exposure=1.0,
    type='minecraft:ore',
)

ORE_MAGMA = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:magma_block',
        ),
    ],
    size=33,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_NETHER_GOLD = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:nether_gold_ore',
        ),
    ],
    size=10,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_QUARTZ = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:nether_quartz_ore',
        ),
    ],
    size=14,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_REDSTONE = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=0,
                                max_inclusive=2031,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:stone_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:redstone_ore',
        ),
        TargetBlock(
            target=RuleTestAnyOf(
                rules=[
                    RuleTestAllOf(
                        rules=[
                            RuleTestTagMatch(
                                tag='minecraft:height_specific_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                            RuleTestHeightMatch(
                                min_inclusive=-2032,
                                max_inclusive=8,
                                predicate_type='minecraft:height_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                    RuleTestAllOf(
                        rules=[
                            RuleTestNot(
                                rule=RuleTestTagMatch(
                                    tag='minecraft:height_specific_ore_replaceables',
                                    predicate_type='minecraft:tag_match',
                                ),
                                predicate_type='minecraft:not',
                            ),
                            RuleTestTagMatch(
                                tag='minecraft:deepslate_ore_replaceables',
                                predicate_type='minecraft:tag_match',
                            ),
                        ],
                        predicate_type='minecraft:all_of',
                    ),
                ],
                predicate_type='minecraft:any_of',
            ),
            state='minecraft:deepslate_redstone_ore',
        ),
    ],
    size=8,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_SOUL_SAND = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestBlockMatch(block='minecraft:netherrack', predicate_type='minecraft:block_match'),
            state='minecraft:soul_sand',
        ),
    ],
    size=12,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

ORE_TUFF = ConfiguredFeatureOre(
    targets=[
        TargetBlock(
            target=RuleTestTagMatch(tag='minecraft:base_stone_overworld', predicate_type='minecraft:tag_match'),
            state='minecraft:tuff',
        ),
    ],
    size=64,
    discard_chance_on_air_exposure=0.0,
    type='minecraft:ore',
)

PALE_FOREST_FLOWER = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:closed_eyeblossom'),
    schedule_tick=True,
    type='minecraft:simple_block',
)

PALE_GARDEN_VEGETATION = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.1, feature='minecraft:pale_oak_creaking_checked'),
        FeaturesStruct(chance=0.9, feature='minecraft:pale_oak_checked'),
    ],
    default='minecraft:pale_oak_checked',
    type='minecraft:random_selector',
)

PALE_MOSS_PATCH = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=1,
    vertical_range=5,
    extra_bottom_block_chance=0.0,
    extra_edge_column_chance=0.75,
    vegetation_chance=0.3,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
    replaceable='#minecraft:moss_replaceable',
    ground_state=FullBlockState(id='minecraft:pale_moss_block'),
    vegetation_feature=PlacedFeature(feature='minecraft:pale_moss_vegetation', placement=[]),
    type='minecraft:vegetation_patch',
)

PALE_MOSS_PATCH_BONEMEAL = ConfiguredFeatureVegetationPatch(
    surface=CaveSurface.FLOOR,
    depth=1,
    vertical_range=5,
    extra_bottom_block_chance=0.0,
    extra_edge_column_chance=0.75,
    vegetation_chance=0.6,
    xz_radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
    replaceable='#minecraft:moss_replaceable',
    ground_state=FullBlockState(id='minecraft:pale_moss_block'),
    vegetation_feature=PlacedFeature(feature='minecraft:pale_moss_vegetation', placement=[]),
    type='minecraft:vegetation_patch',
)

PALE_MOSS_VEGETATION = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=25, data='minecraft:pale_moss_carpet'),
            WeightedEntry(weight=25, data='minecraft:short_grass'),
            WeightedEntry(weight=10, data='minecraft:tall_grass'),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

PALE_OAK = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeThreeLayersFeatureSize(upper_size=2, type='minecraft:three_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:pale_oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:pale_oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerDarkOakTrunkPlacer(
        type='minecraft:dark_oak_trunk_placer',
        base_height=6,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerDarkOakFoliagePlacer(type='minecraft:dark_oak_foliage_placer', radius=0, offset=0),
    decorators=[
        TreeDecoratorPaleMoss(
            leaves_probability=0.15,
            trunk_probability=0.4,
            ground_probability=0.8,
            type='minecraft:pale_moss',
        ),
    ],
    type='minecraft:tree',
)

PALE_OAK_BONEMEAL = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeThreeLayersFeatureSize(upper_size=2, type='minecraft:three_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:pale_oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:pale_oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerDarkOakTrunkPlacer(
        type='minecraft:dark_oak_trunk_placer',
        base_height=6,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerDarkOakFoliagePlacer(type='minecraft:dark_oak_foliage_placer', radius=0, offset=0),
    decorators=[],
    type='minecraft:tree',
)

PALE_OAK_CREAKING = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeThreeLayersFeatureSize(upper_size=2, type='minecraft:three_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:pale_oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:pale_oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerDarkOakTrunkPlacer(
        type='minecraft:dark_oak_trunk_placer',
        base_height=6,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerDarkOakFoliagePlacer(type='minecraft:dark_oak_foliage_placer', radius=0, offset=0),
    decorators=[
        TreeDecoratorPaleMoss(
            leaves_probability=0.15,
            trunk_probability=0.4,
            ground_probability=0.8,
            type='minecraft:pale_moss',
        ),
        TreeDecoratorCreakingHeart(probability=1.0, type='minecraft:creaking_heart'),
    ],
    type='minecraft:tree',
)

PATCH_FIRE = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(
        id='minecraft:fire',
        properties={'age': '0', 'east': 'false', 'north': 'false', 'south': 'false', 'up': 'false', 'west': 'false'},
    ),
    type='minecraft:simple_block',
)

PATCH_SOUL_FIRE = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:soul_fire'), type='minecraft:simple_block')

PILE_HAY = ConfiguredFeatureBlockPile(
    state_provider=TypedBlockStateProviderRotated(
        state=FullBlockState(id='minecraft:hay_block', properties={'axis': 'y'}),
        type='minecraft:rotated',
    ),
    type='minecraft:block_pile',
)

PILE_ICE = ConfiguredFeatureBlockPile(
    state_provider=TypedBlockStateProviderWeighted(
        entries=[WeightedEntry(weight=1, data='minecraft:blue_ice'), WeightedEntry(weight=5, data='minecraft:packed_ice')],
        type='minecraft:weighted',
    ),
    type='minecraft:block_pile',
)

PILE_MELON = ConfiguredFeatureBlockPile(state_provider=FullBlockState(id='minecraft:melon'), type='minecraft:block_pile')

PILE_PUMPKIN = ConfiguredFeatureBlockPile(
    state_provider=TypedBlockStateProviderWeighted(
        entries=[WeightedEntry(weight=19, data='minecraft:pumpkin'), WeightedEntry(weight=1, data='minecraft:jack_o_lantern')],
        type='minecraft:weighted',
    ),
    type='minecraft:block_pile',
)

PILE_SNOW = ConfiguredFeatureBlockPile(
    state_provider=FullBlockState(id='minecraft:snow', properties={'layers': '1'}),
    type='minecraft:block_pile',
)

PINE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(limit=2, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:spruce_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:spruce_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=6,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPineFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 3})),
        type='minecraft:pine_foliage_placer',
        radius=1,
        offset=1,
    ),
    decorators=[],
    type='minecraft:tree',
)

POINTED_DRIPSTONE = ConfiguredFeatureSimpleRandomSelector(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSpeleothem(
                base_block='minecraft:dripstone_block',
                pointed_block='minecraft:pointed_dripstone',
                replaceable_blocks='#minecraft:dripstone_replaceable_blocks',
                type='minecraft:speleothem',
            ),
            placement=[
                PlacementModifierEnvironmentScan(
                    direction_of_search=VerticalDirection.DOWN,
                    max_steps=12,
                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                    allowed_search_condition=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:environment_scan',
                ),
                PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSpeleothem(
                base_block='minecraft:dripstone_block',
                pointed_block='minecraft:pointed_dripstone',
                replaceable_blocks='#minecraft:dripstone_replaceable_blocks',
                type='minecraft:speleothem',
            ),
            placement=[
                PlacementModifierEnvironmentScan(
                    direction_of_search=VerticalDirection.UP,
                    max_steps=12,
                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                    allowed_search_condition=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:environment_scan',
                ),
                PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
            ],
        ),
    ],
    type='minecraft:simple_random_selector',
)

PUMPKIN = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:pumpkin'), type='minecraft:simple_block')

RED_MUSHROOM = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:red_mushroom'), type='minecraft:simple_block')

RED_POPLAR = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:red_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom')],
    type='minecraft:tree',
)

RED_POPLAR_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:red_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom'),
    ],
    type='minecraft:tree',
)

RED_SHRUB = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:red_shrub'), type='minecraft:simple_block')

ROOTED_AZALEA_TREE = ConfiguredFeatureRootSystem(
    required_vertical_space_for_tree=3,
    level_test_distance=0,
    max_level_deviation=0,
    root_radius=3,
    root_placement_attempts=20,
    root_column_max_height=100,
    hanging_root_radius=3,
    hanging_roots_vertical_span=2,
    hanging_root_placement_attempts=20,
    allowed_vertical_water_for_tree=2,
    root_replaceable='#minecraft:azalea_root_replaceable',
    root_state_provider=FullBlockState(id='minecraft:rooted_dirt'),
    hanging_root_state_provider=FullBlockState(id='minecraft:hanging_roots', properties={'waterlogged': 'false'}),
    allowed_tree_position=BlockPredicateAllOf(
        predicates=[
            BlockPredicateAnyOf(
                predicates=[
                    BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                    BlockPredicateMatchingBlockTag(
                        tag='minecraft:replaceable_by_trees',
                        type='minecraft:matching_block_tag',
                    ),
                ],
                type='minecraft:any_of',
            ),
            BlockPredicateMatchingBlockTag(
                offset=(0, -1, 0),
                tag='minecraft:azalea_grows_on',
                type='minecraft:matching_block_tag',
            ),
        ],
        type='minecraft:all_of',
    ),
    feature=PlacedFeature(feature='minecraft:azalea_tree', placement=[]),
    type='minecraft:root_system',
)

ROOTED_SULFUR_SPRING = ConfiguredFeatureRootSystem(
    required_vertical_space_for_tree=5,
    level_test_distance=8,
    max_level_deviation=2,
    root_radius=3,
    root_placement_attempts=20,
    root_column_max_height=184,
    hanging_root_radius=1,
    hanging_roots_vertical_span=1,
    hanging_root_placement_attempts=1,
    allowed_vertical_water_for_tree=1,
    root_replaceable='#minecraft:azalea_root_replaceable',
    root_state_provider=FullBlockState(id='minecraft:sulfur'),
    hanging_root_state_provider=FullBlockState(id='minecraft:sulfur'),
    allowed_tree_position=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    feature=PlacedFeature(feature='minecraft:sulfur_spring', placement=[]),
    type='minecraft:root_system',
)

SCULK_PATCH_ANCIENT_CITY = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSculkPatch(
                charge_count=10,
                amount_per_charge=32,
                spread_attempts=64,
                growth_rounds=0,
                spread_rounds=1,
                type='minecraft:sculk_patch',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureOverlay(
                features=[
                    PlacedFeature(
                        feature=ConfiguredFeatureSimpleBlock(
                            to_place=FullBlockState(id='minecraft:sculk_catalyst', properties={'bloom': 'false'}),
                            type='minecraft:simple_block',
                        ),
                        placement=[
                            PlacementModifierRandomChance(chance=0.5, type='minecraft:random_chance'),
                            PlacementModifierBlockPredicateFilter(
                                predicate=BlockPredicateHasSturdyFace(
                                    offset=(0, -1, 0),
                                    direction=Direction.UP,
                                    type='minecraft:has_sturdy_face',
                                ),
                                type='minecraft:block_predicate_filter',
                            ),
                        ],
                    ),
                    PlacedFeature(
                        feature=ConfiguredFeatureSimpleBlock(
                            to_place=FullBlockState(
                                id='minecraft:sculk_shrieker',
                                properties={'can_summon': 'true', 'shrieking': 'false', 'waterlogged': 'false'},
                            ),
                            type='minecraft:simple_block',
                        ),
                        placement=[
                            PlacementModifierCount(
                                count=IntProvider(
                                    type='minecraft:uniform',
                                    **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 1}),
                                ),
                                type='minecraft:count',
                            ),
                            PlacementModifierOffset(
                                x=IntProvider(
                                    type='minecraft:uniform',
                                    **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': -2}),
                                ),
                                y=IntProvider(
                                    type='minecraft:uniform',
                                    **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': -2}),
                                ),
                                z=IntProvider(
                                    type='minecraft:uniform',
                                    **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': -2}),
                                ),
                                type='minecraft:offset',
                            ),
                            PlacementModifierBlockPredicateFilter(
                                predicate=BlockPredicateAllOf(
                                    predicates=[
                                        BlockPredicateMatchingBlockTag(
                                            tag='minecraft:air',
                                            type='minecraft:matching_block_tag',
                                        ),
                                        BlockPredicateHasSturdyFace(
                                            offset=(0, -1, 0),
                                            direction=Direction.UP,
                                            type='minecraft:has_sturdy_face',
                                        ),
                                    ],
                                    type='minecraft:all_of',
                                ),
                                type='minecraft:block_predicate_filter',
                            ),
                        ],
                    ),
                ],
                type='minecraft:overlay',
            ),
            placement=[],
        ),
    ],
    type='minecraft:sequence',
)

SCULK_PATCH_DEEP_DARK = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSculkPatch(
                charge_count=10,
                amount_per_charge=32,
                spread_attempts=64,
                growth_rounds=0,
                spread_rounds=1,
                type='minecraft:sculk_patch',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:sculk_catalyst', properties={'bloom': 'false'}),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierRandomChance(chance=0.5, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateHasSturdyFace(
                        offset=(0, -1, 0),
                        direction=Direction.UP,
                        type='minecraft:has_sturdy_face',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
    ],
    type='minecraft:sequence',
)

SCULK_VEIN = ConfiguredFeatureMultifaceGrowth(
    block=MultifaceBlock.SCULKVEIN,
    search_range=20,
    chance_of_spreading=1.0,
    can_place_on_floor=True,
    can_place_on_ceiling=True,
    can_place_on_wall=True,
    can_be_placed_on=[
        'minecraft:stone',
        'minecraft:andesite',
        'minecraft:diorite',
        'minecraft:granite',
        'minecraft:dripstone_block',
        'minecraft:calcite',
        'minecraft:tuff',
        'minecraft:deepslate',
    ],
    type='minecraft:multiface_growth',
)

SEAGRASS_MID = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=60,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:tall_seagrass', properties={'half': 'lower'}),
                    type='minecraft:simple_block',
                ),
                placement=[
                    PlacementModifierBlockPredicateFilter(
                        predicate=BlockPredicateMatchingBlocks(
                            offset=(0, 1, 0),
                            blocks='minecraft:water',
                            type='minecraft:matching_blocks',
                        ),
                        type='minecraft:block_predicate_filter',
                    ),
                ],
            ),
        ),
        WeightedEntry(
            weight=40,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:seagrass'),
                    type='minecraft:simple_block',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SEAGRASS_SHORT = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=30,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:tall_seagrass', properties={'half': 'lower'}),
                    type='minecraft:simple_block',
                ),
                placement=[
                    PlacementModifierBlockPredicateFilter(
                        predicate=BlockPredicateMatchingBlocks(
                            offset=(0, 1, 0),
                            blocks='minecraft:water',
                            type='minecraft:matching_blocks',
                        ),
                        type='minecraft:block_predicate_filter',
                    ),
                ],
            ),
        ),
        WeightedEntry(
            weight=70,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:seagrass'),
                    type='minecraft:simple_block',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SEAGRASS_SLIGHTLY_LESS_SHORT = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=40,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:tall_seagrass', properties={'half': 'lower'}),
                    type='minecraft:simple_block',
                ),
                placement=[
                    PlacementModifierBlockPredicateFilter(
                        predicate=BlockPredicateMatchingBlocks(
                            offset=(0, 1, 0),
                            blocks='minecraft:water',
                            type='minecraft:matching_blocks',
                        ),
                        type='minecraft:block_predicate_filter',
                    ),
                ],
            ),
        ),
        WeightedEntry(
            weight=60,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:seagrass'),
                    type='minecraft:simple_block',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SEAGRASS_TALL = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=80,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:tall_seagrass', properties={'half': 'lower'}),
                    type='minecraft:simple_block',
                ),
                placement=[
                    PlacementModifierBlockPredicateFilter(
                        predicate=BlockPredicateMatchingBlocks(
                            offset=(0, 1, 0),
                            blocks='minecraft:water',
                            type='minecraft:matching_blocks',
                        ),
                        type='minecraft:block_predicate_filter',
                    ),
                ],
            ),
        ),
        WeightedEntry(
            weight=20,
            data=PlacedFeature(
                feature=ConfiguredFeatureSimpleBlock(
                    to_place=FullBlockState(id='minecraft:seagrass'),
                    type='minecraft:simple_block',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SEA_PICKLE = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderRandomizedInt(
        property='pickles',
        values=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        source=FullBlockState(id='minecraft:sea_pickle', properties={'pickles': '1', 'waterlogged': 'true'}),
        type='minecraft:randomized_int',
    ),
    type='minecraft:simple_block',
)

SMALL_BASALT_COLUMNS = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=9,
            data=PlacedFeature(
                feature=ConfiguredFeatureSteppedColumnCluster(
                    block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                    can_replace=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:lava',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateHeightRange(
                                        min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                                        max_inclusive=VerticalAnchorStruct4(relative_to_sea_level=0),
                                        type='minecraft:height_range',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    continue_through=BlockPredicateMatchingBlocks(blocks='minecraft:basalt', type='minecraft:matching_blocks'),
                    cannot_place_on='#minecraft:cannot_place_basalt_pillar_on',
                    column_reach=1,
                    column_count=50,
                    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
                    cluster_reach=5,
                    type='minecraft:stepped_column_cluster',
                ),
                placement=[],
            ),
        ),
        WeightedEntry(
            weight=1,
            data=PlacedFeature(
                feature=ConfiguredFeatureSteppedColumnCluster(
                    block=FullBlockState(id='minecraft:basalt', properties={'axis': 'y'}),
                    can_replace=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:lava',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateHeightRange(
                                        min_inclusive=VerticalAnchorStruct2(above_bottom=0),
                                        max_inclusive=VerticalAnchorStruct4(relative_to_sea_level=0),
                                        type='minecraft:height_range',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                        ],
                        type='minecraft:any_of',
                    ),
                    continue_through=BlockPredicateMatchingBlocks(blocks='minecraft:basalt', type='minecraft:matching_blocks'),
                    cannot_place_on='#minecraft:cannot_place_basalt_pillar_on',
                    column_reach=1,
                    column_count=15,
                    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
                    cluster_reach=8,
                    type='minecraft:stepped_column_cluster',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SNOW_LAYER = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:snow', properties={'layers': '1'}),
    type='minecraft:simple_block',
)

SPORE_BLOSSOM = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:spore_blossom'), type='minecraft:simple_block')

SPRING_LAVA_FROZEN = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:lava', properties={'level': '8', 'source': 'true'}),
    valid_blocks=['minecraft:snow_block', 'minecraft:powder_snow', 'minecraft:packed_ice'],
    type='minecraft:spring_feature',
)

SPRING_LAVA_NETHER = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:lava', properties={'level': '8', 'source': 'true'}),
    valid_blocks=['minecraft:netherrack', 'minecraft:soul_sand', 'minecraft:gravel', 'minecraft:magma_block', 'minecraft:blackstone'],
    type='minecraft:spring_feature',
)

SPRING_LAVA_OVERWORLD = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:lava', properties={'level': '8', 'source': 'true'}),
    valid_blocks=[
        'minecraft:stone',
        'minecraft:granite',
        'minecraft:diorite',
        'minecraft:andesite',
        'minecraft:deepslate',
        'minecraft:tuff',
        'minecraft:calcite',
        'minecraft:dirt',
    ],
    type='minecraft:spring_feature',
)

SPRING_NETHER_CLOSED = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:lava', properties={'level': '8', 'source': 'true'}),
    rock_count=5,
    hole_count=0,
    requires_block_below=False,
    valid_blocks='minecraft:netherrack',
    type='minecraft:spring_feature',
)

SPRING_NETHER_OPEN = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:lava', properties={'level': '8', 'source': 'true'}),
    requires_block_below=False,
    valid_blocks='minecraft:netherrack',
    type='minecraft:spring_feature',
)

SPRING_WATER = ConfiguredFeatureSpringFeature(
    state=FluidStateStruct(id='minecraft:water', properties={'level': '8', 'source': 'true'}),
    valid_blocks=[
        'minecraft:stone',
        'minecraft:granite',
        'minecraft:diorite',
        'minecraft:andesite',
        'minecraft:deepslate',
        'minecraft:tuff',
        'minecraft:calcite',
        'minecraft:dirt',
        'minecraft:snow_block',
        'minecraft:powder_snow',
        'minecraft:packed_ice',
    ],
    type='minecraft:spring_feature',
)

SPRUCE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(limit=2, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:spruce_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:spruce_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=1,
    ),
    foliage_placer=FoliagePlacerSpruceFoliagePlacer(
        trunk_height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 1})),
        type='minecraft:spruce_foliage_placer',
        radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 3, 'min_inclusive': 2})),
        offset=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 2, 'min_inclusive': 0})),
    ),
    decorators=[],
    type='minecraft:tree',
)

SUGAR_CANE = ConfiguredFeatureBlockColumn(
    direction=Direction.UP,
    allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    prioritize_tip=False,
    layers=[
        BlockColumnLayer(
            height=IntProvider(type='minecraft:biased_to_bottom', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
            provider=FullBlockState(id='minecraft:sugar_cane', properties={'age': '0'}),
        ),
    ],
    type='minecraft:block_column',
)

SULFUR_POOL = ConfiguredFeatureSequence(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureLake(
                fluid=FullBlockState(id='minecraft:water', properties={'level': '0'}),
                barrier=FullBlockState(id='minecraft:sulfur'),
                can_place_feature=BlockPredicateNot(
                    predicate=BlockPredicateMatchingBlocks(blocks='minecraft:sulfur_spike', type='minecraft:matching_blocks'),
                    type='minecraft:not',
                ),
                can_replace_with_air_or_fluid=BlockPredicateNot(
                    predicate=BlockPredicateMatchingBlockTag(
                        tag='minecraft:features_cannot_replace',
                        type='minecraft:matching_block_tag',
                    ),
                    type='minecraft:not',
                ),
                can_replace_with_barrier=BlockPredicateNot(
                    predicate=BlockPredicateMatchingBlockTag(
                        tag='minecraft:lava_pool_stone_cannot_replace',
                        type='minecraft:matching_block_tag',
                    ),
                    type='minecraft:not',
                ),
                type='minecraft:lake',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSimpleBlock(
                to_place=FullBlockState(id='minecraft:potent_sulfur', properties={'potent_sulfur_state': 'wet'}),
                type='minecraft:simple_block',
            ),
            placement=[
                PlacementModifierEnvironmentScan(
                    direction_of_search=VerticalDirection.DOWN,
                    max_steps=4,
                    target_condition=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateSolid(type='minecraft:solid'),
                            BlockPredicateMatchingFluids(
                                offset=(0, 1, 0),
                                fluids='minecraft:water',
                                state={'source': 'true'},
                                type='minecraft:matching_fluids',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:environment_scan',
                ),
            ],
        ),
    ],
    type='minecraft:sequence',
)

SULFUR_SPIKE = ConfiguredFeatureSimpleRandomSelector(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureSpeleothem(
                base_block='minecraft:sulfur',
                pointed_block='minecraft:sulfur_spike',
                replaceable_blocks='#minecraft:sulfur_spike_replaceable_blocks',
                type='minecraft:speleothem',
            ),
            placement=[
                PlacementModifierEnvironmentScan(
                    direction_of_search=VerticalDirection.DOWN,
                    max_steps=12,
                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                    allowed_search_condition=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:environment_scan',
                ),
                PlacementModifierOffset(x=0, y=1, z=0, type='minecraft:offset'),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureSpeleothem(
                base_block='minecraft:sulfur',
                pointed_block='minecraft:sulfur_spike',
                replaceable_blocks='#minecraft:sulfur_spike_replaceable_blocks',
                type='minecraft:speleothem',
            ),
            placement=[
                PlacementModifierEnvironmentScan(
                    direction_of_search=VerticalDirection.UP,
                    max_steps=12,
                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                    allowed_search_condition=BlockPredicateAnyOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                            BlockPredicateMatchingBlocks(blocks='minecraft:water', type='minecraft:matching_blocks'),
                        ],
                        type='minecraft:any_of',
                    ),
                    type='minecraft:environment_scan',
                ),
                PlacementModifierOffset(x=0, y=-1, z=0, type='minecraft:offset'),
            ],
        ),
    ],
    type='minecraft:simple_random_selector',
)

SULFUR_SPIKE_CLUSTER = ConfiguredFeatureSpeleothemCluster(
    base_block='minecraft:sulfur',
    pointed_block='minecraft:sulfur_spike',
    replaceable_blocks='#minecraft:sulfur_spike_replaceable_blocks',
    floor_to_ceiling_search_range=12,
    height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
    radius=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 8, 'min_inclusive': 2})),
    max_stalagmite_stalactite_height_diff=1,
    height_deviation=3,
    speleothem_block_layer_thickness=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 2})),
    density=FloatProvider(type='minecraft:uniform', **dict[str, Any]({'max_exclusive': 0.7, 'min_inclusive': 0.3})),
    wetness=0.0,
    chance_of_speleothem_at_max_distance_from_center=0.1,
    max_distance_from_edge_affecting_chance_of_speleothem=3,
    max_distance_from_center_affecting_height_bias=8,
    type='minecraft:speleothem_cluster',
)

SULFUR_SPRING = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(
            weight=200,
            data=PlacedFeature(
                feature=ConfiguredFeatureSequence(
                    features=[
                        PlacedFeature(
                            feature=ConfiguredFeatureSimpleBlock(
                                to_place=FullBlockState(id='minecraft:tuff'),
                                type='minecraft:simple_block',
                            ),
                            placement=[
                                PlacementModifierCount(count=64, type='minecraft:count'),
                                PlacementModifierOffset(
                                    x=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0}),
                                    ),
                                    y=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0}),
                                    ),
                                    z=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0}),
                                    ),
                                    type='minecraft:offset',
                                ),
                                PlacementModifierEnvironmentScan(
                                    direction_of_search=VerticalDirection.DOWN,
                                    max_steps=4,
                                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:environment_scan',
                                ),
                                PlacementModifierBlockPredicateFilter(
                                    predicate=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:block_predicate_filter',
                                ),
                            ],
                        ),
                        PlacedFeature(
                            feature=ConfiguredFeatureTemplate(
                                templates=[
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_small_1'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_small_2'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_small_3'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_small_4'),
                                    ),
                                ],
                                type='minecraft:template',
                            ),
                            placement=[PlacementModifierOffset(x=0, y=-7, z=0, type='minecraft:offset')],
                        ),
                    ],
                    type='minecraft:sequence',
                ),
                placement=[],
            ),
        ),
        WeightedEntry(
            weight=90,
            data=PlacedFeature(
                feature=ConfiguredFeatureSequence(
                    features=[
                        PlacedFeature(
                            feature=ConfiguredFeatureSimpleBlock(
                                to_place=FullBlockState(id='minecraft:tuff'),
                                type='minecraft:simple_block',
                            ),
                            placement=[
                                PlacementModifierCount(count=80, type='minecraft:count'),
                                PlacementModifierOffset(
                                    x=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 8, 'min': -8, 'plateau': 0}),
                                    ),
                                    y=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0}),
                                    ),
                                    z=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 8, 'min': -8, 'plateau': 0}),
                                    ),
                                    type='minecraft:offset',
                                ),
                                PlacementModifierEnvironmentScan(
                                    direction_of_search=VerticalDirection.DOWN,
                                    max_steps=4,
                                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:environment_scan',
                                ),
                                PlacementModifierBlockPredicateFilter(
                                    predicate=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:block_predicate_filter',
                                ),
                            ],
                        ),
                        PlacedFeature(
                            feature=ConfiguredFeatureTemplate(
                                templates=[
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_medium_1'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_medium_2'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_medium_3'),
                                    ),
                                ],
                                type='minecraft:template',
                            ),
                            placement=[PlacementModifierOffset(x=0, y=-7, z=0, type='minecraft:offset')],
                        ),
                    ],
                    type='minecraft:sequence',
                ),
                placement=[],
            ),
        ),
        WeightedEntry(
            weight=20,
            data=PlacedFeature(
                feature=ConfiguredFeatureSequence(
                    features=[
                        PlacedFeature(
                            feature=ConfiguredFeatureSimpleBlock(
                                to_place=FullBlockState(id='minecraft:tuff'),
                                type='minecraft:simple_block',
                            ),
                            placement=[
                                PlacementModifierCount(count=96, type='minecraft:count'),
                                PlacementModifierOffset(
                                    x=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 9, 'min': -9, 'plateau': 0}),
                                    ),
                                    y=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0}),
                                    ),
                                    z=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 9, 'min': -9, 'plateau': 0}),
                                    ),
                                    type='minecraft:offset',
                                ),
                                PlacementModifierEnvironmentScan(
                                    direction_of_search=VerticalDirection.DOWN,
                                    max_steps=4,
                                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:environment_scan',
                                ),
                                PlacementModifierBlockPredicateFilter(
                                    predicate=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:block_predicate_filter',
                                ),
                            ],
                        ),
                        PlacedFeature(
                            feature=ConfiguredFeatureTemplate(
                                templates=[
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_large_1'),
                                    ),
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_large_2'),
                                    ),
                                ],
                                type='minecraft:template',
                            ),
                            placement=[PlacementModifierOffset(x=0, y=-7, z=0, type='minecraft:offset')],
                        ),
                    ],
                    type='minecraft:sequence',
                ),
                placement=[],
            ),
        ),
        WeightedEntry(
            weight=5,
            data=PlacedFeature(
                feature=ConfiguredFeatureSequence(
                    features=[
                        PlacedFeature(
                            feature=ConfiguredFeatureSimpleBlock(
                                to_place=FullBlockState(id='minecraft:tuff'),
                                type='minecraft:simple_block',
                            ),
                            placement=[
                                PlacementModifierCount(count=128, type='minecraft:count'),
                                PlacementModifierOffset(
                                    x=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 10, 'min': -10, 'plateau': 0}),
                                    ),
                                    y=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 3, 'min': -3, 'plateau': 0}),
                                    ),
                                    z=IntProvider(
                                        type='minecraft:trapezoid',
                                        **dict[str, Any]({'max': 10, 'min': -10, 'plateau': 0}),
                                    ),
                                    type='minecraft:offset',
                                ),
                                PlacementModifierEnvironmentScan(
                                    direction_of_search=VerticalDirection.DOWN,
                                    max_steps=4,
                                    target_condition=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:environment_scan',
                                ),
                                PlacementModifierBlockPredicateFilter(
                                    predicate=BlockPredicateSolid(type='minecraft:solid'),
                                    type='minecraft:block_predicate_filter',
                                ),
                            ],
                        ),
                        PlacedFeature(
                            feature=ConfiguredFeatureTemplate(
                                templates=[
                                    WeightedEntry(
                                        weight=1,
                                        data=TemplateEntry(id='minecraft:spring/sulfur_spring_extra_large_1'),
                                    ),
                                ],
                                type='minecraft:template',
                            ),
                            placement=[PlacementModifierOffset(x=0, y=-7, z=0, type='minecraft:offset')],
                        ),
                    ],
                    type='minecraft:sequence',
                ),
                placement=[],
            ),
        ),
    ],
    type='minecraft:weighted_random_selector',
)

SUNFLOWER = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:sunflower', properties={'half': 'lower'}),
    type='minecraft:simple_block',
)

SUPER_BIRCH_BEES = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=6,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=1.0, type='minecraft:beehive')],
    type='minecraft:tree',
)

SUPER_BIRCH_BEES_0002 = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:birch_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:birch_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=2,
        height_rand_b=6,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=2, offset=0),
    decorators=[TreeDecoratorBeehive(probability=0.002, type='minecraft:beehive')],
    type='minecraft:tree',
)

SWAMP_OAK = ConfiguredFeatureTree(
    ignore_vines=False,
    minimum_size=FeatureSizeTwoLayersFeatureSize(type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:oak_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:oak_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerStraightTrunkPlacer(
        type='minecraft:straight_trunk_placer',
        base_height=5,
        height_rand_a=3,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerBlobFoliagePlacer(height=3, type='minecraft:blob_foliage_placer', radius=3, offset=0),
    decorators=[TreeDecoratorLeaveVine(probability=0.25, type='minecraft:leave_vine')],
    type='minecraft:tree',
)

TAIGA_GRASS = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[WeightedEntry(weight=1, data='minecraft:short_grass'), WeightedEntry(weight=4, data='minecraft:fern')],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

TALL_GRASS = ConfiguredFeatureSimpleBlock(
    to_place=FullBlockState(id='minecraft:tall_grass', properties={'half': 'lower'}),
    type='minecraft:simple_block',
)

TALL_MANGROVE = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(limit=3, upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:mangrove_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:mangrove_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    root_placer=RootPlacerMangroveRootPlacer(
        mangrove_root_placement=MangroveRootPlacement(
            max_root_width=8,
            max_root_length=15,
            random_skew_chance=0.2,
            can_grow_through='#minecraft:mangrove_roots_can_grow_through',
            muddy_roots_in=['minecraft:mud', 'minecraft:muddy_mangrove_roots'],
            muddy_roots_provider=FullBlockState(id='minecraft:muddy_mangrove_roots', properties={'axis': 'y'}),
        ),
        type='minecraft:mangrove_root_placer',
        root_provider=FullBlockState(id='minecraft:mangrove_roots', properties={'waterlogged': 'false'}),
        trunk_offset_y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 7, 'min_inclusive': 3})),
        above_root_placement=AboveRootPlacement(
            above_root_provider=FullBlockState(id='minecraft:moss_carpet'),
            above_root_placement_chance=0.5,
        ),
    ),
    trunk_placer=TrunkPlacerUpwardsBranchingTrunkPlacer(
        extra_branch_steps=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 1})),
        extra_branch_length=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 1, 'min_inclusive': 0})),
        place_branch_per_log_probability=0.5,
        can_grow_through='#minecraft:mangrove_logs_can_grow_through',
        type='minecraft:upwards_branching_trunk_placer',
        base_height=4,
        height_rand_a=1,
        height_rand_b=9,
    ),
    foliage_placer=FoliagePlacerRandomSpreadFoliagePlacer(
        foliage_height=2,
        leaf_placement_attempts=70,
        type='minecraft:random_spread_foliage_placer',
        radius=3,
        offset=0,
    ),
    decorators=[
        TreeDecoratorLeaveVine(probability=0.125, type='minecraft:leave_vine'),
        TreeDecoratorAttachedToLeaves(
            probability=0.14,
            exclusion_radius_xz=1,
            exclusion_radius_y=0,
            required_empty_blocks=2,
            block_provider='minecraft:mangrove_propagule',
            directions=[Direction.DOWN],
            type='minecraft:attached_to_leaves',
        ),
        TreeDecoratorBeehive(probability=0.01, type='minecraft:beehive'),
    ],
    type='minecraft:tree',
)

TREES_BADLANDS = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree')],
    default='minecraft:oak_leaf_litter',
    type='minecraft:random_selector',
)

TREES_BIRCH = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.0125, feature='minecraft:fallen_birch_tree')],
    default='minecraft:birch_bees_0002',
    type='minecraft:random_selector',
)

TREES_BIRCH_AND_OAK_LEAF_LITTER = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.0025, feature='minecraft:fallen_birch_tree'),
        FeaturesStruct(chance=0.2, feature='minecraft:birch_bees_0002_leaf_litter'),
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_bees_0002_leaf_litter'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree'),
    ],
    default='minecraft:oak_bees_0002_leaf_litter',
    type='minecraft:random_selector',
)

TREES_DAPPLED_FOREST = ConfiguredFeatureWeightedRandomSelector(
    features=[
        WeightedEntry(weight=200, data='minecraft:red_poplar_leaf_litter'),
        WeightedEntry(weight=240, data='minecraft:orange_poplar_leaf_litter'),
        WeightedEntry(weight=90, data='minecraft:yellow_poplar_leaf_litter'),
        WeightedEntry(weight=27, data='minecraft:spruce_checked'),
        WeightedEntry(weight=120, data='minecraft:fallen_poplar_tree'),
    ],
    type='minecraft:weighted_random_selector',
)

TREES_FLOWER_FOREST = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.0025, feature='minecraft:fallen_birch_tree'),
        FeaturesStruct(chance=0.2, feature='minecraft:birch_bees_002'),
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_bees_002'),
    ],
    default='minecraft:oak_bees_002',
    type='minecraft:random_selector',
)

TREES_GROVE = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.33333334, feature='minecraft:pine_on_snow')],
    default='minecraft:spruce_on_snow',
    type='minecraft:random_selector',
)

TREES_JUNGLE = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_checked'),
        FeaturesStruct(chance=0.5, feature='minecraft:jungle_bush'),
        FeaturesStruct(chance=0.33333334, feature='minecraft:mega_jungle_tree_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_jungle_tree'),
    ],
    default='minecraft:jungle_tree',
    type='minecraft:random_selector',
)

TREES_OLD_GROWTH_PINE_TAIGA = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.025641026, feature='minecraft:mega_spruce_checked'),
        FeaturesStruct(chance=0.30769232, feature='minecraft:mega_pine_checked'),
        FeaturesStruct(chance=0.33333334, feature='minecraft:pine_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_spruce_tree'),
    ],
    default='minecraft:spruce_checked',
    type='minecraft:random_selector',
)

TREES_OLD_GROWTH_SPRUCE_TAIGA = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.33333334, feature='minecraft:mega_spruce_checked'),
        FeaturesStruct(chance=0.33333334, feature='minecraft:pine_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_spruce_tree'),
    ],
    default='minecraft:spruce_checked',
    type='minecraft:random_selector',
)

TREES_PLAINS = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.33333334, feature=PlacedFeature(feature='minecraft:fancy_oak_bees_005', placement=[])),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree'),
    ],
    default=PlacedFeature(feature='minecraft:oak_bees_005', placement=[]),
    type='minecraft:random_selector',
)

TREES_SAVANNA = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.8, feature='minecraft:acacia_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree'),
    ],
    default='minecraft:oak_checked',
    type='minecraft:random_selector',
)

TREES_SNOWY = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.0125, feature='minecraft:fallen_spruce_tree')],
    default='minecraft:spruce_checked',
    type='minecraft:random_selector',
)

TREES_SPARSE_JUNGLE = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_checked'),
        FeaturesStruct(chance=0.5, feature='minecraft:jungle_bush'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_jungle_tree'),
    ],
    default='minecraft:jungle_tree',
    type='minecraft:random_selector',
)

TREES_TAIGA = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.33333334, feature='minecraft:pine_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_spruce_tree'),
    ],
    default='minecraft:spruce_checked',
    type='minecraft:random_selector',
)

TREES_WATER = ConfiguredFeatureRandomSelector(
    features=[FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_checked')],
    default='minecraft:oak_checked',
    type='minecraft:random_selector',
)

TREES_WINDSWEPT_HILLS = ConfiguredFeatureRandomSelector(
    features=[
        FeaturesStruct(chance=0.008325, feature='minecraft:fallen_spruce_tree'),
        FeaturesStruct(chance=0.666, feature='minecraft:spruce_checked'),
        FeaturesStruct(chance=0.1, feature='minecraft:fancy_oak_checked'),
        FeaturesStruct(chance=0.0125, feature='minecraft:fallen_oak_tree'),
    ],
    default='minecraft:oak_checked',
    type='minecraft:random_selector',
)

TWISTING_VINES = ConfiguredFeatureBlockColumn(
    direction=Direction.UP,
    allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
    prioritize_tip=True,
    layers=[
        BlockColumnLayer(
            height=IntProvider(
                type='minecraft:weighted_list',
                **dict[str, Any]({
                    'distribution': [
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 7, 'min_inclusive': 0}, 'weight': 10},
                        {'data': {'type': 'minecraft:uniform', 'max_inclusive': 15, 'min_inclusive': 1}, 'weight': 2},
                        {'data': 0, 'weight': 3},
                    ],
                }),
            ),
            provider=FullBlockState(id='minecraft:twisting_vines_plant'),
        ),
        BlockColumnLayer(
            height=1,
            provider=TypedBlockStateProviderRandomizedInt(
                property='age',
                values=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 25, 'min_inclusive': 17})),
                source=FullBlockState(id='minecraft:twisting_vines', properties={'age': '0'}),
                type='minecraft:randomized_int',
            ),
        ),
    ],
    type='minecraft:block_column',
)

UNDERWATER_MAGMA = ConfiguredFeatureUnderwaterMagma(
    floor_search_range=5,
    placement_radius_around_floor=1,
    placement_probability_per_valid_position=0.5,
    type='minecraft:underwater_magma',
)

VINES = ConfiguredFeatureVines(type='minecraft:vines')

VOID_START_PLATFORM = ConfiguredFeatureVoidStartPlatform(type='minecraft:void_start_platform')

WARM_OCEAN_VEGETATION = ConfiguredFeatureSimpleRandomSelector(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureCoralTree(
                feature=PlacedFeature(
                    feature='minecraft:coral/tube_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_tree',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralClaw(
                feature=PlacedFeature(
                    feature='minecraft:coral/tube_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_claw',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature='minecraft:coral/tube_block',
            placement=[
                PlacementModifierOffset(
                    x=0,
                    y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': -1, 'min_inclusive': -3})),
                    z=0,
                    type='minecraft:offset',
                ),
                PlacementModifierCuboid(
                    xz_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    y_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    include_interior=False,
                    include_edges=False,
                    type='minecraft:cuboid',
                ),
                PlacementModifierRandomChance(chance=0.9, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateAnyOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateMatchingBlockTag(
                                        tag='minecraft:corals',
                                        type='minecraft:matching_block_tag',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            BlockPredicateMatchingBlocks(
                                offset=(0, 1, 0),
                                blocks='minecraft:water',
                                type='minecraft:matching_blocks',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralTree(
                feature=PlacedFeature(
                    feature='minecraft:coral/brain_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_tree',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralClaw(
                feature=PlacedFeature(
                    feature='minecraft:coral/brain_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_claw',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature='minecraft:coral/brain_block',
            placement=[
                PlacementModifierOffset(
                    x=0,
                    y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': -1, 'min_inclusive': -3})),
                    z=0,
                    type='minecraft:offset',
                ),
                PlacementModifierCuboid(
                    xz_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    y_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    include_interior=False,
                    include_edges=False,
                    type='minecraft:cuboid',
                ),
                PlacementModifierRandomChance(chance=0.9, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateAnyOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateMatchingBlockTag(
                                        tag='minecraft:corals',
                                        type='minecraft:matching_block_tag',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            BlockPredicateMatchingBlocks(
                                offset=(0, 1, 0),
                                blocks='minecraft:water',
                                type='minecraft:matching_blocks',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralTree(
                feature=PlacedFeature(
                    feature='minecraft:coral/bubble_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_tree',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralClaw(
                feature=PlacedFeature(
                    feature='minecraft:coral/bubble_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_claw',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature='minecraft:coral/bubble_block',
            placement=[
                PlacementModifierOffset(
                    x=0,
                    y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': -1, 'min_inclusive': -3})),
                    z=0,
                    type='minecraft:offset',
                ),
                PlacementModifierCuboid(
                    xz_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    y_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    include_interior=False,
                    include_edges=False,
                    type='minecraft:cuboid',
                ),
                PlacementModifierRandomChance(chance=0.9, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateAnyOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateMatchingBlockTag(
                                        tag='minecraft:corals',
                                        type='minecraft:matching_block_tag',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            BlockPredicateMatchingBlocks(
                                offset=(0, 1, 0),
                                blocks='minecraft:water',
                                type='minecraft:matching_blocks',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralTree(
                feature=PlacedFeature(
                    feature='minecraft:coral/fire_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_tree',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralClaw(
                feature=PlacedFeature(
                    feature='minecraft:coral/fire_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_claw',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature='minecraft:coral/fire_block',
            placement=[
                PlacementModifierOffset(
                    x=0,
                    y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': -1, 'min_inclusive': -3})),
                    z=0,
                    type='minecraft:offset',
                ),
                PlacementModifierCuboid(
                    xz_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    y_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    include_interior=False,
                    include_edges=False,
                    type='minecraft:cuboid',
                ),
                PlacementModifierRandomChance(chance=0.9, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateAnyOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateMatchingBlockTag(
                                        tag='minecraft:corals',
                                        type='minecraft:matching_block_tag',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            BlockPredicateMatchingBlocks(
                                offset=(0, 1, 0),
                                blocks='minecraft:water',
                                type='minecraft:matching_blocks',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralTree(
                feature=PlacedFeature(
                    feature='minecraft:coral/horn_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_tree',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureCoralClaw(
                feature=PlacedFeature(
                    feature='minecraft:coral/horn_block',
                    placement=[
                        PlacementModifierBlockPredicateFilter(
                            predicate=BlockPredicateAllOf(
                                predicates=[
                                    BlockPredicateAnyOf(
                                        predicates=[
                                            BlockPredicateMatchingBlocks(
                                                blocks='minecraft:water',
                                                type='minecraft:matching_blocks',
                                            ),
                                            BlockPredicateMatchingBlockTag(
                                                tag='minecraft:corals',
                                                type='minecraft:matching_block_tag',
                                            ),
                                        ],
                                        type='minecraft:any_of',
                                    ),
                                    BlockPredicateMatchingBlocks(
                                        offset=(0, 1, 0),
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                ],
                                type='minecraft:all_of',
                            ),
                            type='minecraft:block_predicate_filter',
                        ),
                    ],
                ),
                type='minecraft:coral_claw',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature='minecraft:coral/horn_block',
            placement=[
                PlacementModifierOffset(
                    x=0,
                    y=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': -1, 'min_inclusive': -3})),
                    z=0,
                    type='minecraft:offset',
                ),
                PlacementModifierCuboid(
                    xz_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    y_size=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 4})),
                    include_interior=False,
                    include_edges=False,
                    type='minecraft:cuboid',
                ),
                PlacementModifierRandomChance(chance=0.9, type='minecraft:random_chance'),
                PlacementModifierBlockPredicateFilter(
                    predicate=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateAnyOf(
                                predicates=[
                                    BlockPredicateMatchingBlocks(
                                        blocks='minecraft:water',
                                        type='minecraft:matching_blocks',
                                    ),
                                    BlockPredicateMatchingBlockTag(
                                        tag='minecraft:corals',
                                        type='minecraft:matching_block_tag',
                                    ),
                                ],
                                type='minecraft:any_of',
                            ),
                            BlockPredicateMatchingBlocks(
                                offset=(0, 1, 0),
                                blocks='minecraft:water',
                                type='minecraft:matching_blocks',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    type='minecraft:block_predicate_filter',
                ),
            ],
        ),
    ],
    type='minecraft:simple_random_selector',
)

WARPED_FOREST_VEGETATION = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=85, data='minecraft:warped_roots'),
            WeightedEntry(weight=1, data='minecraft:crimson_roots'),
            WeightedEntry(weight=13, data='minecraft:warped_fungus'),
            WeightedEntry(weight=1, data='minecraft:crimson_fungus'),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

WARPED_FUNGUS = ConfiguredFeatureHugeFungus(
    hat_state='minecraft:warped_wart_block',
    decor_state='minecraft:shroomlight',
    stem_state='minecraft:warped_stem',
    valid_base_block='minecraft:warped_nylium',
    replaceable_blocks=BlockPredicateMatchingBlocks(
        blocks=[
            'minecraft:oak_sapling',
            'minecraft:spruce_sapling',
            'minecraft:birch_sapling',
            'minecraft:jungle_sapling',
            'minecraft:acacia_sapling',
            'minecraft:cherry_sapling',
            'minecraft:dark_oak_sapling',
            'minecraft:pale_oak_sapling',
            'minecraft:mangrove_propagule',
            'minecraft:dandelion',
            'minecraft:torchflower',
            'minecraft:poppy',
            'minecraft:blue_orchid',
            'minecraft:allium',
            'minecraft:azure_bluet',
            'minecraft:red_tulip',
            'minecraft:orange_tulip',
            'minecraft:white_tulip',
            'minecraft:pink_tulip',
            'minecraft:oxeye_daisy',
            'minecraft:cornflower',
            'minecraft:wither_rose',
            'minecraft:lily_of_the_valley',
            'minecraft:brown_mushroom',
            'minecraft:red_mushroom',
            'minecraft:wheat',
            'minecraft:sugar_cane',
            'minecraft:attached_pumpkin_stem',
            'minecraft:attached_melon_stem',
            'minecraft:pumpkin_stem',
            'minecraft:melon_stem',
            'minecraft:lily_pad',
            'minecraft:nether_wart',
            'minecraft:cocoa',
            'minecraft:carrots',
            'minecraft:potatoes',
            'minecraft:chorus_plant',
            'minecraft:chorus_flower',
            'minecraft:torchflower_crop',
            'minecraft:pitcher_crop',
            'minecraft:beetroots',
            'minecraft:sweet_berry_bush',
            'minecraft:warped_fungus',
            'minecraft:crimson_fungus',
            'minecraft:weeping_vines',
            'minecraft:weeping_vines_plant',
            'minecraft:twisting_vines',
            'minecraft:twisting_vines_plant',
            'minecraft:cave_vines',
            'minecraft:cave_vines_plant',
            'minecraft:spore_blossom',
            'minecraft:azalea',
            'minecraft:flowering_azalea',
            'minecraft:moss_carpet',
            'minecraft:pink_petals',
            'minecraft:wildflowers',
            'minecraft:big_dripleaf',
            'minecraft:big_dripleaf_stem',
            'minecraft:small_dripleaf',
        ],
        type='minecraft:matching_blocks',
    ),
    type='minecraft:huge_fungus',
)

WARPED_FUNGUS_PLANTED = ConfiguredFeatureHugeFungus(
    hat_state='minecraft:warped_wart_block',
    decor_state='minecraft:shroomlight',
    stem_state='minecraft:warped_stem',
    valid_base_block='minecraft:warped_nylium',
    planted=True,
    replaceable_blocks=BlockPredicateMatchingBlocks(
        blocks=[
            'minecraft:oak_sapling',
            'minecraft:spruce_sapling',
            'minecraft:birch_sapling',
            'minecraft:jungle_sapling',
            'minecraft:acacia_sapling',
            'minecraft:cherry_sapling',
            'minecraft:dark_oak_sapling',
            'minecraft:pale_oak_sapling',
            'minecraft:mangrove_propagule',
            'minecraft:dandelion',
            'minecraft:torchflower',
            'minecraft:poppy',
            'minecraft:blue_orchid',
            'minecraft:allium',
            'minecraft:azure_bluet',
            'minecraft:red_tulip',
            'minecraft:orange_tulip',
            'minecraft:white_tulip',
            'minecraft:pink_tulip',
            'minecraft:oxeye_daisy',
            'minecraft:cornflower',
            'minecraft:wither_rose',
            'minecraft:lily_of_the_valley',
            'minecraft:brown_mushroom',
            'minecraft:red_mushroom',
            'minecraft:wheat',
            'minecraft:sugar_cane',
            'minecraft:attached_pumpkin_stem',
            'minecraft:attached_melon_stem',
            'minecraft:pumpkin_stem',
            'minecraft:melon_stem',
            'minecraft:lily_pad',
            'minecraft:nether_wart',
            'minecraft:cocoa',
            'minecraft:carrots',
            'minecraft:potatoes',
            'minecraft:chorus_plant',
            'minecraft:chorus_flower',
            'minecraft:torchflower_crop',
            'minecraft:pitcher_crop',
            'minecraft:beetroots',
            'minecraft:sweet_berry_bush',
            'minecraft:warped_fungus',
            'minecraft:crimson_fungus',
            'minecraft:weeping_vines',
            'minecraft:weeping_vines_plant',
            'minecraft:twisting_vines',
            'minecraft:twisting_vines_plant',
            'minecraft:cave_vines',
            'minecraft:cave_vines_plant',
            'minecraft:spore_blossom',
            'minecraft:azalea',
            'minecraft:flowering_azalea',
            'minecraft:moss_carpet',
            'minecraft:pink_petals',
            'minecraft:wildflowers',
            'minecraft:big_dripleaf',
            'minecraft:big_dripleaf_stem',
            'minecraft:small_dripleaf',
        ],
        type='minecraft:matching_blocks',
    ),
    type='minecraft:huge_fungus',
)

WATERLILY = ConfiguredFeatureSimpleBlock(to_place=FullBlockState(id='minecraft:lily_pad'), type='minecraft:simple_block')

WEEPING_VINES = ConfiguredFeatureOverlay(
    features=[
        PlacedFeature(
            feature=ConfiguredFeatureRandomNeighborSpread(
                block=FullBlockState(id='minecraft:nether_wart_block'),
                accepted_neighbors=['minecraft:netherrack', 'minecraft:nether_wart_block'],
                can_replace=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                attempts=200,
                xz_offset=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 5, 'min': -5, 'plateau': 0})),
                y_offset=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 1, 'min': -4, 'plateau': 3})),
                type='minecraft:random_neighbor_spread',
            ),
            placement=[],
        ),
        PlacedFeature(
            feature=ConfiguredFeatureBlockColumn(
                direction=Direction.DOWN,
                allowed_placement=BlockPredicateMatchingBlockTag(tag='minecraft:air', type='minecraft:matching_block_tag'),
                prioritize_tip=True,
                layers=[
                    BlockColumnLayer(
                        height=IntProvider(
                            type='minecraft:weighted_list',
                            **dict[str, Any]({
                                'distribution': [
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 8, 'min_inclusive': 1},
                                        'weight': 10,
                                    },
                                    {
                                        'data': {'type': 'minecraft:uniform', 'max_inclusive': 17, 'min_inclusive': 2},
                                        'weight': 2,
                                    },
                                    {'data': 1, 'weight': 3},
                                ],
                            }),
                        ),
                        provider=FullBlockState(id='minecraft:weeping_vines_plant'),
                    ),
                    BlockColumnLayer(
                        height=1,
                        provider=TypedBlockStateProviderRandomizedInt(
                            property='age',
                            values=IntProvider(
                                type='minecraft:uniform',
                                **dict[str, Any]({'max_inclusive': 25, 'min_inclusive': 17}),
                            ),
                            source=FullBlockState(id='minecraft:weeping_vines', properties={'age': '0'}),
                            type='minecraft:randomized_int',
                        ),
                    ),
                ],
                type='minecraft:block_column',
            ),
            placement=[
                PlacementModifierCount(count=100, type='minecraft:count'),
                PlacementModifierOffset(
                    x=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
                    y=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 1, 'min': -4, 'plateau': 3})),
                    z=IntProvider(type='minecraft:trapezoid', **dict[str, Any]({'max': 7, 'min': -7, 'plateau': 0})),
                    type='minecraft:offset',
                ),
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
        ),
    ],
    type='minecraft:overlay',
)

WILDFLOWER = ConfiguredFeatureSimpleBlock(
    to_place=TypedBlockStateProviderWeighted(
        entries=[
            WeightedEntry(weight=1, data='minecraft:wildflowers'),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'east', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'south', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'west', 'flower_amount': '1'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'north', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'east', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'south', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'west', 'flower_amount': '2'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'north', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'east', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'south', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'west', 'flower_amount': '3'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'north', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'east', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'south', 'flower_amount': '4'}),
            ),
            WeightedEntry(
                weight=1,
                data=FullBlockState(id='minecraft:wildflowers', properties={'facing': 'west', 'flower_amount': '4'}),
            ),
        ],
        type='minecraft:weighted',
    ),
    type='minecraft:simple_block',
)

YELLOW_POPLAR = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:yellow_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom')],
    type='minecraft:tree',
)

YELLOW_POPLAR_LEAF_LITTER = ConfiguredFeatureTree(
    ignore_vines=True,
    minimum_size=FeatureSizeTwoLayersFeatureSize(upper_size=2, type='minecraft:two_layers_feature_size'),
    below_trunk_provider='minecraft:soil_beneath_tree',
    trunk_provider=FullBlockState(id='minecraft:poplar_log', properties={'axis': 'y'}),
    foliage_provider=FullBlockState(
        id='minecraft:yellow_poplar_leaves',
        properties={'distance': '7', 'persistent': 'false', 'waterlogged': 'false'},
    ),
    trunk_placer=TrunkPlacerPoplarTrunkPlacer(
        trunk_height_above_branches=4,
        branch_amount=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 4, 'min_inclusive': 1})),
        type='minecraft:poplar_trunk_placer',
        base_height=7,
        height_rand_a=4,
        height_rand_b=0,
    ),
    foliage_placer=FoliagePlacerPoplarFoliagePlacer(
        height=IntProvider(type='minecraft:uniform', **dict[str, Any]({'max_inclusive': 6, 'min_inclusive': 5})),
        side_hole_chance=0.15,
        type='minecraft:poplar_foliage_placer',
        radius=IntProvider(
            type='minecraft:weighted_list',
            **dict[str, Any]({
                'distribution': [{'data': 5, 'weight': 5}, {'data': 6, 'weight': 5}, {'data': 7, 'weight': 1}, {'data': 8, 'weight': 1}],
            }),
        ),
        offset=0,
    ),
    decorators=[
        TreeDecoratorPlaceOnGround(
            tries=96,
            radius=4,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorPlaceOnGround(
            tries=150,
            height=2,
            block_state_provider=TypedBlockStateProviderWeighted(
                entries=[
                    WeightedEntry(weight=1, data='minecraft:leaf_litter'),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '1'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '1'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '2'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '2'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '3'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '3'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'north', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'east', 'segment_amount': '4'}),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(
                            id='minecraft:leaf_litter',
                            properties={'facing': 'south', 'segment_amount': '4'},
                        ),
                    ),
                    WeightedEntry(
                        weight=1,
                        data=FullBlockState(id='minecraft:leaf_litter', properties={'facing': 'west', 'segment_amount': '4'}),
                    ),
                ],
                type='minecraft:weighted',
            ),
            type='minecraft:place_on_ground',
        ),
        TreeDecoratorShelfMushroom(probability=0.4, type='minecraft:shelf_mushroom'),
    ],
    type='minecraft:tree',
)
