# Generated from symbols.json for ::java::data::worldgen::feature::WeightedRandomFeatureConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.util.WeightedList import WeightedList


@dataclass(kw_only=True)
class WeightedRandomFeatureConfig:
    features: WeightedList[PlacedFeatureRef]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::WeightedRandomFeatureConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "features",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::WeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef"
                        }
                    ]
                }
            }
        ]
    }
}

