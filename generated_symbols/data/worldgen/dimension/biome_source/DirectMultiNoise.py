# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::DirectMultiNoise
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class DirectMultiNoise:
    biomes: list[Any]


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

