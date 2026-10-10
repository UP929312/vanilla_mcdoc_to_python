"""
Generated from symbols.json for ::java::data::worldgen::material_condition::WaterCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/WaterCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class WaterCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    offset: int
    surface_depth_multiplier: Annotated[int, Field(ge=-20, le=20)]
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
