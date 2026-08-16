"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::NoiseParameters
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/NoiseParameters.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class NoiseParameters:
    __resource_dir__: ClassVar[str] = 'worldgen/noise'

    base_octave: Annotated[int, 'Range | `-32`-`32` | both inclusive']
    base_amplitude: Annotated[float, 'Range | `0`-`1000000` | both inclusive'] | None = None  # Defaults to 1.0.
    octave_count: Annotated[int, 'Range | `1`-`32` | both inclusive'] | None = None  # Defaults to 1.
    normalize: bool | None = None  # Defaults to `true`.
    amplitude_modifiers: Annotated[list[Annotated[float, 'Range | `0`-`1000000` | both inclusive']], 'Length = up to 32 (inclusive)'] | None = None  # When empty or not present, defaults to all 1.0.  Otherwise, the size must match `octave_count`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::NoiseParameters": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "firstOctave",
                            "type": {
                                "kind": "int"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "amplitudes",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "double"
                                }
                            }
                        }
                    ]
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
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "base_octave",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": -32,
                                    "max": 32
                                }
                            }
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to 1.0.",
                            "key": "base_amplitude",
                            "type": {
                                "kind": "double",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0,
                                    "max": 1000000
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to 1.",
                            "key": "octave_count",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1,
                                    "max": 32
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to `True`.",
                            "key": "normalize",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "boolean"
                                    },
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "legacy"
                                        },
                                        "attributes": [
                                            {
                                                "name": "deprecated"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "When empty or not present, defaults to all 1.0. \\\nOtherwise, the size must match `octave_count`.",
                            "key": "amplitude_modifiers",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "double",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 1000000
                                    }
                                },
                                "lengthRange": {
                                    "kind": 0,
                                    "max": 32
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

