"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::CherryTrunkPlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/CherryTrunkPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.UniformIntProvider import UniformIntProvider


class CherryTrunkPlacer(GeneratedModel):
    branch_count: IntProvider[Annotated[int, Field(ge=1, le=3)]] | Annotated[int, Field(ge=1, le=3)]
    branch_horizontal_length: IntProvider[Annotated[int, Field(ge=2, le=16)]] | Annotated[int, Field(ge=2, le=16)]
    branch_start_offset_from_top: UniformIntProvider[Annotated[int, Field(ge=-16, le=0)]] | Annotated[int, Field(ge=-16, le=0)]
    branch_end_offset_from_top: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::CherryTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "branch_count",
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
                                "max": 3
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_horizontal_length",
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
                                "min": 2,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_start_offset_from_top",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::UniformIntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 0
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_end_offset_from_top",
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
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            }
        ]
    }
}

