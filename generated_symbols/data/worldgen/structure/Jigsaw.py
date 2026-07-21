# Generated from symbols.json for ::java::data::worldgen::structure::Jigsaw
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.data.worldgen.HeightmapType import HeightmapType
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings
    from generated_symbols.data.worldgen.structure.PoolAlias import PoolAlias


@dataclass(kw_only=True)
class Jigsaw:
    start_pool: str
    size: Annotated[int, 'Range | `1`-`20` | both inclusive']
    start_height: HeightProvider
    max_distance_from_center: Any
    use_expansion_hack: bool
    start_jigsaw_name: str | None = None
    project_start_to_heightmap: HeightmapType | None = None
    pool_aliases: list[PoolAlias] | None = None
    dimension_padding: Annotated[int, 'Range | Min `0` and above | inclusive'] | Any | None = None
    liquid_settings: LiquidSettings | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::Jigsaw": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "start_pool",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/template_pool"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "size",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 7
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 20
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.3"
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "start_height",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::HeightProvider"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "start_jigsaw_name",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id"
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "project_start_to_heightmap",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::HeightmapType"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "max_distance_from_center",
                            "type": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            "terrain_adaptation"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:jigsaw_max_distance_from_center"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "use_expansion_hack",
                            "type": {
                                "kind": "boolean"
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "pool_aliases",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure::PoolAlias"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "dimension_padding",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        }
                                    },
                                    {
                                        "kind": "struct",
                                        "fields": [
                                            {
                                                "kind": "pair",
                                                "key": "bottom",
                                                "type": {
                                                    "kind": "int",
                                                    "valueRange": {
                                                        "kind": 0,
                                                        "min": 0
                                                    }
                                                },
                                                "optional": True
                                            },
                                            {
                                                "kind": "pair",
                                                "key": "top",
                                                "type": {
                                                    "kind": "int",
                                                    "valueRange": {
                                                        "kind": 0,
                                                        "min": 0
                                                    }
                                                },
                                                "optional": True
                                            }
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "liquid_settings",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::structure::LiquidSettings"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

