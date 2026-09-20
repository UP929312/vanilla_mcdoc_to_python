"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CherryFoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/CherryFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class CherryFoliagePlacer(GeneratedModel):
    height: IntProvider[Annotated[int, Field(ge=4, le=16)]] | Annotated[int, Field(ge=4, le=16)]
    wide_bottom_layer_hole_chance: Annotated[float, Field(ge=0, le=1)]
    corner_hole_chance: Annotated[float, Field(ge=0, le=1)]
    hanging_leaves_chance: Annotated[float, Field(ge=0, le=1)]
    hanging_leaves_extension_chance: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::CherryFoliagePlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
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
                                "min": 4,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "wide_bottom_layer_hole_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "corner_hole_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "hanging_leaves_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "hanging_leaves_extension_chance",
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

