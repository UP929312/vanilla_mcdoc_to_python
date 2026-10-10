"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/FoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from generated_symbols.data.worldgen.feature.tree.CherryFoliagePlacer import CherryFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.HeightFoliagePlacer import HeightFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.MegaPineFoliagePlacer import MegaPineFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.PineFoliagePlacer import PineFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.PoplarFoliagePlacer import PoplarFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.RandomSpreadFoliagePlacer import RandomSpreadFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.SprucePineFoliagePlacer import SprucePineFoliagePlacer

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class FoliagePlacerBlobFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:blob_foliage_placer', 'blob_foliage_placer'] = 'minecraft:blob_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerBushFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:bush_foliage_placer', 'bush_foliage_placer'] = 'minecraft:bush_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerCherryFoliagePlacer(CherryFoliagePlacer):
    type: Literal['minecraft:cherry_foliage_placer', 'cherry_foliage_placer'] = 'minecraft:cherry_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerFancyFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:fancy_foliage_placer', 'fancy_foliage_placer'] = 'minecraft:fancy_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerJungleFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:jungle_foliage_placer', 'jungle_foliage_placer'] = 'minecraft:jungle_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerMegaPineFoliagePlacer(MegaPineFoliagePlacer):
    type: Literal['minecraft:mega_pine_foliage_placer', 'mega_pine_foliage_placer'] = 'minecraft:mega_pine_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerPineFoliagePlacer(PineFoliagePlacer):
    type: Literal['minecraft:pine_foliage_placer', 'pine_foliage_placer'] = 'minecraft:pine_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerPoplarFoliagePlacer(PoplarFoliagePlacer):
    type: Literal['minecraft:poplar_foliage_placer', 'poplar_foliage_placer'] = 'minecraft:poplar_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerRandomSpreadFoliagePlacer(RandomSpreadFoliagePlacer):
    type: Literal['minecraft:random_spread_foliage_placer', 'random_spread_foliage_placer'] = 'minecraft:random_spread_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


class FoliagePlacerSpruceFoliagePlacer(SprucePineFoliagePlacer):
    type: Literal['minecraft:spruce_foliage_placer', 'spruce_foliage_placer'] = 'minecraft:spruce_foliage_placer'
    radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    offset: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]


type FoliagePlacer = Annotated[
    FoliagePlacerBlobFoliagePlacer | FoliagePlacerBushFoliagePlacer | FoliagePlacerCherryFoliagePlacer | FoliagePlacerFancyFoliagePlacer | FoliagePlacerJungleFoliagePlacer | FoliagePlacerMegaPineFoliagePlacer | FoliagePlacerPineFoliagePlacer | FoliagePlacerPoplarFoliagePlacer | FoliagePlacerRandomSpreadFoliagePlacer | FoliagePlacerSpruceFoliagePlacer,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::FoliagePlacer": {
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
                                    "value": "worldgen/foliage_placer_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "radius",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::UniformInt"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 8
                                    }
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 8
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::IntProvider"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 16
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
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
                "key": "offset",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::UniformInt"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 8
                                    }
                                },
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 8
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::IntProvider"
                            },
                            "typeArgs": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 16
                                    }
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
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
                    "registry": "minecraft:foliage_placer"
                }
            }
        ]
    }
}

