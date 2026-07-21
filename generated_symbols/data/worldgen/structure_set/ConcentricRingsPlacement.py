# Generated from symbols.json for ::java::data::worldgen::structure_set::ConcentricRingsPlacement
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ConcentricRingsPlacement:
    distance: Annotated[int, 'Range | `0`-`1023` | both inclusive']
    spread: Annotated[int, 'Range | `0`-`1023` | both inclusive']
    count: Annotated[int, 'Range | `1`-`4095` | both inclusive']
    preferred_biomes: list[str] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::ConcentricRingsPlacement": {
        "kind": "struct",
        "fields": [
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

