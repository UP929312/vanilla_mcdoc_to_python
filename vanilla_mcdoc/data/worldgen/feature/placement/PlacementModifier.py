"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacementModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/PlacementModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.feature.placement.BlockPredicateFilter import BlockPredicateFilter
from vanilla_mcdoc.data.worldgen.feature.placement.CountModifier import CountModifier
from vanilla_mcdoc.data.worldgen.feature.placement.CountOnEveryLayerModifier import CountOnEveryLayerModifier
from vanilla_mcdoc.data.worldgen.feature.placement.CuboidModifier import CuboidModifier
from vanilla_mcdoc.data.worldgen.feature.placement.EnvironmentScanModifier import EnvironmentScanModifier
from vanilla_mcdoc.data.worldgen.feature.placement.FixedPlacementModifier import FixedPlacementModifier
from vanilla_mcdoc.data.worldgen.feature.placement.HeightRangeModifier import HeightRangeModifier
from vanilla_mcdoc.data.worldgen.feature.placement.HeightmapModifier import HeightmapModifier
from vanilla_mcdoc.data.worldgen.feature.placement.NoiseBasedCountModifier import NoiseBasedCountModifier
from vanilla_mcdoc.data.worldgen.feature.placement.NoiseThresholdCountModifier import NoiseThresholdCountModifier
from vanilla_mcdoc.data.worldgen.feature.placement.OffsetModifier import OffsetModifier
from vanilla_mcdoc.data.worldgen.feature.placement.RandomChanceModifier import RandomChanceModifier
from vanilla_mcdoc.data.worldgen.feature.placement.RandomlySelectedModifier import RandomlySelectedModifier
from vanilla_mcdoc.data.worldgen.feature.placement.RarityFilter import RarityFilter
from vanilla_mcdoc.data.worldgen.feature.placement.SurfaceRelativeThresholdFilter import SurfaceRelativeThresholdFilter
from vanilla_mcdoc.data.worldgen.feature.placement.SurfaceWaterDepthFilter import SurfaceWaterDepthFilter


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


class PlacementModifierBiome(GeneratedModel):
    type: Literal['minecraft:biome', 'biome'] = 'minecraft:biome'


class PlacementModifierInSquare(GeneratedModel):
    type: Literal['minecraft:in_square', 'in_square'] = 'minecraft:in_square'


type PlacementModifier = Annotated[
    Annotated[PlacementModifierBlockPredicateFilter, Tag('minecraft:block_predicate_filter')]
    | Annotated[PlacementModifierCount, Tag('minecraft:count')]
    | Annotated[PlacementModifierCountOnEveryLayer, Tag('minecraft:count_on_every_layer')]
    | Annotated[PlacementModifierCuboid, Tag('minecraft:cuboid')]
    | Annotated[PlacementModifierEnvironmentScan, Tag('minecraft:environment_scan')]
    | Annotated[PlacementModifierFixedPlacement, Tag('minecraft:fixed_placement')]
    | Annotated[PlacementModifierHeightRange, Tag('minecraft:height_range')]
    | Annotated[PlacementModifierHeightmap, Tag('minecraft:heightmap')]
    | Annotated[PlacementModifierNoiseBasedCount, Tag('minecraft:noise_based_count')]
    | Annotated[PlacementModifierNoiseThresholdCount, Tag('minecraft:noise_threshold_count')]
    | Annotated[PlacementModifierOffset, Tag('minecraft:offset')]
    | Annotated[PlacementModifierRandomChance, Tag('minecraft:random_chance')]
    | Annotated[PlacementModifierRandomlySelected, Tag('minecraft:randomly_selected')]
    | Annotated[PlacementModifierRarityFilter, Tag('minecraft:rarity_filter')]
    | Annotated[PlacementModifierSurfaceRelativeThresholdFilter, Tag('minecraft:surface_relative_threshold_filter')]
    | Annotated[PlacementModifierSurfaceWaterDepthFilter, Tag('minecraft:surface_water_depth_filter')]
    | Annotated[PlacementModifierBiome, Tag('minecraft:biome')]
    | Annotated[PlacementModifierInSquare, Tag('minecraft:in_square')],
    Discriminator(tag_of('type')),
]
