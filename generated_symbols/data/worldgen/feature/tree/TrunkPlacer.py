"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/TrunkPlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.UniformIntProvider import UniformIntProvider
    from generated_symbols.registry.KnownBlockId import KnownBlockId


@dataclass(kw_only=True)
class TrunkPlacerBendingTrunkPlacer:
    type: Literal['minecraft:bending_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']
    bend_length: IntProvider[Annotated[int, 'Range | `1`-`64` | both inclusive']] | Annotated[int, 'Range | `1`-`64` | both inclusive']
    min_height_for_leaves: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class TrunkPlacerCherryTrunkPlacer:
    type: Literal['minecraft:cherry_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']
    branch_count: IntProvider[Annotated[int, 'Range | `1`-`3` | both inclusive']] | Annotated[int, 'Range | `1`-`3` | both inclusive']
    branch_horizontal_length: IntProvider[Annotated[int, 'Range | `2`-`16` | both inclusive']] | Annotated[int, 'Range | `2`-`16` | both inclusive']
    branch_start_offset_from_top: UniformIntProvider[Annotated[int, 'Range | `-16`-`0` | both inclusive']] | Annotated[int, 'Range | `-16`-`0` | both inclusive']
    branch_end_offset_from_top: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerDarkOakTrunkPlacer:
    type: Literal['minecraft:dark_oak_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerFancyTrunkPlacer:
    type: Literal['minecraft:fancy_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerForkingTrunkPlacer:
    type: Literal['minecraft:forking_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerGiantTrunkPlacer:
    type: Literal['minecraft:giant_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerMegaJungleTrunkPlacer:
    type: Literal['minecraft:mega_jungle_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerPoplarTrunkPlacer:
    type: Literal['minecraft:poplar_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']
    trunk_height_above_branches: IntProvider[Annotated[int, 'Range | `0`-`8` | both inclusive']] | Annotated[int, 'Range | `0`-`8` | both inclusive']
    branch_amount: IntProvider[Annotated[int, 'Range | `1`-`4` | both inclusive']] | Annotated[int, 'Range | `1`-`4` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerStraightTrunkPlacer:
    type: Literal['minecraft:straight_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerUpwardsBranchingTrunkPlacer:
    type: Literal['minecraft:upwards_branching_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']
    extra_branch_steps: IntProvider[Annotated[int, 'Range | Min `1` and above | inclusive']] | Annotated[int, 'Range | Min `1` and above | inclusive']
    extra_branch_length: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']
    place_branch_per_log_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    can_grow_through: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId


type TrunkPlacer = TrunkPlacerBendingTrunkPlacer | TrunkPlacerCherryTrunkPlacer | TrunkPlacerDarkOakTrunkPlacer | TrunkPlacerFancyTrunkPlacer | TrunkPlacerForkingTrunkPlacer | TrunkPlacerGiantTrunkPlacer | TrunkPlacerMegaJungleTrunkPlacer | TrunkPlacerPoplarTrunkPlacer | TrunkPlacerStraightTrunkPlacer | TrunkPlacerUpwardsBranchingTrunkPlacer


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TrunkPlacer": {
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
                                    "value": "worldgen/trunk_placer_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "base_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 32
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height_rand_a",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 24
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height_rand_b",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 24
                    }
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
                    "registry": "minecraft:trunk_placer"
                }
            }
        ]
    }
}

