"""
Generated from symbols.json for ::java::data::worldgen::WeightListHeightProvider
Local link to file: generated_symbols/data/worldgen/WeightListHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


class WeightListHeightProvider(GeneratedModel):
    distribution: NonEmptyWeightedList[HeightProvider]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::WeightListHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "distribution",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::NonEmptyWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::HeightProvider"
                        }
                    ]
                }
            }
        ]
    }
}

