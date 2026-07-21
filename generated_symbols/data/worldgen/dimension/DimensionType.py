# Generated from symbols.json for ::java::data::worldgen::dimension::DimensionType
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.attribute.GlobalEnvironmentAttributeMap import GlobalEnvironmentAttributeMap
    from generated_symbols.data.worldgen.dimension.CardinalLightType import CardinalLightType
    from generated_symbols.data.worldgen.dimension.SkyboxType import SkyboxType


@dataclass(kw_only=True)
class DimensionType:
    has_skylight: bool  # Affects the weather, lighting engine and respawning rules.
    has_ceiling: bool  # Affects the weather, map items and respawning rules.
    has_ender_dragon_fight: bool
    coordinate_scale: Annotated[float, 'Range | `1e-05`-`30000000` | both inclusive']
    ambient_light: Annotated[float, 'Range | `0`-`1` | both inclusive']
    logical_height: Annotated[int, 'Range | `0`-`4064` | both inclusive']  # Portals can't spawn and chorus fruit can't teleport players above this height.
    infiniburn: str | list[str]  # Defining what blocks keep fire infinitely burning.
    min_y: Annotated[int, 'Range | `-2032`-`2031` | both inclusive | divisible by 16']  # The minimum height in which blocks can exist.
    height: Annotated[int, 'Range | `16`-`4064` | both inclusive | divisible by 16']  # The total height in which blocks can exist. Max Y = Min Y + Height.
    monster_spawn_light_level: IntProvider[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive']
    monster_spawn_block_light_limit: Annotated[int, 'Range | `0`-`15` | both inclusive']
    attributes: GlobalEnvironmentAttributeMap | None = None
    default_clock: str | None = None
    timelines: str | list[str] | None = None
    has_fixed_time: bool | None = None  # Defaults to `false`.
    skybox: SkyboxType | None = None  # Skybox type. Defaults to `overworld`.
    cardinal_light: CardinalLightType | None = None  # The direction of cardinal lighting that affects blocks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::DimensionType": {
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "attributes",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap"
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "default_clock",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "world_clock"
                                }
                            }
                        }
                    ]
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "timelines",
                "type": {
                    "kind": "union",
                    "members": [
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
                                                    "value": "timeline"
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
                                                "value": "timeline"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If True, water will evaporate and sponges will dry.",
                "key": "ultrawarm",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If True, portals will spawn zombified piglins. If False, compasses and clocks spin randomly.",
                "key": "natural",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If False, piglins will shake and convert to zombified piglins.",
                "key": "piglin_safe",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If True, players can charge and use respawn anchors to set their spawn. If False, respawn anchors will blow up when used.",
                "key": "respawn_anchor_works",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If True, players can use beds to set their spawn and advance time. If False, beds will blow up when used.",
                "key": "bed_works",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "If True, players with the Bad Omen effect can cause a raid.",
                "key": "has_raids",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "desc": "Affects the weather, lighting engine and respawning rules.",
                "key": "has_skylight",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "desc": "Affects the weather, map items and respawning rules.",
                "key": "has_ceiling",
                "type": {
                    "kind": "boolean"
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "has_ender_dragon_fight",
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
                                "value": "1.16.2"
                            }
                        }
                    }
                ],
                "key": "shrunk",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.16.2"
                            }
                        }
                    }
                ],
                "key": "coordinate_scale",
                "type": {
                    "kind": "double",
                    "valueRange": {
                        "kind": 0,
                        "min": 1e-05,
                        "max": 30000000
                    }
                }
            },
            {
                "kind": "pair",
                "key": "ambient_light",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Setting this value will keep the sun in a fixed position.",
                "key": "fixed_time",
                "type": {
                    "kind": "int"
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `False`.",
                "key": "has_fixed_time",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Portals can't spawn and chorus fruit can't teleport players above this height.",
                "key": "logical_height",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 256
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
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 4064
                            },
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
                                "value": "1.16.2"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Sky effects.",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::DimensionTypeEffects",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "Skybox type.\nDefaults to `overworld`.",
                "key": "skybox",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::SkyboxType"
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "The direction of cardinal lighting that affects blocks.",
                "key": "cardinal_light",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::CardinalLightType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defining what blocks keep fire infinitely burning.",
                "key": "infiniburn",
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
                ],
                "desc": "The minimum height in which blocks can exist.",
                "key": "min_y",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -2032,
                        "max": 2031
                    },
                    "attributes": [
                        {
                            "name": "divisible_by",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "int",
                                    "value": 16
                                }
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "The total height in which blocks can exist. Max Y = Min Y + Height.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 16,
                        "max": 4064
                    },
                    "attributes": [
                        {
                            "name": "divisible_by",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "int",
                                    "value": 16
                                }
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "monster_spawn_light_level",
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
                                "max": 15
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "monster_spawn_block_light_limit",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
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
                                "value": "1.21.6"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "The Y-level where the clouds start in the dimension. If not present, no clouds will be visible.",
                "key": "cloud_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -2032,
                        "max": 2031
                    }
                },
                "optional": True
            }
        ]
    }
}

