# Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseGeneratorSettings
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef
    from generated_symbols.data.worldgen.noise_settings.Aquifer import Aquifer
    from generated_symbols.data.worldgen.noise_settings.NoiseRouter import NoiseRouter
    from generated_symbols.data.worldgen.noise_settings.NoiseSettings import NoiseSettings
    from generated_symbols.data.worldgen.noise_settings.OreVeinifier import OreVeinifier
    from generated_symbols.data.worldgen.noise_settings.SpawnTargetPoint import SpawnTargetPoint
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class NoiseGeneratorSettings:
    default_block: BlockState
    default_fluid: BlockState
    sea_level: int
    disable_mob_generation: bool  # If true, mobs will not spawn during generation.
    legacy_random_source: bool
    noise: NoiseSettings
    noise_router: NoiseRouter
    spawn_target: list[SpawnTargetPoint]
    material_rule: MaterialRuleRef
    aquifers: Aquifer | None = None
    ore_veins: list[OreVeinifier] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseGeneratorSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "default_block",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "default_fluid",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "desc": "Relative position of the bedrock roof starting at the world height. Higher numbers move the roof down.",
                "key": "bedrock_roof_position",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -20,
                                "max": 276
                            },
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
                            "kind": "int",
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "bedrock_floor_position",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -20,
                                "max": 276
                            },
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
                            "kind": "int",
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
                "key": "sea_level",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 255
                            },
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
                            "kind": "int",
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "min_surface_level",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "desc": "If True, mobs will not spawn during generation.",
                "key": "disable_mob_generation",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.17"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
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
                                }
                            ],
                            "key": "noise_caves_enabled",
                            "type": {
                                "kind": "boolean"
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
                                            "value": "1.18.2"
                                        }
                                    }
                                }
                            ],
                            "key": "noodle_caves_enabled",
                            "type": {
                                "kind": "boolean"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "aquifers_enabled",
                            "type": {
                                "kind": "boolean"
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
                                            "value": "1.18"
                                        }
                                    }
                                }
                            ],
                            "key": "deepslate_enabled",
                            "type": {
                                "kind": "boolean"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "ore_veins_enabled",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "aquifers",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::Aquifer"
                },
                "optional": True
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "ore_veins",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::noise_settings::OreVeinifier"
                    }
                },
                "optional": True
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
                "key": "legacy_random_source",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseSettings"
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "noise_router",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseRouter"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "spawn_target",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::dimension::biome_source::ClimateParameters"
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::noise_settings::SpawnTargetPoint"
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
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
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "surface_rule",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::material_rule::MaterialRuleRef"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "material_rule",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::material_rule::MaterialRuleRef"
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "structures",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::StructureSettings"
                }
            }
        ]
    }
}

