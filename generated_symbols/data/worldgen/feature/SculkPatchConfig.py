# Generated from symbols.json for ::java::data::worldgen::feature::SculkPatchConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class SculkPatchConfig:
    charge_count: Annotated[int, 'Range | `1`-`32` | both inclusive']
    amount_per_charge: Annotated[int, 'Range | `1`-`500` | both inclusive']
    spread_attempts: Annotated[int, 'Range | `1`-`64` | both inclusive']
    growth_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']
    spread_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SculkPatchConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "charge_count",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 32
                    }
                }
            },
            {
                "kind": "pair",
                "key": "amount_per_charge",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 500
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 64
                    }
                }
            },
            {
                "kind": "pair",
                "key": "growth_rounds",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                }
            },
            {
                "kind": "pair",
                "key": "spread_rounds",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
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
                "key": "extra_rare_growths",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
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
                "key": "catalyst_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

