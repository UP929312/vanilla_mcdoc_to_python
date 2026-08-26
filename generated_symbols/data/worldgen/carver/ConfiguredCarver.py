"""
Generated from symbols.json for ::java::data::worldgen::carver::ConfiguredCarver
Local link to file: generated_symbols/data/worldgen/carver/ConfiguredCarver.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.carver.CanyonShape import CanyonShape


@dataclass(kw_only=True)
class ConfiguredCarverCanyon(CarverConfigBase):
    __resource_dir__: ClassVar[str] = 'worldgen/carver'

    type: Literal['minecraft:canyon']
    vertical_rotation: FloatProvider[float] | float
    shape: CanyonShape


@dataclass(kw_only=True)
class ConfiguredCarverCave(CarverConfigBase):
    type: Literal['minecraft:cave']
    count: IntProvider[Annotated[int, 'Range | `0` and above | inclusive']] | Annotated[int, 'Range | `0` and above | inclusive']
    thickness: FloatProvider[Annotated[float, 'Range | `0` and above | inclusive']] | Annotated[float, 'Range | `0` and above | inclusive']
    weird_thickness_bias: bool | None = None  # Defaults to `false`.
    room_vertical_radius_multiplier: FloatProvider[float] | float
    horizontal_radius_multiplier: FloatProvider[float] | float
    vertical_radius_multiplier: FloatProvider[float] | float
    start_vertical_radiues_multiplier: FloatProvider[float] | float | None = None  # Defaults to constant 1.0
    floor_level: FloatProvider[Annotated[float, 'Range | `-1`-`1` | both inclusive']] | Annotated[float, 'Range | `-1`-`1` | both inclusive']


type ConfiguredCarver = ConfiguredCarverCanyon | ConfiguredCarverCave


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::ConfiguredCarver": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/carver"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/carver_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "config",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:carver_config"
                }
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:carver_config"
                }
            }
        ]
    }
}

