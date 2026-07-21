# Generated from symbols.json for ::java::data::worldgen::biome::Biome
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttributeMap import PositionalEnvironmentAttributeMap
    from generated_symbols.data.worldgen.biome.BiomeEffects import BiomeEffects
    from generated_symbols.data.worldgen.biome.TemperatureModifier import TemperatureModifier
    from generated_symbols.data.worldgen.carver.CarverRef import CarverRef
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


@dataclass(kw_only=True)
class Biome:
    temperature: float
    downfall: float
    has_precipitation: bool
    effects: BiomeEffects
    carvers: list[CarverRef] | str
    features: Annotated[list[list[PlacedFeatureRef] | str], 'Length = up to 11 (inclusive)']
    attributes: PositionalEnvironmentAttributeMap | None = None
    temperature_modifier: TemperatureModifier | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::Biome": {
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
                    "path": "::java::data::worldgen::attribute::PositionalEnvironmentAttributeMap"
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
                "key": "category",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::BiomeCategory"
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
                "desc": "Raises or lowers the terrain. Positive values are considered land and negative are oceans.",
                "key": "depth",
                "type": {
                    "kind": "float"
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
                "desc": "Vertically stretches the terrain. Lower values produce flatter terrain.",
                "key": "scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "temperature",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "downfall",
                "type": {
                    "kind": "float"
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
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "key": "precipitation",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::Precipitation"
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
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "key": "has_precipitation",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "temperature_modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::TemperatureModifier"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "desc": "If True, the world spawn will be preferred in this biome.",
                "key": "player_spawn_friendly",
                "type": {
                    "kind": "boolean"
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "creature_spawn_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 0.9999999
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::BiomeEffects"
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
                "key": "surface_builder",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilderRef"
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
                "key": "starts",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure::StructureRef"
                    }
                }
            },
            {
                "kind": "spread",
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
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::NaturalMobSpawns"
                }
            },
            {
                "kind": "pair",
                "key": "carvers",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": {
                                        "kind": "reference",
                                        "path": "::java::data::worldgen::CarveStep"
                                    },
                                    "type": {
                                        "kind": "union",
                                        "members": [
                                            {
                                                "kind": "list",
                                                "item": {
                                                    "kind": "reference",
                                                    "path": "::java::data::worldgen::carver::CarverRef"
                                                }
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
                                                            "kind": "tree",
                                                            "values": {
                                                                "registry": {
                                                                    "kind": "literal",
                                                                    "value": {
                                                                        "kind": "string",
                                                                        "value": "worldgen/configured_carver"
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
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::data::worldgen::carver::CarverRef"
                                    }
                                },
                                {
                                    "kind": "string",
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
                                                            "value": "worldgen/configured_carver"
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
                                    "kind": "string",
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
                                                            "value": "worldgen/carver"
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
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
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
                "key": "features",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::feature::ConfiguredFeatureRef"
                                }
                            },
                            "lengthRange": {
                                "kind": 0,
                                "max": 10
                            },
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
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "list",
                                        "item": {
                                            "kind": "reference",
                                            "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef"
                                        }
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
                                                    "kind": "tree",
                                                    "values": {
                                                        "registry": {
                                                            "kind": "literal",
                                                            "value": {
                                                                "kind": "string",
                                                                "value": "worldgen/placed_feature"
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
                                    }
                                ]
                            },
                            "lengthRange": {
                                "kind": 0,
                                "max": 11
                            },
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
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

