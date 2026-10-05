"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::FixedPlacementModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/FixedPlacementModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class FixedPlacementModifier(GeneratedModel):
    positions: Annotated[list[tuple[int, int, int]], Field(min_length=1)]  # Fixed list of block positions to place the feature at.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::FixedPlacementModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Fixed list of block positions to place the feature at.",
                "key": "positions",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "list",
                                "item": {
                                    "kind": "int"
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 3,
                                    "max": 3
                                }
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.4"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "list",
                                "item": {
                                    "kind": "int"
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 3,
                                    "max": 3
                                }
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.4"
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

