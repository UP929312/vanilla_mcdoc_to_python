"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::RandomSpreadFoliagePlacer
Local link to file: generated_symbols/data/worldgen/feature/tree/RandomSpreadFoliagePlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class RandomSpreadFoliagePlacer(GeneratedModel):
    foliage_height: IntProvider[Annotated[int, Field(ge=1, le=512)]] | Annotated[int, Field(ge=1, le=512)]
    leaf_placement_attempts: Annotated[int, Field(ge=0, le=256)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::RandomSpreadFoliagePlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "foliage_height",
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
                                "max": 512
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "leaf_placement_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 256
                    }
                }
            }
        ]
    }
}

