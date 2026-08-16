"""
Generated from symbols.json for ::java::data::worldgen::feature::RandomSelector
Local link to file: generated_symbols/data/worldgen/feature/RandomSelector.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class FeaturesStruct:
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    feature: FeatureRef


@dataclass(kw_only=True)
class RandomSelector:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: list[FeaturesStruct]
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

