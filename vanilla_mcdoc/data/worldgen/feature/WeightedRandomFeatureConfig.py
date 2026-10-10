"""
Generated from symbols.json for ::java::data::worldgen::feature::WeightedRandomFeatureConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/WeightedRandomFeatureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from vanilla_mcdoc.util.WeightedList import WeightedList


class WeightedRandomFeatureConfig(GeneratedModel):
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
