"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacementModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/PlacementModifier.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.feature.placement.BlockPredicateFilter import BlockPredicateFilter
from generated_symbols.data.worldgen.feature.placement.CountModifier import CountModifier
from generated_symbols.data.worldgen.feature.placement.CountOnEveryLayerModifier import CountOnEveryLayerModifier
from generated_symbols.data.worldgen.feature.placement.CuboidModifier import CuboidModifier
from generated_symbols.data.worldgen.feature.placement.EnvironmentScanModifier import EnvironmentScanModifier
from generated_symbols.data.worldgen.feature.placement.FixedPlacementModifier import FixedPlacementModifier
from generated_symbols.data.worldgen.feature.placement.HeightRangeModifier import HeightRangeModifier
from generated_symbols.data.worldgen.feature.placement.HeightmapModifier import HeightmapModifier
from generated_symbols.data.worldgen.feature.placement.NoiseBasedCountModifier import NoiseBasedCountModifier
from generated_symbols.data.worldgen.feature.placement.NoiseThresholdCountModifier import NoiseThresholdCountModifier
from generated_symbols.data.worldgen.feature.placement.OffsetModifier import OffsetModifier
from generated_symbols.data.worldgen.feature.placement.RandomChanceModifier import RandomChanceModifier
from generated_symbols.data.worldgen.feature.placement.RandomlySelectedModifier import RandomlySelectedModifier
from generated_symbols.data.worldgen.feature.placement.RarityFilter import RarityFilter
from generated_symbols.data.worldgen.feature.placement.SurfaceRelativeThresholdFilter import SurfaceRelativeThresholdFilter
from generated_symbols.data.worldgen.feature.placement.SurfaceWaterDepthFilter import SurfaceWaterDepthFilter


@dataclass(kw_only=True)
class PlacementModifierBlockPredicateFilter(BlockPredicateFilter):
    type: Literal['minecraft:block_predicate_filter']


@dataclass(kw_only=True)
class PlacementModifierCount(CountModifier):
    type: Literal['minecraft:count']


@dataclass(kw_only=True)
class PlacementModifierCountOnEveryLayer(CountOnEveryLayerModifier):
    type: Literal['minecraft:count_on_every_layer']


@dataclass(kw_only=True)
class PlacementModifierCuboid(CuboidModifier):
    type: Literal['minecraft:cuboid']


@dataclass(kw_only=True)
class PlacementModifierEnvironmentScan(EnvironmentScanModifier):
    type: Literal['minecraft:environment_scan']


@dataclass(kw_only=True)
class PlacementModifierFixedPlacement(FixedPlacementModifier):
    type: Literal['minecraft:fixed_placement']


@dataclass(kw_only=True)
class PlacementModifierHeightRange(HeightRangeModifier):
    type: Literal['minecraft:height_range']


@dataclass(kw_only=True)
class PlacementModifierHeightmap(HeightmapModifier):
    type: Literal['minecraft:heightmap']


@dataclass(kw_only=True)
class PlacementModifierNoiseBasedCount(NoiseBasedCountModifier):
    type: Literal['minecraft:noise_based_count']


@dataclass(kw_only=True)
class PlacementModifierNoiseThresholdCount(NoiseThresholdCountModifier):
    type: Literal['minecraft:noise_threshold_count']


@dataclass(kw_only=True)
class PlacementModifierOffset(OffsetModifier):
    type: Literal['minecraft:offset']


@dataclass(kw_only=True)
class PlacementModifierRandomChance(RandomChanceModifier):
    type: Literal['minecraft:random_chance']


@dataclass(kw_only=True)
class PlacementModifierRandomlySelected(RandomlySelectedModifier):
    type: Literal['minecraft:randomly_selected']


@dataclass(kw_only=True)
class PlacementModifierRarityFilter(RarityFilter):
    type: Literal['minecraft:rarity_filter']


@dataclass(kw_only=True)
class PlacementModifierSurfaceRelativeThresholdFilter(SurfaceRelativeThresholdFilter):
    type: Literal['minecraft:surface_relative_threshold_filter']


@dataclass(kw_only=True)
class PlacementModifierSurfaceWaterDepthFilter(SurfaceWaterDepthFilter):
    type: Literal['minecraft:surface_water_depth_filter']


type PlacementModifier = PlacementModifierBlockPredicateFilter | PlacementModifierCount | PlacementModifierCountOnEveryLayer | PlacementModifierCuboid | PlacementModifierEnvironmentScan | PlacementModifierFixedPlacement | PlacementModifierHeightRange | PlacementModifierHeightmap | PlacementModifierNoiseBasedCount | PlacementModifierNoiseThresholdCount | PlacementModifierOffset | PlacementModifierRandomChance | PlacementModifierRandomlySelected | PlacementModifierRarityFilter | PlacementModifierSurfaceRelativeThresholdFilter | PlacementModifierSurfaceWaterDepthFilter


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::PlacementModifier": {
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
                                    "value": "worldgen/placement_modifier_type"
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
                    "registry": "minecraft:placement_modifier"
                }
            }
        ]
    }
}

