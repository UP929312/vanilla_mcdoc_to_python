"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/TrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.worldgen.feature.tree.BendingTrunkPlacer import BendingTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.CherryTrunkPlacer import CherryTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.PoplarTrunkPlacer import PoplarTrunkPlacer
from generated_symbols.data.worldgen.feature.tree.UpwardsBranchingTrunkPlacer import UpwardsBranchingTrunkPlacer
from pydantic import Field


class TrunkPlacerBendingTrunkPlacer(BendingTrunkPlacer):
    type: Literal['minecraft:bending_trunk_placer'] = 'minecraft:bending_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerCherryTrunkPlacer(CherryTrunkPlacer):
    type: Literal['minecraft:cherry_trunk_placer'] = 'minecraft:cherry_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerDarkOakTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:dark_oak_trunk_placer'] = 'minecraft:dark_oak_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerFancyTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:fancy_trunk_placer'] = 'minecraft:fancy_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerForkingTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:forking_trunk_placer'] = 'minecraft:forking_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerGiantTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:giant_trunk_placer'] = 'minecraft:giant_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerMegaJungleTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:mega_jungle_trunk_placer'] = 'minecraft:mega_jungle_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerPoplarTrunkPlacer(PoplarTrunkPlacer):
    type: Literal['minecraft:poplar_trunk_placer'] = 'minecraft:poplar_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerStraightTrunkPlacer(GeneratedModel):
    type: Literal['minecraft:straight_trunk_placer'] = 'minecraft:straight_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


class TrunkPlacerUpwardsBranchingTrunkPlacer(UpwardsBranchingTrunkPlacer):
    type: Literal['minecraft:upwards_branching_trunk_placer'] = 'minecraft:upwards_branching_trunk_placer'
    base_height: Annotated[int, Field(ge=0, le=32)]
    height_rand_a: Annotated[int, Field(ge=0, le=24)]
    height_rand_b: Annotated[int, Field(ge=0, le=24)]


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

