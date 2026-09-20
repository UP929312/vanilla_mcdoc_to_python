"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseSettings
Local link to file: generated_symbols/data/worldgen/noise_settings/NoiseSettings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class NoiseSettings(GeneratedModel):
    min_y: Annotated[int, Field(ge=-2048, le=2047)]  # Minimum height where blocks start generating.
    height: Annotated[int, Field(ge=0, le=4096)]  # The total height where blocks can generate. Max Y = Min Y + Height.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseSettings": {
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Minimum height where blocks start generating.",
                "key": "min_y",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -2048,
                        "max": 2047
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "The total height where blocks can generate. Max Y = Min Y + Height.",
                "key": "height",
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
                                "max": 4096
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
                "key": "size_horizontal",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 4
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "size_vertical",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 4
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "density_factor",
                "type": {
                    "kind": "double"
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
                "key": "density_offset",
                "type": {
                    "kind": "double"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "sampling",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseSamplingSettings"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Adds or removes terrain at the top of the world. Does nothing when size is 0.",
                "key": "top_slide",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseSlideSettings"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Adds or removes terrain at the bottom of the world. Does nothing when size is 0.",
                "key": "bottom_slide",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::NoiseSlideSettings"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "terrain_shaper",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::noise_settings::TerrainShaper"
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
                "key": "simplex_surface_noise",
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
                "key": "random_density_offset",
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "desc": "If True, terrain will be shaped like islands similar to the end.",
                "key": "island_noise_override",
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "amplified",
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "large_biomes",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

