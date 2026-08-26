"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/FoliagePlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.feature.tree.CherryFoliagePlacer import CherryFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.HeightFoliagePlacer import HeightFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.MegaPineFoliagePlacer import MegaPineFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.PineFoliagePlacer import PineFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.PoplarFoliagePlacer import PoplarFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.RandomSpreadFoliagePlacer import RandomSpreadFoliagePlacer
from generated_symbols.data.worldgen.feature.tree.SprucePineFoliagePlacer import SprucePineFoliagePlacer

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class FoliagePlacerBlobFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:blob_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerBushFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:bush_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerCherryFoliagePlacer(CherryFoliagePlacer):
    type: Literal['minecraft:cherry_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerFancyFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:fancy_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerJungleFoliagePlacer(HeightFoliagePlacer):
    type: Literal['minecraft:jungle_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerMegaPineFoliagePlacer(MegaPineFoliagePlacer):
    type: Literal['minecraft:mega_pine_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerPineFoliagePlacer(PineFoliagePlacer):
    type: Literal['minecraft:pine_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerPoplarFoliagePlacer(PoplarFoliagePlacer):
    type: Literal['minecraft:poplar_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerRandomSpreadFoliagePlacer(RandomSpreadFoliagePlacer):
    type: Literal['minecraft:random_spread_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerSpruceFoliagePlacer(SprucePineFoliagePlacer):
    type: Literal['minecraft:spruce_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']


type FoliagePlacer = FoliagePlacerBlobFoliagePlacer | FoliagePlacerBushFoliagePlacer | FoliagePlacerCherryFoliagePlacer | FoliagePlacerFancyFoliagePlacer | FoliagePlacerJungleFoliagePlacer | FoliagePlacerMegaPineFoliagePlacer | FoliagePlacerPineFoliagePlacer | FoliagePlacerPoplarFoliagePlacer | FoliagePlacerRandomSpreadFoliagePlacer | FoliagePlacerSpruceFoliagePlacer


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

