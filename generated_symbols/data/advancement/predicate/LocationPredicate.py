"""
Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicate
Local link to file: generated_symbols/data/advancement/predicate/LocationPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.advancement.predicate.FluidPredicate import FluidPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class PositionStruct:
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None


@dataclass(kw_only=True)
class LightStruct:
    light: MinMaxBounds[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None


@dataclass(kw_only=True)
class LocationPredicate:
    position: PositionStruct | None = None
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]] | None = None
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]] | None = None
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    light: LightStruct | None = None  # Calculated using: `max(sky-darkening, block)`.
    block: BlockPredicate | None = None
    fluid: FluidPredicate | None = None
    smokey: bool | None = None  # Whether the block is above (5 blocks or less) a campfire or soul campfire.
    can_see_sky: bool | None = None  # Whether the location has the maximum possible level of sky light


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LocationPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "position",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "x",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "float"
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "y",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "float"
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "z",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "float"
                                    }
                                ]
                            },
                            "optional": True
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "biome",
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
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "biome"
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
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/biome"
                                        }
                                    }
                                }
                            ]
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "biomes",
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
                                                    "value": "worldgen/biome"
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
                                                "value": "worldgen/biome"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "feature",
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
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/configured_structure_feature"
                                        }
                                    }
                                }
                            ]
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
                                "value": "1.19"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "structure",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/structure"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "structures",
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
                                                    "value": "worldgen/structure"
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
                                                "value": "worldgen/structure"
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
                "key": "dimension",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Calculated using: `max(sky-darkening, block)`.",
                "key": "light",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "light",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "reference",
                                    "path": "::java::data::util::MinMaxBounds"
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
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::BlockPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "fluid",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::FluidPredicate"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Whether the block is above (5 blocks or less) a campfire or soul campfire.",
                "key": "smokey",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Whether the location has the maximum possible level of sky light",
                "key": "can_see_sky",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

