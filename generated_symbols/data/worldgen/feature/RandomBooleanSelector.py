# Generated from symbols.json for ::java::data::worldgen::feature::RandomBooleanSelector
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class RandomBooleanSelector:
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

