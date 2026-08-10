"""
Generated from symbols.json for ::java::data::worldgen::feature::OverlayConfig
Local link to file: generated_symbols/data/worldgen/feature/OverlayConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef


@dataclass(kw_only=True)
class OverlayConfig:
    features: PlacedFeatureListRef  # The features to generate, in order.  All features are placed regardless of individual placement success.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::OverlayConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The features to generate, in order. \\\nAll features are placed regardless of individual placement success.",
                "key": "features",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::placement::PlacedFeatureListRef"
                }
            }
        ]
    }
}

