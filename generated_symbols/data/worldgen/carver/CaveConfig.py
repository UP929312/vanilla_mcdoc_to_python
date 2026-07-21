# Generated from symbols.json for ::java::data::worldgen::carver::CaveConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class CaveConfig(CarverConfigBase):
    count: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']
    thickness: FloatProvider[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive']
    room_vertical_radius_multiplier: FloatProvider[float] | float
    horizontal_radius_multiplier: FloatProvider[float] | float
    vertical_radius_multiplier: FloatProvider[float] | float
    floor_level: FloatProvider[Annotated[float, 'Range | `-1`-`1` | both inclusive']] | Annotated[float, 'Range | `-1`-`1` | both inclusive']
    weird_thickness_bias: bool | None = None  # Defaults to `false`.
    start_vertical_radiues_multiplier: FloatProvider[float] | float | None = None  # Defaults to constant 1.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CaveConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::carver::CarverConfigBase"
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
                "key": "count",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        }
                    ]
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
                "key": "thickness",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        }
                    ]
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
                "desc": "Defaults to `False`.",
                "key": "weird_thickness_bias",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "room_vertical_radius_multiplier",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "horizontal_radius_multiplier",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "vertical_radius_multiplier",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
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
                "desc": "Defaults to constant 1.0",
                "key": "start_vertical_radiues_multiplier",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "floor_level",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": -1,
                                "max": 1
                            }
                        }
                    ]
                }
            }
        ]
    }
}

