"""
Generated from symbols.json for ::java::data::worldgen::feature::WeightedRandomFeatureConfig
Local link to file: generated_symbols/data/worldgen/feature/WeightedRandomFeatureConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.util.WeightedList import WeightedList


@dataclass(kw_only=True)
class WeightedRandomFeatureConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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

