"""
Generated from symbols.json for ::java::data::worldgen::feature::SculkPatchConfig
Local link to file: generated_symbols/data/worldgen/feature/SculkPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel


class SculkPatchConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    charge_count: Annotated[int, Field(ge=1, le=32)]
    amount_per_charge: Annotated[int, Field(ge=1, le=500)]
    spread_attempts: Annotated[int, Field(ge=1, le=64)]
    growth_rounds: Annotated[int, Field(ge=0, le=8)]
    spread_rounds: Annotated[int, Field(ge=0, le=8)]


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

