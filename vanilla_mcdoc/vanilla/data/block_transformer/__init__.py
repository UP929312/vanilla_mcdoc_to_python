"""Vanilla's data/block_transformer/ files"""
from vanilla_mcdoc.data.block_transformer.BlockTransformData import BlockTransformData
from vanilla_mcdoc.data.block_transformer.BlockTransformDropStrategy import BlockTransformDropStrategy
from vanilla_mcdoc.data.block_transformer.BlockTransformParticle import BlockTransformParticle
from vanilla_mcdoc.data.block_transformer.BlockTransformType import BlockTransformType
from vanilla_mcdoc.data.worldgen.feature.RuleBasedBlockStateProvider import RulesStruct
from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicateAllOf, BlockPredicateMatchingBlockTag, BlockPredicateMatchingBlocks
from vanilla_mcdoc.data.worldgen.feature.block_state_provider.TypedBlockStateProvider import TypedBlockStateProviderCopyProperties, TypedBlockStateProviderRuleBased
from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState
from vanilla_mcdoc.util.direction.Direction import Direction

AXE = [
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:oak_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_oak_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:oak_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_oak_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:dark_oak_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_dark_oak_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:dark_oak_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_dark_oak_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:pale_oak_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_pale_oak_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:pale_oak_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_pale_oak_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:poplar_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_poplar_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:poplar_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_poplar_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:acacia_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_acacia_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:acacia_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_acacia_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:cherry_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_cherry_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:cherry_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_cherry_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:birch_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_birch_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:birch_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_birch_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:jungle_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_jungle_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:jungle_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_jungle_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:spruce_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_spruce_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:spruce_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_spruce_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:warped_stem', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_warped_stem', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:warped_hyphae', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_warped_hyphae', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:crimson_stem', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_crimson_stem', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:crimson_hyphae', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_crimson_hyphae', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:mangrove_wood', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_mangrove_wood', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:mangrove_log', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_mangrove_log', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:bamboo_block', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:stripped_bamboo_block', properties={'axis': 'y'}),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.strip',
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:exposed_copper', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_block'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:weathered_copper', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:oxidized_copper', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_bulb', properties={'lit': 'false', 'powered': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_bulb',
                            properties={'lit': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_bulb',
                            properties={'lit': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_chain', properties={'axis': 'y', 'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_chain',
                            properties={'axis': 'y', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_chain',
                            properties={'axis': 'y', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.scrape',
        particle=BlockTransformParticle.SCRAPE,
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.scrape',
        particle=BlockTransformParticle.SCRAPE,
        transform_type=BlockTransformType.COPPERCHEST,
        update_from_neighbors=False,
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:exposed_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:weathered_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:oxidized_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.scrape',
        particle=BlockTransformParticle.SCRAPE,
        update_from_neighbors=False,
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_block',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_block'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:oxidized_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:waxed_cut_copper', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_cut_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:oxidized_cut_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_cut_copper_slab',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_cut_copper_slab',
                            properties={'type': 'bottom', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_cut_copper_stairs',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_cut_copper_stairs',
                            properties={'facing': 'north', 'half': 'bottom', 'shape': 'straight', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_chiseled_copper',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:oxidized_chiseled_copper'),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_trapdoor',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_trapdoor',
                            properties={
                                'facing': 'north',
                                'half': 'bottom',
                                'open': 'false',
                                'powered': 'false',
                                'waterlogged': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:waxed_copper_bars', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_bars',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_bars',
                            properties={
                                'east': 'false',
                                'north': 'false',
                                'south': 'false',
                                'waterlogged': 'false',
                                'west': 'false',
                            },
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:exposed_copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:weathered_copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_grate',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:oxidized_copper_grate', properties={'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:waxed_copper_bulb', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_bulb', properties={'lit': 'false', 'powered': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_bulb',
                            properties={'lit': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_bulb',
                            properties={'lit': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_bulb',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_bulb',
                            properties={'lit': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_golem_statue',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_golem_statue',
                            properties={'copper_golem_pose': 'standing', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_lightning_rod',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_lightning_rod',
                            properties={'facing': 'up', 'powered': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_lantern',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_lantern',
                            properties={'hanging': 'false', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(id='minecraft:copper_chain', properties={'axis': 'y', 'waterlogged': 'false'}),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_chain',
                            properties={'axis': 'y', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_chain',
                            properties={'axis': 'y', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_chain',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_chain',
                            properties={'axis': 'y', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.wax_off',
        particle=BlockTransformParticle.WAXOFF,
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_chest',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_chest',
                            properties={'type': 'single', 'facing': 'north', 'waterlogged': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.wax_off',
        particle=BlockTransformParticle.WAXOFF,
        transform_type=BlockTransformType.COPPERCHEST,
        update_from_neighbors=False,
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:waxed_copper_door', type='minecraft:matching_blocks'),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_exposed_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:exposed_copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_weathered_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:weathered_copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(
                        blocks='minecraft:waxed_oxidized_copper_door',
                        type='minecraft:matching_blocks',
                    ),
                    then=TypedBlockStateProviderCopyProperties(
                        source=FullBlockState(
                            id='minecraft:oxidized_copper_door',
                            properties={'facing': 'north', 'half': 'lower', 'hinge': 'left', 'open': 'false', 'powered': 'false'},
                        ),
                        type='minecraft:copy_properties',
                    ),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.axe.wax_off',
        particle=BlockTransformParticle.WAXOFF,
        update_from_neighbors=False,
        item_damage_per_use=1,
    ),
]

HOE = [
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(
                                tag='minecraft:turns_into_farmland',
                                type='minecraft:matching_block_tag',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, 1, 0),
                                tag='minecraft:air',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    then=FullBlockState(id='minecraft:farmland', properties={'moisture': '0'}),
                ),
                RulesStruct(
                    if_true=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateMatchingBlocks(
                                blocks='minecraft:coarse_dirt',
                                type='minecraft:matching_blocks',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, 1, 0),
                                tag='minecraft:air',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    then=FullBlockState(id='minecraft:dirt'),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.hoe.till',
        disallowed_faces=[Direction.DOWN],
        item_damage_per_use=1,
    ),
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateMatchingBlocks(blocks='minecraft:rooted_dirt', type='minecraft:matching_blocks'),
                    then=FullBlockState(id='minecraft:dirt'),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.hoe.till',
        loot='minecraft:till/rooted_dirt',
        drop_strategy=BlockTransformDropStrategy.CLICKEDFACE,
        item_damage_per_use=1,
    ),
]

SHOVEL = [
    BlockTransformData(
        block_state_provider=TypedBlockStateProviderRuleBased(
            rules=[
                RulesStruct(
                    if_true=BlockPredicateAllOf(
                        predicates=[
                            BlockPredicateMatchingBlockTag(
                                tag='minecraft:turns_into_dirt_path',
                                type='minecraft:matching_block_tag',
                            ),
                            BlockPredicateMatchingBlockTag(
                                offset=(0, 1, 0),
                                tag='minecraft:air',
                                type='minecraft:matching_block_tag',
                            ),
                        ],
                        type='minecraft:all_of',
                    ),
                    then=FullBlockState(id='minecraft:dirt_path'),
                ),
            ],
            type='minecraft:rule_based',
        ),
        sound='minecraft:item.shovel.flatten',
        disallowed_faces=[Direction.DOWN],
        item_damage_per_use=1,
    ),
]
