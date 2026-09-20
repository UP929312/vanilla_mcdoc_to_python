"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomBooleanSelector
Local link to file: generated_symbols/data/worldgen/feature/RandomBooleanSelector.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


class RandomBooleanSelector(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    feature_false: FeatureRef
    feature_true: FeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RandomBooleanSelector": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "feature_False",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            },
            {
                "kind": "pair",
                "key": "feature_True",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

