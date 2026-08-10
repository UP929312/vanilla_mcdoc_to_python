"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/FoliagePlacer.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class FoliagePlacerBlobFoliagePlacer:
    type: Literal['minecraft:blob_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerBushFoliagePlacer:
    type: Literal['minecraft:bush_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerCherryFoliagePlacer:
    type: Literal['minecraft:cherry_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `4`-`16` | both inclusive']] | Annotated[int, 'Range | `4`-`16` | both inclusive']
    wide_bottom_layer_hole_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    corner_hole_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    hanging_leaves_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    hanging_leaves_extension_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerFancyFoliagePlacer:
    type: Literal['minecraft:fancy_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerJungleFoliagePlacer:
    type: Literal['minecraft:jungle_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: Annotated[int, 'Range | `0`-`16` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerMegaPineFoliagePlacer:
    type: Literal['minecraft:mega_pine_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    crown_height: IntProvider[Annotated[int, 'Range | `0`-`24` | both inclusive']] | Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerPineFoliagePlacer:
    type: Literal['minecraft:pine_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `0`-`24` | both inclusive']] | Annotated[int, 'Range | `0`-`24` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerPoplarFoliagePlacer:
    type: Literal['minecraft:poplar_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height: IntProvider[Annotated[int, 'Range | `5`-`16` | both inclusive']] | Annotated[int, 'Range | `5`-`16` | both inclusive']
    side_hole_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerRandomSpreadFoliagePlacer:
    type: Literal['minecraft:random_spread_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    foliage_height: IntProvider[Annotated[int, 'Range | `1`-`512` | both inclusive']] | Annotated[int, 'Range | `1`-`512` | both inclusive']
    leaf_placement_attempts: Annotated[int, 'Range | `0`-`256` | both inclusive']


@dataclass(kw_only=True)
class FoliagePlacerSpruceFoliagePlacer:
    type: Literal['minecraft:spruce_foliage_placer']
    radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    offset: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    trunk_height: IntProvider[Annotated[int, 'Range | `0`-`24` | both inclusive']] | Annotated[int, 'Range | `0`-`24` | both inclusive']


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

