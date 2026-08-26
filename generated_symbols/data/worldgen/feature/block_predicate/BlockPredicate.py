"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::BlockPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/BlockPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.feature.block_predicate.CombiningPredicate import CombiningPredicate
from generated_symbols.data.worldgen.feature.block_predicate.HasSturdyFacePredicate import HasSturdyFacePredicate
from generated_symbols.data.worldgen.feature.block_predicate.HeightRangePredicate import HeightRangePredicate
from generated_symbols.data.worldgen.feature.block_predicate.InsideWorldBoundsPredicate import InsideWorldBoundsPredicate
from generated_symbols.data.worldgen.feature.block_predicate.MatchingBiomesPredicate import MatchingBiomesPredicate
from generated_symbols.data.worldgen.feature.block_predicate.MatchingBlockTagPredicate import MatchingBlockTagPredicate
from generated_symbols.data.worldgen.feature.block_predicate.MatchingBlocksPredicate import MatchingBlocksPredicate
from generated_symbols.data.worldgen.feature.block_predicate.MatchingFluidsPredicate import MatchingFluidsPredicate
from generated_symbols.data.worldgen.feature.block_predicate.NotPredicate import NotPredicate
from generated_symbols.data.worldgen.feature.block_predicate.UnobstructedPredicate import UnobstructedPredicate
from generated_symbols.data.worldgen.feature.block_predicate.VolumeMatchPredicate import VolumeMatchPredicate
from generated_symbols.data.worldgen.feature.block_predicate.WouldSurvivePredicate import WouldSurvivePredicate


@dataclass(kw_only=True)
class BlockPredicateAllOf(CombiningPredicate):
    type: Literal['minecraft:all_of']


@dataclass(kw_only=True)
class BlockPredicateAnyOf(CombiningPredicate):
    type: Literal['minecraft:any_of']


@dataclass(kw_only=True)
class BlockPredicateHasSturdyFace(HasSturdyFacePredicate):
    type: Literal['minecraft:has_sturdy_face']


@dataclass(kw_only=True)
class BlockPredicateHeightRange(HeightRangePredicate):
    type: Literal['minecraft:height_range']


@dataclass(kw_only=True)
class BlockPredicateInsideWorldBounds(InsideWorldBoundsPredicate):
    type: Literal['minecraft:inside_world_bounds']


@dataclass(kw_only=True)
class BlockPredicateMatchingBiomes(MatchingBiomesPredicate):
    type: Literal['minecraft:matching_biomes']


@dataclass(kw_only=True)
class BlockPredicateMatchingBlockTag(MatchingBlockTagPredicate):
    type: Literal['minecraft:matching_block_tag']


@dataclass(kw_only=True)
class BlockPredicateMatchingBlocks(MatchingBlocksPredicate):
    type: Literal['minecraft:matching_blocks']


@dataclass(kw_only=True)
class BlockPredicateMatchingFluids(MatchingFluidsPredicate):
    type: Literal['minecraft:matching_fluids']


@dataclass(kw_only=True)
class BlockPredicateNot(NotPredicate):
    type: Literal['minecraft:not']


@dataclass(kw_only=True)
class BlockPredicateUnobstructed(UnobstructedPredicate):
    type: Literal['minecraft:unobstructed']


@dataclass(kw_only=True)
class BlockPredicateVolumeMatch(VolumeMatchPredicate):
    type: Literal['minecraft:volume_match']


@dataclass(kw_only=True)
class BlockPredicateWouldSurvive(WouldSurvivePredicate):
    type: Literal['minecraft:would_survive']


type BlockPredicate = BlockPredicateAllOf | BlockPredicateAnyOf | BlockPredicateHasSturdyFace | BlockPredicateHeightRange | BlockPredicateInsideWorldBounds | BlockPredicateMatchingBiomes | BlockPredicateMatchingBlockTag | BlockPredicateMatchingBlocks | BlockPredicateMatchingFluids | BlockPredicateNot | BlockPredicateUnobstructed | BlockPredicateVolumeMatch | BlockPredicateWouldSurvive


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::BlockPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block_predicate_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:block_predicate"
                }
            }
        ]
    }
}

