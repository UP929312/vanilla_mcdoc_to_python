"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/TrunkPlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal

from generated_symbols.data.worldgen.feature.tree.BendingTrunkPlacer import BendingTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.CherryTrunkPlacer import CherryTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.PoplarTrunkPlacer import PoplarTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.UpwardsBranchingTrunkPlacer import UpwardsBranchingTrunkPlacer


@dataclass(kw_only=True)
class TrunkPlacerBendingTrunkPlacer(BendingTrunkPlacer):
    type: Literal['minecraft:bending_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerCherryTrunkPlacer(CherryTrunkPlacer):
    type: Literal['minecraft:cherry_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


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
class TrunkPlacerPoplarTrunkPlacer(PoplarTrunkPlacer):
    type: Literal['minecraft:poplar_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerStraightTrunkPlacer:
    type: Literal['minecraft:straight_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class TrunkPlacerUpwardsBranchingTrunkPlacer(UpwardsBranchingTrunkPlacer):
    type: Literal['minecraft:upwards_branching_trunk_placer']
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


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

