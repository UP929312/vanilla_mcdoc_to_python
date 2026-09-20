"""
Generated from symbols.json for ::java::data::worldgen::feature::GrowingPlantHeight
Local link to file: generated_symbols/data/worldgen/feature/GrowingPlantHeight.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class GrowingPlantHeight(GeneratedModel):
    weight: int
    data: IntProvider[int] | int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GrowingPlantHeight": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "data",
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
            }
        ]
    }
}

