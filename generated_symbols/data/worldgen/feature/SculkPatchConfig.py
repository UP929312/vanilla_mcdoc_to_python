# Generated from symbols.json for ::java::data::worldgen::feature::SculkPatchConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class SculkPatchConfig:
    charge_count: Annotated[int, 'Range | `1`-`32` | both inclusive']
    amount_per_charge: Annotated[int, 'Range | `1`-`500` | both inclusive']
    spread_attempts: Annotated[int, 'Range | `1`-`64` | both inclusive']
    growth_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']
    spread_rounds: Annotated[int, 'Range | `0`-`8` | both inclusive']
    extra_rare_growths: IntProvider[int] | int
    catalyst_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


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

