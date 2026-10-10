"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacementModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/PlacementModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

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


class PlacementModifierBlockPredicateFilter(BlockPredicateFilter):
    type: Literal['minecraft:block_predicate_filter', 'block_predicate_filter'] = 'minecraft:block_predicate_filter'


class PlacementModifierCount(CountModifier):
    type: Literal['minecraft:count', 'count'] = 'minecraft:count'


class PlacementModifierCountOnEveryLayer(CountOnEveryLayerModifier):
    type: Literal['minecraft:count_on_every_layer', 'count_on_every_layer'] = 'minecraft:count_on_every_layer'


class PlacementModifierCuboid(CuboidModifier):
    type: Literal['minecraft:cuboid', 'cuboid'] = 'minecraft:cuboid'


class PlacementModifierEnvironmentScan(EnvironmentScanModifier):
    type: Literal['minecraft:environment_scan', 'environment_scan'] = 'minecraft:environment_scan'


class PlacementModifierFixedPlacement(FixedPlacementModifier):
    type: Literal['minecraft:fixed_placement', 'fixed_placement'] = 'minecraft:fixed_placement'


class PlacementModifierHeightRange(HeightRangeModifier):
    type: Literal['minecraft:height_range', 'height_range'] = 'minecraft:height_range'


class PlacementModifierHeightmap(HeightmapModifier):
    type: Literal['minecraft:heightmap', 'heightmap'] = 'minecraft:heightmap'


class PlacementModifierNoiseBasedCount(NoiseBasedCountModifier):
    type: Literal['minecraft:noise_based_count', 'noise_based_count'] = 'minecraft:noise_based_count'


class PlacementModifierNoiseThresholdCount(NoiseThresholdCountModifier):
    type: Literal['minecraft:noise_threshold_count', 'noise_threshold_count'] = 'minecraft:noise_threshold_count'


class PlacementModifierOffset(OffsetModifier):
    type: Literal['minecraft:offset', 'offset'] = 'minecraft:offset'


class PlacementModifierRandomChance(RandomChanceModifier):
    type: Literal['minecraft:random_chance', 'random_chance'] = 'minecraft:random_chance'


class PlacementModifierRandomlySelected(RandomlySelectedModifier):
    type: Literal['minecraft:randomly_selected', 'randomly_selected'] = 'minecraft:randomly_selected'


class PlacementModifierRarityFilter(RarityFilter):
    type: Literal['minecraft:rarity_filter', 'rarity_filter'] = 'minecraft:rarity_filter'


class PlacementModifierSurfaceRelativeThresholdFilter(SurfaceRelativeThresholdFilter):
    type: Literal['minecraft:surface_relative_threshold_filter', 'surface_relative_threshold_filter'] = 'minecraft:surface_relative_threshold_filter'


class PlacementModifierSurfaceWaterDepthFilter(SurfaceWaterDepthFilter):
    type: Literal['minecraft:surface_water_depth_filter', 'surface_water_depth_filter'] = 'minecraft:surface_water_depth_filter'


type PlacementModifier = Annotated[
    PlacementModifierBlockPredicateFilter | PlacementModifierCount | PlacementModifierCountOnEveryLayer | PlacementModifierCuboid | PlacementModifierEnvironmentScan | PlacementModifierFixedPlacement | PlacementModifierHeightRange | PlacementModifierHeightmap | PlacementModifierNoiseBasedCount | PlacementModifierNoiseThresholdCount | PlacementModifierOffset | PlacementModifierRandomChance | PlacementModifierRandomlySelected | PlacementModifierRarityFilter | PlacementModifierSurfaceRelativeThresholdFilter | PlacementModifierSurfaceWaterDepthFilter,
    Field(discriminator='type'),
]


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

