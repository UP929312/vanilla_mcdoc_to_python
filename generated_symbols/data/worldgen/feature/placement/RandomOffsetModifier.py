"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomOffsetModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/RandomOffsetModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class RandomOffsetModifier(GeneratedModel):
    xz_spread: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]
    y_spread: IntProvider[Annotated[int, Field(ge=-16, le=16)]] | Annotated[int, Field(ge=-16, le=16)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::RandomOffsetModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "xz_spread",
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
            },
            {
                "kind": "pair",
                "key": "y_spread",
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

