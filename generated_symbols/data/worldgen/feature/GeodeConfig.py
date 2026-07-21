# Generated from symbols.json for ::java::data::worldgen::feature::GeodeConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.feature.GeodeBlockSettings import GeodeBlockSettings
    from generated_symbols.data.worldgen.feature.GeodeCrackSettings import GeodeCrackSettings
    from generated_symbols.data.worldgen.feature.GeodeLayerSettings import GeodeLayerSettings


@dataclass(kw_only=True)
class GeodeConfig:
    blocks: GeodeBlockSettings
    layers: GeodeLayerSettings
    crack: GeodeCrackSettings
    invalid_blocks_threshold: int
    noise_multiplier: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    use_potential_placements_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    use_alternate_layer0_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    placements_require_layer0_alternate: bool | None = None
    outer_wall_distance: IntProvider[Annotated[int, 'Range | `1`-`20` | both inclusive']] | Annotated[int, 'Range | `1`-`20` | both inclusive'] | None = None
    distribution_points: IntProvider[Annotated[int, 'Range | `1`-`20` | both inclusive']] | Annotated[int, 'Range | `1`-`20` | both inclusive'] | None = None
    point_offset: IntProvider[Annotated[int, 'Range | `1`-`10` | both inclusive']] | Annotated[int, 'Range | `1`-`10` | both inclusive'] | None = None
    min_gen_offset: int | None = None
    max_gen_offset: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GeodeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "blocks",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::GeodeBlockSettings"
                }
            },
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::GeodeLayerSettings"
                }
            },
            {
                "kind": "pair",
                "key": "crack",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::GeodeCrackSettings"
                }
            },
            {
                "kind": "pair",
                "key": "noise_multiplier",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "use_potential_placements_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "use_alternate_layer0_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "placements_require_layer0_alternate",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "outer_wall_distance",
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
                                "min": 1,
                                "max": 20
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "distribution_points",
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
                                "min": 1,
                                "max": 20
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "point_offset",
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
                                "min": 1,
                                "max": 10
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "min_gen_offset",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max_gen_offset",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "invalid_blocks_threshold",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

