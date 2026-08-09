# Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacementModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CarveStep import CarveStep
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.direction.VerticalDirection import VerticalDirection


@dataclass(kw_only=True)
class PlacementModifierBlockPredicateFilter:
    type: Literal['minecraft:block_predicate_filter']
    predicate: BlockPredicate


@dataclass(kw_only=True)
class PlacementModifierCarvingMask:
    type: Literal['minecraft:carving_mask']
    step: CarveStep


@dataclass(kw_only=True)
class PlacementModifierCount:
    type: Literal['minecraft:count']
    count: IntProvider[Annotated[int, 'Range | `0`-`4096` | both inclusive']] | Annotated[int, 'Range | `0`-`4096` | both inclusive']


@dataclass(kw_only=True)
class PlacementModifierCountOnEveryLayer:
    type: Literal['minecraft:count_on_every_layer']
    count: IntProvider[Annotated[int, 'Range | `0`-`256` | both inclusive']] | Annotated[int, 'Range | `0`-`256` | both inclusive']


@dataclass(kw_only=True)
class PlacementModifierCuboid:
    type: Literal['minecraft:cuboid']
    xz_size: IntProvider[Annotated[int, 'Range | `1`-`16` | both inclusive']] | Annotated[int, 'Range | `1`-`16` | both inclusive']
    y_size: IntProvider[Annotated[int, 'Range | `1`-`16` | both inclusive']] | Annotated[int, 'Range | `1`-`16` | both inclusive']
    include_interior: bool | None = None  # Defaults to `true`.
    include_edges: bool | None = None  # Defaults to `true`.


@dataclass(kw_only=True)
class PlacementModifierEnvironmentScan:
    type: Literal['minecraft:environment_scan']
    direction_of_search: VerticalDirection
    max_steps: Annotated[int, 'Range | `1`-`32` | both inclusive']
    target_condition: BlockPredicate
    allowed_search_condition: BlockPredicate | None = None


@dataclass(kw_only=True)
class PlacementModifierFixedPlacement:
    type: Literal['minecraft:fixed_placement']
    positions: list[tuple[int, int, int]]  # Fixed list of block positions to place the feature at.


@dataclass(kw_only=True)
class PlacementModifierHeightRange:
    type: Literal['minecraft:height_range']
    height: HeightProvider


@dataclass(kw_only=True)
class PlacementModifierHeightmap:
    type: Literal['minecraft:heightmap']
    heightmap: HeightmapType


@dataclass(kw_only=True)
class PlacementModifierNoiseBasedCount:
    type: Literal['minecraft:noise_based_count']
    noise_to_count_ratio: int
    noise_factor: float
    noise_offset: float | None = None


@dataclass(kw_only=True)
class PlacementModifierNoiseThresholdCount:
    type: Literal['minecraft:noise_threshold_count']
    noise_level: float
    below_noise: int
    above_noise: int


@dataclass(kw_only=True)
class PlacementModifierOffset:
    type: Literal['minecraft:offset']
    x: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']
    y: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']
    z: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


@dataclass(kw_only=True)
class PlacementModifierRandomChance:
    type: Literal['minecraft:random_chance']
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class PlacementModifierRandomOffset:
    type: Literal['minecraft:random_offset']
    xz_spread: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']
    y_spread: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


@dataclass(kw_only=True)
class PlacementModifierRarityFilter:
    type: Literal['minecraft:rarity_filter']
    chance: Annotated[int, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class PlacementModifierSurfaceRelativeThresholdFilter:
    type: Literal['minecraft:surface_relative_threshold_filter']
    heightmap: HeightmapType
    min_inclusive: int | None = None
    max_inclusive: int | None = None


@dataclass(kw_only=True)
class PlacementModifierSurfaceWaterDepthFilter:
    type: Literal['minecraft:surface_water_depth_filter']
    max_water_depth: int


type PlacementModifier = PlacementModifierBlockPredicateFilter | PlacementModifierCarvingMask | PlacementModifierCount | PlacementModifierCountOnEveryLayer | PlacementModifierCuboid | PlacementModifierEnvironmentScan | PlacementModifierFixedPlacement | PlacementModifierHeightRange | PlacementModifierHeightmap | PlacementModifierNoiseBasedCount | PlacementModifierNoiseThresholdCount | PlacementModifierOffset | PlacementModifierRandomChance | PlacementModifierRandomOffset | PlacementModifierRarityFilter | PlacementModifierSurfaceRelativeThresholdFilter | PlacementModifierSurfaceWaterDepthFilter


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

