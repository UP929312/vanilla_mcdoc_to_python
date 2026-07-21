# Generated from symbols.json for ::java::data::worldgen::WeightListHeightProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class WeightListHeightProvider:
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

