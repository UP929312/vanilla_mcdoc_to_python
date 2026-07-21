# Generated from symbols.json for ::java::data::worldgen::feature::RandomSelector
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class RandomSelector:
    features: list[Any]
    default: FeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RandomSelector": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "features",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "chance",
                                "type": {
                                    "kind": "float",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 1
                                    }
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "feature",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::data::worldgen::feature::FeatureRef"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

