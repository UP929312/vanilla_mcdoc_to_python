"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::BlockPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/BlockPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.block_predicate.BelowHeightmapPredicate import BelowHeightmapPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.CombiningPredicate import CombiningPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.HasSturdyFacePredicate import HasSturdyFacePredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.HeightRangePredicate import HeightRangePredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.InsideWorldBoundsPredicate import InsideWorldBoundsPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingBiomesPredicate import MatchingBiomesPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingBlockTagPredicate import MatchingBlockTagPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingBlocksPredicate import MatchingBlocksPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingFluidsPredicate import MatchingFluidsPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.NotPredicate import NotPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.UnobstructedPredicate import UnobstructedPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.VolumeMatchPredicate import VolumeMatchPredicate
from vanilla_mcdoc.data.worldgen.feature.block_predicate.WouldSurvivePredicate import WouldSurvivePredicate


class BlockPredicateAllOf(CombiningPredicate):
    type: Literal['minecraft:all_of', 'all_of'] = 'minecraft:all_of'


class BlockPredicateAnyOf(CombiningPredicate):
    type: Literal['minecraft:any_of', 'any_of'] = 'minecraft:any_of'


class BlockPredicateBelowHeightmap(BelowHeightmapPredicate):
    type: Literal['minecraft:below_heightmap', 'below_heightmap'] = 'minecraft:below_heightmap'


class BlockPredicateHasSturdyFace(HasSturdyFacePredicate):
    type: Literal['minecraft:has_sturdy_face', 'has_sturdy_face'] = 'minecraft:has_sturdy_face'


class BlockPredicateHeightRange(HeightRangePredicate):
    type: Literal['minecraft:height_range', 'height_range'] = 'minecraft:height_range'


class BlockPredicateInsideWorldBounds(InsideWorldBoundsPredicate):
    type: Literal['minecraft:inside_world_bounds', 'inside_world_bounds'] = 'minecraft:inside_world_bounds'


class BlockPredicateMatchingBiomes(MatchingBiomesPredicate):
    type: Literal['minecraft:matching_biomes', 'matching_biomes'] = 'minecraft:matching_biomes'


class BlockPredicateMatchingBlockTag(MatchingBlockTagPredicate):
    type: Literal['minecraft:matching_block_tag', 'matching_block_tag'] = 'minecraft:matching_block_tag'


class BlockPredicateMatchingBlocks(MatchingBlocksPredicate):
    type: Literal['minecraft:matching_blocks', 'matching_blocks'] = 'minecraft:matching_blocks'


class BlockPredicateMatchingFluids(MatchingFluidsPredicate):
    type: Literal['minecraft:matching_fluids', 'matching_fluids'] = 'minecraft:matching_fluids'


class BlockPredicateNot(NotPredicate):
    type: Literal['minecraft:not', 'not'] = 'minecraft:not'


class BlockPredicateUnobstructed(UnobstructedPredicate):
    type: Literal['minecraft:unobstructed', 'unobstructed'] = 'minecraft:unobstructed'


class BlockPredicateVolumeMatch(VolumeMatchPredicate):
    type: Literal['minecraft:volume_match', 'volume_match'] = 'minecraft:volume_match'


class BlockPredicateWouldSurvive(WouldSurvivePredicate):
    type: Literal['minecraft:would_survive', 'would_survive'] = 'minecraft:would_survive'


type BlockPredicate = Annotated[
    BlockPredicateAllOf | BlockPredicateAnyOf | BlockPredicateBelowHeightmap | BlockPredicateHasSturdyFace | BlockPredicateHeightRange | BlockPredicateInsideWorldBounds | BlockPredicateMatchingBiomes | BlockPredicateMatchingBlockTag | BlockPredicateMatchingBlocks | BlockPredicateMatchingFluids | BlockPredicateNot | BlockPredicateUnobstructed | BlockPredicateVolumeMatch | BlockPredicateWouldSurvive,
    Field(discriminator='type'),
]
