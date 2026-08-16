"""
Generated from symbols.json for ::java::data::worldgen::material_condition::YAboveCondition
Local link to file: generated_symbols/data/worldgen/material_condition/YAboveCondition.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class YAboveCondition:
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    anchor: VerticalAnchor
    surface_depth_multiplier: Annotated[int, 'Range | `-20`-`20` | both inclusive']
    add_stone_depth: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::YAboveCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "anchor",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
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

