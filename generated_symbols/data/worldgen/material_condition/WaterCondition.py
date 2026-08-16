"""
Generated from symbols.json for ::java::data::worldgen::material_condition::WaterCondition
Local link to file: generated_symbols/data/worldgen/material_condition/WaterCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar


@dataclass(kw_only=True)
class WaterCondition:
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    offset: int
    surface_depth_multiplier: Annotated[int, 'Range | `-20`-`20` | both inclusive']
    add_stone_depth: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::WaterCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offset",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "surface_depth_multiplier",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -20,
                        "max": 20
                    }
                }
            },
            {
                "kind": "pair",
                "key": "add_stone_depth",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

