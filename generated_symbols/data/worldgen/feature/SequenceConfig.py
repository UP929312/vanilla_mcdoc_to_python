"""
Generated from symbols.json for ::java::data::worldgen::feature::SequenceConfig
Local link to file: generated_symbols/data/worldgen/feature/SequenceConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef


@dataclass(kw_only=True)
class SequenceConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: PlacedFeatureListRef  # The features to generate, in order.  If any feature in the list is not placed, the following features will also be skipped.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SequenceConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The features to generate, in order. \\\nIf any feature in the list is not placed, the following features will also be skipped.",
                "key": "features",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::placement::PlacedFeatureListRef"
                }
            }
        ]
    }
}

