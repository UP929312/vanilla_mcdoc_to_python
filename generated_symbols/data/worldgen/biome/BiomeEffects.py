# Generated from symbols.json for ::java::data::worldgen::biome::BiomeEffects
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.GrassColorModifier import GrassColorModifier
    from generated_symbols.util.color.StringRGB import StringRGB


@dataclass(kw_only=True)
class BiomeEffects:
    water_color: StringRGB
    grass_color: StringRGB | None = None
    foliage_color: StringRGB | None = None
    dry_foliage_color: StringRGB | None = None
    grass_color_modifier: GrassColorModifier | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::BiomeEffects": {
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "sky_color",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_rgb"
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
                "key": "fog_color",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_rgb"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "water_color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
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
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::color::StringRGB",
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
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "key": "water_fog_color",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_rgb"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "grass_color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
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
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::color::StringRGB",
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "foliage_color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
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
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::color::StringRGB",
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "dry_foliage_color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
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
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::color::StringRGB",
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
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "grass_color_modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::GrassColorModifier"
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
                "key": "ambient_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
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
                "key": "mood_sound",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "sound",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::util::SoundEventRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "tick_delay",
                            "type": {
                                "kind": "int"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "block_search_extent",
                            "type": {
                                "kind": "int"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "offset",
                            "type": {
                                "kind": "float"
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
                "key": "additions_sound",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "sound",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::util::SoundEventRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "tick_chance",
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
                "key": "music",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::biome::BiomeMusic",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.4"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::util::WeightedList"
                            },
                            "typeArgs": [
                                {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::biome::BiomeMusic"
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.4"
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
                                "value": "1.21.4"
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
                "desc": "The volume of the music in this biome. Defaults to 1.\nThe game will smoothly transition between the current music volume and the new volume when entering the biome.",
                "key": "music_volume",
                "type": {
                    "kind": "float"
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
                "key": "particle",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "options",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::particle::Particle"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "probability",
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
                },
                "optional": True
            }
        ]
    }
}

