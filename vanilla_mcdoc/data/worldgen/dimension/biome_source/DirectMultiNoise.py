"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::DirectMultiNoise
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/DirectMultiNoise.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameters import ClimateParameters


class BiomesStruct(GeneratedModel):
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]
    parameters: ClimateParameters


class DirectMultiNoise(GeneratedModel):
    biomes: list[BiomesStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::DirectMultiNoise": {
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "temperature_noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "humidity_noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "altitude_noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "weirdness_noise",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
                }
            },
            {
                "kind": "pair",
                "key": "biomes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "biome",
                                "type": {
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
                            },
                            {
                                "kind": "pair",
                                "key": "parameters",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameters"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}
