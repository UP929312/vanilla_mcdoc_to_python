"""
Generated from symbols.json for ::java::data::worldgen::feature::LargeSpeleothemConfig
Local link to file: generated_symbols/data/worldgen/feature/LargeSpeleothemConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.block_state.BlockState import BlockState


class LargeSpeleothemConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    base_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, Field(ge=1, le=512)] | None = None
    column_radius: IntProvider[Annotated[int, Field(ge=0, le=16)]] | Annotated[int, Field(ge=0, le=16)]
    height_scale: FloatProvider[Annotated[float, Field(ge=0, le=20)]] | Annotated[float, Field(ge=0, le=20)]
    max_column_radius_to_cave_height_ratio: Annotated[float, Field(ge=0, le=1)]
    stalactite_bluntness: FloatProvider[Annotated[float, Field(ge=0.1, le=10)]] | Annotated[float, Field(ge=0.1, le=10)]
    stalagmite_bluntness: FloatProvider[Annotated[float, Field(ge=0.1, le=10)]] | Annotated[float, Field(ge=0.1, le=10)]
    wind_speed: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    min_radius_for_wind: Annotated[int, Field(ge=0, le=100)]
    min_bluntness_for_wind: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::LargeSpeleothemConfig": {
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
                                "value": "26.4"
                            }
                        }
                    }
                ],
                "key": "base_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
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

