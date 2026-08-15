"""
Generated from symbols.json for ::java::data::worldgen::feature::ConfiguredFeature
Local link to file: generated_symbols/data/worldgen/feature/ConfiguredFeature.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CaveSurface import CaveSurface
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.BlockColumnLayer import BlockColumnLayer
    from generated_symbols.data.worldgen.feature.EndSpike import EndSpike
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef
    from generated_symbols.data.worldgen.feature.GeodeBlockSettings import GeodeBlockSettings
    from generated_symbols.data.worldgen.feature.GeodeCrackSettings import GeodeCrackSettings
    from generated_symbols.data.worldgen.feature.GeodeLayerSettings import GeodeLayerSettings
    from generated_symbols.data.worldgen.feature.GrowingPlantHeight import GrowingPlantHeight
    from generated_symbols.data.worldgen.feature.MultifaceBlock import MultifaceBlock
    from generated_symbols.data.worldgen.feature.TargetBlock import TargetBlock
    from generated_symbols.data.worldgen.feature.TemplateEntry import TemplateEntry
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.data.worldgen.feature.tree.FeatureSize import FeatureSize
    from generated_symbols.data.worldgen.feature.tree.FoliagePlacer import FoliagePlacer
    from generated_symbols.data.worldgen.feature.tree.RootPlacer import RootPlacer
    from generated_symbols.data.worldgen.feature.tree.TreeDecorator import TreeDecorator
    from generated_symbols.data.worldgen.feature.tree.TrunkPlacer import TrunkPlacer
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.WeightedList import WeightedList
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.direction.Direction import Direction
    from generated_symbols.util.direction.VerticalDirection import VerticalDirection
    from generated_symbols.util.fluid_state.FluidState import FluidState


@dataclass(kw_only=True)
class FeaturesStruct:
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureBamboo:
    type: Literal['minecraft:bamboo']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureBasaltColumns:
    type: Literal['minecraft:basalt_columns']
    block: BlockStateProvider
    can_replace: BlockPredicate
    continue_through: BlockPredicate
    cannot_place_on: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    column_reach: IntProvider[Annotated[int, 'Range | `0`-`3` | both inclusive']] | Annotated[int, 'Range | `0`-`3` | both inclusive']
    column_count: IntProvider[Annotated[int, 'Range | `1`-`150` | both inclusive']] | Annotated[int, 'Range | `1`-`150` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `1`-`10` | both inclusive']] | Annotated[int, 'Range | `1`-`10` | both inclusive']
    cluster_reach: IntProvider[Annotated[int, 'Range | `0`-`13` | both inclusive']] | Annotated[int, 'Range | `0`-`13` | both inclusive']  # The effective reach is limited by `height`.


@dataclass(kw_only=True)
class ConfiguredFeatureBlockBlob:
    type: Literal['minecraft:block_blob']
    state: BlockState
    can_place_on: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureBlockColumn:
    type: Literal['minecraft:block_column']
    direction: Direction
    allowed_placement: BlockPredicate
    prioritize_tip: bool
    layers: list[BlockColumnLayer]


@dataclass(kw_only=True)
class ConfiguredFeatureBlockPile:
    type: Literal['minecraft:block_pile']
    state_provider: BlockStateProvider


@dataclass(kw_only=True)
class ConfiguredFeatureCoralClaw:
    type: Literal['minecraft:coral_claw']
    feature: PlacedFeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureCoralTree:
    type: Literal['minecraft:coral_tree']
    feature: PlacedFeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureDecorated:
    type: Literal['minecraft:decorated']
    decorator: ConfiguredDecorator
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureDeltaFeature:
    type: Literal['minecraft:delta_feature']
    contents: BlockState
    rim: BlockState
    size: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    rim_size: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureDisk:
    type: Literal['minecraft:disk']
    state_provider: BlockStateProvider
    radius: IntProvider[Annotated[int, 'Range | `0`-`8` | both inclusive']] | Annotated[int, 'Range | `0`-`8` | both inclusive']
    half_height: Annotated[int, 'Range | `0`-`4` | both inclusive']
    target: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureDripstoneCluster:
    type: Literal['minecraft:dripstone_cluster']
    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, 'Range | `1`-`512` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    radius: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    max_stalagmite_stalactite_height_diff: Annotated[int, 'Range | `0`-`64` | both inclusive']  # Max height difference between the stalagmite and stalactite.
    height_deviation: Annotated[int, 'Range | `1`-`64` | both inclusive']
    speleothem_block_layer_thickness: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    density: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    wetness: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    chance_of_speleothem_at_max_distance_from_center: Annotated[float, 'Range | `0`-`1` | both inclusive']
    max_distance_from_edge_affecting_chance_of_speleothem: Annotated[int, 'Range | `1`-`64` | both inclusive']
    max_distance_from_center_affecting_height_bias: Annotated[int, 'Range | `1`-`64` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureEmeraldOre:
    type: Literal['minecraft:emerald_ore']
    state: BlockState
    target: BlockState


@dataclass(kw_only=True)
class ConfiguredFeatureEndGateway:
    type: Literal['minecraft:end_gateway']
    exact: bool
    exit: tuple[int, int, int] | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureEndPodium:
    type: Literal['minecraft:end_podium']
    active: bool | None = None  # Defaults to `false`.


@dataclass(kw_only=True)
class ConfiguredFeatureEndSpike:
    type: Literal['minecraft:end_spike']
    spikes: list[EndSpike]
    crystal_invulnerable: bool | None = None
    crystal_beam_target: tuple[int, int, int] | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureFallenTree:
    type: Literal['minecraft:fallen_tree']
    trunk_provider: BlockStateProvider
    log_length: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    stump_decorators: list[TreeDecorator]
    log_decorators: list[TreeDecorator]


@dataclass(kw_only=True)
class ConfiguredFeatureFillLayer:
    type: Literal['minecraft:fill_layer']
    state: BlockState
    height: Annotated[int, 'Range | `0`-`255` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureFlower:
    type: Literal['minecraft:flower']
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # How many attempts will be made to find a placement. Defaults to 128.
    xz_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 7.
    y_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 3.
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureForestRock:
    type: Literal['minecraft:forest_rock']
    state: BlockState


@dataclass(kw_only=True)
class ConfiguredFeatureFossil:
    type: Literal['minecraft:fossil']
    max_empty_corners_allowed: Annotated[int, 'Range | `0`-`7` | both inclusive']  # If more corners are exposed to air, feature placement is cancelled.
    fossil_structures: list[Annotated[str, IdSpec(registry='structure')]]
    overlay_structures: list[Annotated[str, IdSpec(registry='structure')]]
    fossil_processors: ProcessorListRef
    overlay_processors: ProcessorListRef


@dataclass(kw_only=True)
class ConfiguredFeatureGeode:
    type: Literal['minecraft:geode']
    blocks: GeodeBlockSettings
    layers: GeodeLayerSettings
    crack: GeodeCrackSettings
    noise_multiplier: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    use_potential_placements_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    use_alternate_layer0_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    placements_require_layer0_alternate: bool | None = None
    outer_wall_distance: IntProvider[Annotated[int, 'Range | `1`-`20` | both inclusive']] | Annotated[int, 'Range | `1`-`20` | both inclusive'] | None = None
    distribution_points: IntProvider[Annotated[int, 'Range | `1`-`20` | both inclusive']] | Annotated[int, 'Range | `1`-`20` | both inclusive'] | None = None
    point_offset: IntProvider[Annotated[int, 'Range | `1`-`10` | both inclusive']] | Annotated[int, 'Range | `1`-`10` | both inclusive'] | None = None
    min_gen_offset: int | None = None
    max_gen_offset: int | None = None
    invalid_blocks_threshold: int


@dataclass(kw_only=True)
class ConfiguredFeatureGlowLichen:
    type: Literal['minecraft:glow_lichen']
    block: MultifaceBlock
    search_range: Annotated[int, 'Range | `1`-`64` | both inclusive'] | None = None
    chance_of_spreading: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    can_place_on_floor: bool | None = None
    can_place_on_ceiling: bool | None = None
    can_place_on_wall: bool | None = None
    can_be_placed_on: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureGrowingPlant:
    type: Literal['minecraft:growing_plant']
    direction: Direction
    allow_water: bool
    height_distribution: list[GrowingPlantHeight]
    body_provider: BlockStateProvider
    head_provider: BlockStateProvider


@dataclass(kw_only=True)
class ConfiguredFeatureHugeBrownMushroom:
    type: Literal['minecraft:huge_brown_mushroom']
    cap_provider: BlockStateProvider
    stem_provider: BlockStateProvider
    foliage_radius: int
    can_place_on: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureHugeFungus:
    type: Literal['minecraft:huge_fungus']
    hat_state: BlockState
    decor_state: BlockState
    stem_state: BlockState
    valid_base_block: BlockState
    planted: bool | None = None
    replaceable_blocks: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureHugeRedMushroom:
    type: Literal['minecraft:huge_red_mushroom']
    cap_provider: BlockStateProvider
    stem_provider: BlockStateProvider
    foliage_radius: int
    can_place_on: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureIcePatch:
    type: Literal['minecraft:ice_patch']
    state_provider: BlockStateProvider
    radius: IntProvider[Annotated[int, 'Range | `0`-`8` | both inclusive']] | Annotated[int, 'Range | `0`-`8` | both inclusive']
    half_height: Annotated[int, 'Range | `0`-`4` | both inclusive']
    target: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureIceberg:
    type: Literal['minecraft:iceberg']
    state: BlockState


@dataclass(kw_only=True)
class ConfiguredFeatureLake:
    type: Literal['minecraft:lake']
    fluid: BlockStateProvider
    barrier: BlockStateProvider
    can_place_feature: BlockPredicate
    can_replace_with_air_or_fluid: BlockPredicate
    can_replace_with_barrier: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureLargeDripstone:
    type: Literal['minecraft:large_dripstone']
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, 'Range | `1`-`512` | both inclusive'] | None = None
    column_radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height_scale: FloatProvider[Annotated[float, 'Range | `0`-`20` | both inclusive']] | Annotated[float, 'Range | `0`-`20` | both inclusive']
    max_column_radius_to_cave_height_ratio: Annotated[float, 'Range | `0`-`1` | both inclusive']
    stalactite_bluntness: FloatProvider[Annotated[float, 'Range | `0.1`-`10` | both inclusive']] | Annotated[float, 'Range | `0.1`-`10` | both inclusive']
    stalagmite_bluntness: FloatProvider[Annotated[float, 'Range | `0.1`-`10` | both inclusive']] | Annotated[float, 'Range | `0.1`-`10` | both inclusive']
    wind_speed: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    min_radius_for_wind: Annotated[int, 'Range | `0`-`100` | both inclusive']
    min_bluntness_for_wind: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureMultifaceGrowth:
    type: Literal['minecraft:multiface_growth']
    block: MultifaceBlock
    search_range: Annotated[int, 'Range | `1`-`64` | both inclusive'] | None = None
    chance_of_spreading: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    can_place_on_floor: bool | None = None
    can_place_on_ceiling: bool | None = None
    can_place_on_wall: bool | None = None
    can_be_placed_on: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureNetherForestVegetation:
    type: Literal['minecraft:nether_forest_vegetation']
    state_provider: BlockStateProvider
    spread_width: Annotated[int, 'Range | Min `1` and above | inclusive']
    spread_height: Annotated[int, 'Range | Min `1` and above | inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureNetherrackReplaceBlobs:
    type: Literal['minecraft:netherrack_replace_blobs']
    state: BlockState
    target: BlockState
    radius: IntProvider[Annotated[int, 'Range | `0`-`12` | both inclusive']] | Annotated[int, 'Range | `0`-`12` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureNoBonemealFlower:
    type: Literal['minecraft:no_bonemeal_flower']
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # How many attempts will be made to find a placement. Defaults to 128.
    xz_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 7.
    y_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 3.
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureNoSurfaceOre:
    type: Literal['minecraft:no_surface_ore']
    targets: list[TargetBlock]
    size: Annotated[int, 'Range | `0`-`64` | both inclusive']
    discard_chance_on_air_exposure: Annotated[float, 'Range | `0`-`1` | both inclusive']  # Chance that feature placement will be discarded if the ore is exposed to air blocks.


@dataclass(kw_only=True)
class ConfiguredFeatureOre:
    type: Literal['minecraft:ore']
    targets: list[TargetBlock]
    size: Annotated[int, 'Range | `0`-`64` | both inclusive']
    discard_chance_on_air_exposure: Annotated[float, 'Range | `0`-`1` | both inclusive']  # Chance that feature placement will be discarded if the ore is exposed to air blocks.


@dataclass(kw_only=True)
class ConfiguredFeatureOverlay:
    type: Literal['minecraft:overlay']
    features: PlacedFeatureListRef  # The features to generate, in order.  All features are placed regardless of individual placement success.


@dataclass(kw_only=True)
class ConfiguredFeaturePointedDripstone:
    type: Literal['minecraft:pointed_dripstone']
    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    chance_of_taller_generation: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_directional_spread: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_spread_radius2: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_spread_radius3: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureProjectedRandomPatchySquare:
    type: Literal['minecraft:projected_random_patchy_square']
    block: BlockStateProvider
    project_through: BlockPredicate
    size: IntProvider[Annotated[int, 'Range | `1`-`16` | both inclusive']] | Annotated[int, 'Range | `1`-`16` | both inclusive']
    max_projection_height: Annotated[int, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomBooleanSelector:
    type: Literal['minecraft:random_boolean_selector']
    feature_false: FeatureRef
    feature_true: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureRandomNeighborSpread:
    type: Literal['minecraft:random_neighbor_spread']
    block: BlockStateProvider
    accepted_neighbors: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    can_replace: BlockPredicate
    attempts: IntProvider[Annotated[int, 'Range | `1`-`3000` | both inclusive']] | Annotated[int, 'Range | `1`-`3000` | both inclusive']
    xz_offset: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']
    y_offset: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureRandomPatch:
    type: Literal['minecraft:random_patch']
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # How many attempts will be made to find a placement. Defaults to 128.
    xz_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 7.
    y_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 3.
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureRandomSelector:
    type: Literal['minecraft:random_selector']
    features: list[FeaturesStruct]
    default: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureReplaceSingleBlock:
    type: Literal['minecraft:replace_single_block']
    targets: list[TargetBlock]


@dataclass(kw_only=True)
class ConfiguredFeatureRootSystem:
    type: Literal['minecraft:root_system']
    required_vertical_space_for_tree: Annotated[int, 'Range | `1`-`64` | both inclusive']
    level_test_distance: Annotated[int, 'Range | `0`-`16` | both inclusive']
    max_level_deviation: Annotated[int, 'Range | `0`-`64` | both inclusive']
    root_radius: Annotated[int, 'Range | `1`-`64` | both inclusive']
    root_placement_attempts: Annotated[int, 'Range | `1`-`256` | both inclusive']
    root_column_max_height: Annotated[int, 'Range | `1`-`4096` | both inclusive']
    hanging_root_radius: Annotated[int, 'Range | `1`-`64` | both inclusive']
    hanging_roots_vertical_span: Annotated[int, 'Range | `1`-`16` | both inclusive']
    hanging_root_placement_attempts: Annotated[int, 'Range | `0`-`256` | both inclusive']
    allowed_vertical_water_for_tree: Annotated[int, 'Range | `1`-`64` | both inclusive']
    root_replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    root_state_provider: BlockStateProvider
    hanging_root_state_provider: BlockStateProvider
    allowed_tree_position: BlockPredicate
    feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureScatteredOre:
    type: Literal['minecraft:scattered_ore']
    targets: list[TargetBlock]
    size: Annotated[int, 'Range | `0`-`64` | both inclusive']
    discard_chance_on_air_exposure: Annotated[float, 'Range | `0`-`1` | both inclusive']  # Chance that feature placement will be discarded if the ore is exposed to air blocks.


@dataclass(kw_only=True)
class ConfiguredFeatureSculkPatch:
    type: Literal['minecraft:sculk_patch']
    charge_count: Annotated[int, 'Range | `1`-`32` | both inclusive']
    amount_per_charge: Annotated[int, 'Range | `1`-`500` | both inclusive']
    spread_attempts: Annotated[int, 'Range | `1`-`64` | both inclusive']
    growth_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']
    spread_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureSeaPickle:
    type: Literal['minecraft:sea_pickle']
    count: IntProvider[Annotated[int, 'Range | `0`-`256` | both inclusive']] | Annotated[int, 'Range | `0`-`256` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureSeagrass:
    type: Literal['minecraft:seagrass']
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureSequence:
    type: Literal['minecraft:sequence']
    features: PlacedFeatureListRef  # The features to generate, in order.  If any feature in the list is not placed, the following features will also be skipped.


@dataclass(kw_only=True)
class ConfiguredFeatureSimpleBlock:
    type: Literal['minecraft:simple_block']
    to_place: BlockStateProvider
    schedule_tick: bool | None = None  # Whether to schedule a block update. Defaults to `false`.


@dataclass(kw_only=True)
class ConfiguredFeatureSimpleRandomSelector:
    type: Literal['minecraft:simple_random_selector']
    features: PlacedFeatureListRef


@dataclass(kw_only=True)
class ConfiguredFeatureSingleBlockPillar:
    type: Literal['minecraft:single_block_pillar']
    block: BlockStateProvider
    can_replace: BlockPredicate | None = None  # Defaults to "always true".
    direction: VerticalDirection
    chance_to_continue: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to 1.
    cap_feature: PlacedFeatureRef | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureSmallDripstone:
    type: Literal['minecraft:small_dripstone']
    max_placements: Annotated[int, 'Range | `0`-`100` | both inclusive'] | None = None
    empty_space_search_radius: Annotated[int, 'Range | `0`-`20` | both inclusive'] | None = None
    max_offset_from_origin: Annotated[int, 'Range | `0`-`20` | both inclusive'] | None = None
    chance_of_taller_dripstone: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureSpeleothem:
    type: Literal['minecraft:speleothem']
    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    chance_of_taller_generation: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_directional_spread: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_spread_radius2: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    chance_of_spread_radius3: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureSpeleothemCluster:
    type: Literal['minecraft:speleothem_cluster']
    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, 'Range | `1`-`512` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    radius: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    max_stalagmite_stalactite_height_diff: Annotated[int, 'Range | `0`-`64` | both inclusive']  # Max height difference between the stalagmite and stalactite.
    height_deviation: Annotated[int, 'Range | `1`-`64` | both inclusive']
    speleothem_block_layer_thickness: IntProvider[Annotated[int, 'Range | `0`-`128` | both inclusive']] | Annotated[int, 'Range | `0`-`128` | both inclusive']
    density: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    wetness: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    chance_of_speleothem_at_max_distance_from_center: Annotated[float, 'Range | `0`-`1` | both inclusive']
    max_distance_from_edge_affecting_chance_of_speleothem: Annotated[int, 'Range | `1`-`64` | both inclusive']
    max_distance_from_center_affecting_height_bias: Annotated[int, 'Range | `1`-`64` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureSpike:
    type: Literal['minecraft:spike']
    state: BlockState
    can_place_on: BlockPredicate
    can_replace: BlockPredicate


@dataclass(kw_only=True)
class ConfiguredFeatureSpringFeature:
    type: Literal['minecraft:spring_feature']
    state: FluidState
    rock_count: int
    hole_count: int
    requires_block_below: bool
    valid_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId


@dataclass(kw_only=True)
class ConfiguredFeatureSteppedColumnCluster:
    type: Literal['minecraft:stepped_column_cluster']
    block: BlockStateProvider
    can_replace: BlockPredicate
    continue_through: BlockPredicate
    cannot_place_on: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    column_reach: IntProvider[Annotated[int, 'Range | `0`-`3` | both inclusive']] | Annotated[int, 'Range | `0`-`3` | both inclusive']
    column_count: IntProvider[Annotated[int, 'Range | `1`-`150` | both inclusive']] | Annotated[int, 'Range | `1`-`150` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `1`-`10` | both inclusive']] | Annotated[int, 'Range | `1`-`10` | both inclusive']
    cluster_reach: IntProvider[Annotated[int, 'Range | `0`-`13` | both inclusive']] | Annotated[int, 'Range | `0`-`13` | both inclusive']  # The effective reach is limited by `height`.


@dataclass(kw_only=True)
class ConfiguredFeatureTemplate:
    type: Literal['minecraft:template']
    templates: WeightedList[TemplateEntry]
    processors: ProcessorListRef | None = None


@dataclass(kw_only=True)
class ConfiguredFeatureTree:
    type: Literal['minecraft:tree']
    ignore_vines: bool | None = None
    minimum_size: FeatureSize
    below_trunk_provider: BlockStateProvider
    trunk_provider: BlockStateProvider
    foliage_provider: BlockStateProvider
    root_placer: RootPlacer | None = None
    trunk_placer: TrunkPlacer
    foliage_placer: FoliagePlacer
    decorators: list[TreeDecorator]


@dataclass(kw_only=True)
class ConfiguredFeatureTwistingVines:
    type: Literal['minecraft:twisting_vines']
    spread_width: Annotated[int, 'Range | Min `1` and above | inclusive']
    spread_height: Annotated[int, 'Range | Min `1` and above | inclusive']
    max_height: Annotated[int, 'Range | Min `1` and above | inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureUnderwaterMagma:
    type: Literal['minecraft:underwater_magma']
    floor_search_range: Annotated[int, 'Range | `0`-`512` | both inclusive']
    placement_radius_around_floor: Annotated[int, 'Range | `0`-`64` | both inclusive']
    placement_probability_per_valid_position: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ConfiguredFeatureVegetationPatch:
    type: Literal['minecraft:vegetation_patch']
    surface: CaveSurface
    depth: IntProvider[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive']
    vertical_range: Annotated[int, 'Range | `1`-`256` | both inclusive']
    extra_bottom_block_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    extra_edge_column_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    vegetation_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    xz_radius: IntProvider[int] | int
    replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    ground_state: BlockStateProvider
    vegetation_feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureWaterloggedVegetationPatch:
    type: Literal['minecraft:waterlogged_vegetation_patch']
    surface: CaveSurface
    depth: IntProvider[Annotated[int, 'Range | `1`-`128` | both inclusive']] | Annotated[int, 'Range | `1`-`128` | both inclusive']
    vertical_range: Annotated[int, 'Range | `1`-`256` | both inclusive']
    extra_bottom_block_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    extra_edge_column_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    vegetation_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    xz_radius: IntProvider[int] | int
    replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    ground_state: BlockStateProvider
    vegetation_feature: FeatureRef


@dataclass(kw_only=True)
class ConfiguredFeatureWeightedRandomSelector:
    type: Literal['minecraft:weighted_random_selector']
    features: WeightedList[PlacedFeatureRef]


type ConfiguredFeature = ConfiguredFeatureBamboo | ConfiguredFeatureBasaltColumns | ConfiguredFeatureBlockBlob | ConfiguredFeatureBlockColumn | ConfiguredFeatureBlockPile | ConfiguredFeatureCoralClaw | ConfiguredFeatureCoralTree | ConfiguredFeatureDecorated | ConfiguredFeatureDeltaFeature | ConfiguredFeatureDisk | ConfiguredFeatureDripstoneCluster | ConfiguredFeatureEmeraldOre | ConfiguredFeatureEndGateway | ConfiguredFeatureEndPodium | ConfiguredFeatureEndSpike | ConfiguredFeatureFallenTree | ConfiguredFeatureFillLayer | ConfiguredFeatureFlower | ConfiguredFeatureForestRock | ConfiguredFeatureFossil | ConfiguredFeatureGeode | ConfiguredFeatureGlowLichen | ConfiguredFeatureGrowingPlant | ConfiguredFeatureHugeBrownMushroom | ConfiguredFeatureHugeFungus | ConfiguredFeatureHugeRedMushroom | ConfiguredFeatureIcePatch | ConfiguredFeatureIceberg | ConfiguredFeatureLake | ConfiguredFeatureLargeDripstone | ConfiguredFeatureMultifaceGrowth | ConfiguredFeatureNetherForestVegetation | ConfiguredFeatureNetherrackReplaceBlobs | ConfiguredFeatureNoBonemealFlower | ConfiguredFeatureNoSurfaceOre | ConfiguredFeatureOre | ConfiguredFeatureOverlay | ConfiguredFeaturePointedDripstone | ConfiguredFeatureProjectedRandomPatchySquare | ConfiguredFeatureRandomBooleanSelector | ConfiguredFeatureRandomNeighborSpread | ConfiguredFeatureRandomPatch | ConfiguredFeatureRandomSelector | ConfiguredFeatureReplaceSingleBlock | ConfiguredFeatureRootSystem | ConfiguredFeatureScatteredOre | ConfiguredFeatureSculkPatch | ConfiguredFeatureSeaPickle | ConfiguredFeatureSeagrass | ConfiguredFeatureSequence | ConfiguredFeatureSimpleBlock | ConfiguredFeatureSimpleRandomSelector | ConfiguredFeatureSingleBlockPillar | ConfiguredFeatureSmallDripstone | ConfiguredFeatureSpeleothem | ConfiguredFeatureSpeleothemCluster | ConfiguredFeatureSpike | ConfiguredFeatureSpringFeature | ConfiguredFeatureSteppedColumnCluster | ConfiguredFeatureTemplate | ConfiguredFeatureTree | ConfiguredFeatureTwistingVines | ConfiguredFeatureUnderwaterMagma | ConfiguredFeatureVegetationPatch | ConfiguredFeatureWaterloggedVegetationPatch | ConfiguredFeatureWeightedRandomSelector


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ConfiguredFeature": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/feature"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/feature_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "config",
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
                    "registry": "minecraft:feature_config"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
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
                    "registry": "minecraft:feature_config"
                }
            }
        ]
    }
}

