"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::ClimateParameter
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/ClimateParameter.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field


type ClimateParameter = Annotated[float, Field(ge=-2, le=2)] | tuple[Annotated[float, Field(ge=-2, le=2)], Annotated[float, Field(ge=-2, le=2)]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::ClimateParameter": {
        "kind": "union",
        "members": [
            {
                "kind": "float",
                "valueRange": {
                    "kind": 0,
                    "min": -2,
                    "max": 2
                }
            },
            {
                "kind": "list",
                "item": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": -2,
                        "max": 2
                    }
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 2,
                    "max": 2
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
