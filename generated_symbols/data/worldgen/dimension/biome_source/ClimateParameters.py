"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::ClimateParameters
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/ClimateParameters.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameter import ClimateParameter


class ClimateParameters(GeneratedModel):
    temperature: ClimateParameter
    humidity: ClimateParameter
    continentalness: ClimateParameter
    erosion: ClimateParameter
    weirdness: ClimateParameter
    depth: ClimateParameter
    offset: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::ClimateParameters": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "temperature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
                }
            },
            {
                "kind": "pair",
                "key": "humidity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
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
                "key": "altitude",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": -2,
                        "max": 2
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "continentalness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
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
                "key": "erosion",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
                }
            },
            {
                "kind": "pair",
                "key": "weirdness",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
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
                "key": "depth",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
                }
            },
            {
                "kind": "pair",
                "key": "offset",
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
    }
}

