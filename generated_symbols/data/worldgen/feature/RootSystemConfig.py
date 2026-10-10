"""
Generated from symbols.json for ::java::data::worldgen::feature::RootSystemConfig
Local link to file: generated_symbols/data/worldgen/feature/RootSystemConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from generated_symbols.registry.KnownBlockId import KnownBlockId


class RootSystemConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    required_vertical_space_for_tree: Annotated[int, Field(ge=1, le=64)]
    level_test_distance: Annotated[int, Field(ge=0, le=16)]
    max_level_deviation: Annotated[int, Field(ge=0, le=64)]
    root_radius: Annotated[int, Field(ge=1, le=64)]
    root_placement_attempts: Annotated[int, Field(ge=1, le=256)]
    root_column_max_height: Annotated[int, Field(ge=1, le=4096)]
    hanging_root_radius: Annotated[int, Field(ge=1, le=64)]
    hanging_roots_vertical_span: Annotated[int, Field(ge=1, le=16)]
    hanging_root_placement_attempts: Annotated[int, Field(ge=0, le=256)]
    allowed_vertical_water_for_tree: Annotated[int, Field(ge=1, le=64)]
    root_replaceable: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]
    root_state_provider: BlockStateProviderRef
    hanging_root_state_provider: BlockStateProviderRef
    allowed_tree_position: BlockPredicate
    feature: FeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RootSystemConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "required_vertical_space_for_tree",
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
                "key": "level_test_distance",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
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
                "key": "max_level_deviation",
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
                "key": "root_radius",
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
                "key": "root_placement_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 256
                    }
                }
            },
            {
                "kind": "pair",
                "key": "root_column_max_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 4096
                    }
                }
            },
            {
                "kind": "pair",
                "key": "hanging_root_radius",
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
                "key": "hanging_roots_vertical_span",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 16
                    }
                }
            },
            {
                "kind": "pair",
                "key": "hanging_root_placement_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 256
                    }
                }
            },
            {
                "kind": "pair",
                "key": "allowed_vertical_water_for_tree",
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
                "key": "root_replaceable",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                },
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
                                                    "value": "implicit"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                },
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.2"
                                        }
                                    }
                                },
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
                                                    "value": "required"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
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
                                },
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
                        },
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
                            },
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
                "key": "root_state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "hanging_root_state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "allowed_tree_position",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            },
            {
                "kind": "pair",
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

