# Generated from symbols.json for ::java::data::worldgen::feature::LargeDripstoneConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class LargeDripstoneConfig:
    replaceable_blocks: list[str] | str
    column_radius: IntProvider[Annotated[int, 'Range | `0`-`16` | both inclusive']] | Annotated[int, 'Range | `0`-`16` | both inclusive']
    height_scale: FloatProvider[Annotated[float, 'Range | `0`-`20` | both inclusive']] | Annotated[float, 'Range | `0`-`20` | both inclusive']
    max_column_radius_to_cave_height_ratio: Annotated[float, 'Range | `0`-`1` | both inclusive']
    stalactite_bluntness: FloatProvider[Annotated[float, 'Range | `0.1`-`10` | both inclusive']] | Annotated[float, 'Range | `0.1`-`10` | both inclusive']
    stalagmite_bluntness: FloatProvider[Annotated[float, 'Range | `0.1`-`10` | both inclusive']] | Annotated[float, 'Range | `0.1`-`10` | both inclusive']
    wind_speed: FloatProvider[Annotated[float, 'Range | `0`-`2` | both inclusive']] | Annotated[float, 'Range | `0`-`2` | both inclusive']
    min_radius_for_wind: Annotated[int, 'Range | `0`-`100` | both inclusive']
    min_bluntness_for_wind: Annotated[float, 'Range | `0`-`1` | both inclusive']
    floor_to_ceiling_search_range: Annotated[int, 'Range | `1`-`512` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::LargeDripstoneConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "key": "replaceable_blocks",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "block"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
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
                "key": "floor_to_ceiling_search_range",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 512
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "column_radius",
                "type": {
                    "kind": "union",
                    "members": [
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
                                        "max": 60
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
                                            "value": "26.2"
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
                                            "value": "26.2"
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
                "key": "height_scale",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 20
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "max_column_radius_to_cave_height_ratio",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "stalactite_bluntness",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0.1,
                                "max": 10
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "stalagmite_bluntness",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0.1,
                                "max": 10
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "wind_speed",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 2
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "min_radius_for_wind",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 100
                    }
                }
            },
            {
                "kind": "pair",
                "key": "min_bluntness_for_wind",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

