# Generated from symbols.json for ::java::data::worldgen::carver::ConfiguredCarver
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.carver.CanyonShape import CanyonShape


@dataclass(kw_only=True)
class ConfiguredCarverCanyon(CarverConfigBase):
    type: Literal['minecraft:canyon']
    vertical_rotation: FloatProvider[float] | float
    shape: CanyonShape


@dataclass(kw_only=True)
class ConfiguredCarverCave(CarverConfigBase):
    type: Literal['minecraft:cave']
    count: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']
    thickness: FloatProvider[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive']
    room_vertical_radius_multiplier: FloatProvider[float] | float
    horizontal_radius_multiplier: FloatProvider[float] | float
    vertical_radius_multiplier: FloatProvider[float] | float
    floor_level: FloatProvider[Annotated[float, 'Range | `-1`-`1` | both inclusive']] | Annotated[float, 'Range | `-1`-`1` | both inclusive']
    weird_thickness_bias: bool | None = None  # Defaults to `false`.
    start_vertical_radiues_multiplier: FloatProvider[float] | float | None = None  # Defaults to constant 1.0


@dataclass(kw_only=True)
class ConfiguredCarverNetherCave(CarverConfigBase):
    type: Literal['minecraft:nether_cave']
    count: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']
    thickness: FloatProvider[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive']
    room_vertical_radius_multiplier: FloatProvider[float] | float
    horizontal_radius_multiplier: FloatProvider[float] | float
    vertical_radius_multiplier: FloatProvider[float] | float
    floor_level: FloatProvider[Annotated[float, 'Range | `-1`-`1` | both inclusive']] | Annotated[float, 'Range | `-1`-`1` | both inclusive']
    weird_thickness_bias: bool | None = None  # Defaults to `false`.
    start_vertical_radiues_multiplier: FloatProvider[float] | float | None = None  # Defaults to constant 1.0


type ConfiguredCarver = ConfiguredCarverCanyon | ConfiguredCarverCave | ConfiguredCarverNetherCave


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

