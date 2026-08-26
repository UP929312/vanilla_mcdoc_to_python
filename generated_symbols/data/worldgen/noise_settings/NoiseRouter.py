"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseRouter
Local link to file: generated_symbols/data/worldgen/noise_settings/NoiseRouter.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


@dataclass(kw_only=True)
class NoiseRouter:
    temperature: DensityFunctionRef
    vegetation: DensityFunctionRef
    continents: DensityFunctionRef
    erosion: DensityFunctionRef
    depth: DensityFunctionRef
    ridges: DensityFunctionRef
    chunk_surface_level: DensityFunctionRef
    final_density: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseRouter": {
        "kind": "struct",
        "fields": [
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
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "barrier",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "fluid_level_floodedness",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "fluid_level_spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "lava",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "vein_toggle",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "vein_ridged",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "vein_gap",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "temperature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "vegetation",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "continents",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "erosion",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "depth",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "ridges",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ],
                "key": "initial_density_without_jaggedness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
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
                                "value": "1.21.9"
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
                "key": "preliminary_surface_level",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
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
                "key": "chunk_surface_level",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "final_density",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

