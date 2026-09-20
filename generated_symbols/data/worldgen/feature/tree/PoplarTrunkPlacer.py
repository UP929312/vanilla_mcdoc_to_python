"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::PoplarTrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/PoplarTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class PoplarTrunkPlacer(GeneratedModel):
    trunk_height_above_branches: IntProvider[Annotated[int, Field(ge=0, le=8)]] | Annotated[int, Field(ge=0, le=8)]
    branch_amount: IntProvider[Annotated[int, Field(ge=1, le=4)]] | Annotated[int, Field(ge=1, le=4)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PoplarTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "trunk_height_above_branches",
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
                                "min": 0,
                                "max": 8
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_amount",
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
                                "max": 4
                            }
                        }
                    ]
                }
            }
        ]
    }
}

