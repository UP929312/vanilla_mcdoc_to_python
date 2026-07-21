# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::ClimateParameter
from typing import Annotated


type ClimateParameter = Annotated[float, 'Range | `-2`-`2` | both inclusive'] | tuple[Annotated[float, 'Range | `-2`-`2` | both inclusive'], Annotated[float, 'Range | `-2`-`2` | both inclusive']]


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

