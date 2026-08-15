"""
Generated from symbols.json for ::java::data::worldgen::material_condition::NoiseThresholdCondition
Local link to file: generated_symbols/data/worldgen/material_condition/NoiseThresholdCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class NoiseThresholdCondition:
    noise: Annotated[str, IdSpec(registry='worldgen/noise')]
    min_threshold: float
    max_threshold: float
    is_3d: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::NoiseThresholdCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "noise",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/noise"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "min_threshold",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "max_threshold",
                "type": {
                    "kind": "float"
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
                                "value": "26.2"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `False`.",
                "key": "is_3d",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

