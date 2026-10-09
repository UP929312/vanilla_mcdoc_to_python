"""
Generated from symbols.json for ::java::data::worldgen::structure_set::ConcentricRingsPlacement
Local link to file: generated_symbols/data/worldgen/structure_set/ConcentricRingsPlacement.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.data.worldgen.structure_set.SpreadingPlacementBase import SpreadingPlacementBase
from minecraft_registry import IdSpec
from pydantic import Field


class ConcentricRingsPlacement(SpreadingPlacementBase):
    distance: Annotated[int, Field(ge=0, le=1023)]
    spread: Annotated[int, Field(ge=0, le=1023)]
    count: Annotated[int, Field(ge=1, le=4095)]
    preferred_biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::ConcentricRingsPlacement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::SpreadingPlacementBase"
                }
            },
            {
                "kind": "pair",
                "key": "distance",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1023
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1023
                    }
                }
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 4095
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "preferred_biomes",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
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
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/biome"
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
        ]
    }
}

