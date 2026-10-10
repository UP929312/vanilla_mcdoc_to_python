"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::BendingTrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/BendingTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class BendingTrunkPlacer(GeneratedModel):
    bend_length: IntProvider[Annotated[int, Field(ge=1, le=64)]] | Annotated[int, Field(ge=1, le=64)]
    min_height_for_leaves: Annotated[int, Field(ge=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::BendingTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "bend_length",
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
                                "min": 1,
                                "max": 64
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "min_height_for_leaves",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}
