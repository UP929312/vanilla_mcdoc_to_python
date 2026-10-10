"""
Generated from symbols.json for ::java::data::worldgen::feature::SpeleothemClusterConfig
Local link to file: generated_symbols/data/worldgen/feature/SpeleothemClusterConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.SpeleothemBaseBlockTransformer import SpeleothemBaseBlockTransformer
    from generated_symbols.data.worldgen.feature.SpeleothemClusterPlacementMode import SpeleothemClusterPlacementMode
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.block_state.BlockState import BlockState


class PlacementOptionsStruct(GeneratedModel):
    placement_mode: SpeleothemClusterPlacementMode
    base_block_transformer: SpeleothemBaseBlockTransformer
    allow_water_placement: bool


class SpeleothemClusterConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    base_block: BlockState
    pointed_block: BlockState
    replaceable_blocks: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId
    floor_to_ceiling_search_range: Annotated[int, Field(ge=1, le=512)]
    height: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    radius: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    max_stalagmite_stalactite_height_diff: Annotated[int, Field(ge=0, le=64)]  # Max height difference between the stalagmite and stalactite.
    height_deviation: Annotated[int, Field(ge=1, le=64)]
    speleothem_block_layer_thickness: IntProvider[Annotated[int, Field(ge=0, le=128)]] | Annotated[int, Field(ge=0, le=128)]
    density: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    wetness: FloatProvider[Annotated[float, Field(ge=0, le=2)]] | Annotated[float, Field(ge=0, le=2)]
    chance_of_speleothem_at_max_distance_from_center: Annotated[float, Field(ge=0, le=1)]
    max_distance_from_edge_affecting_chance_of_speleothem: Annotated[int, Field(ge=1, le=64)]
    max_distance_from_center_affecting_height_bias: Annotated[int, Field(ge=1, le=64)]
    placement_options: PlacementOptionsStruct | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SpeleothemClusterConfig": {
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
                "key": "pointed_block",
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
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
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
                                "max": 128
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "radius",
                "type": {
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
                                "max": 128
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Max height difference between the stalagmite and stalactite.",
                "key": "max_stalagmite_stalactite_height_diff",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height_deviation",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 64
                    }
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "key": "dripstone_block_layer_thickness",
                "type": {
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
                                "max": 128
                            }
                        }
                    ]
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
                "key": "speleothem_block_layer_thickness",
                "type": {
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
                                "max": 128
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "density",
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
                "key": "wetness",
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
                ],
                "key": "chance_of_dripstone_column_at_max_distance_from_center",
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
                "key": "chance_of_speleothem_at_max_distance_from_center",
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
                ],
                "key": "max_distance_from_edge_affecting_chance_of_dripstone_column",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 64
                    }
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
                "key": "max_distance_from_edge_affecting_chance_of_speleothem",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 64
                    }
                }
            },
            {
                "kind": "pair",
                "key": "max_distance_from_center_affecting_height_bias",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 64
                    }
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
                                "value": "26.4"
                            }
                        }
                    }
                ],
                "key": "placement_options",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "placement_mode",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::SpeleothemClusterPlacementMode"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "base_block_transformer",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::SpeleothemBaseBlockTransformer"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "allow_water_placement",
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
