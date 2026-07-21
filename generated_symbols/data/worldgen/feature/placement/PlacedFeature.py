# Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeature
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.ConfiguredFeatureRef import ConfiguredFeatureRef
    from generated_symbols.data.worldgen.feature.placement.PlacementModifier import PlacementModifier


@dataclass(kw_only=True)
class PlacedFeature:
    feature: ConfiguredFeatureRef
    placement: list[PlacementModifier]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::PlacedFeature": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::ConfiguredFeatureRef"
                }
            },
            {
                "kind": "pair",
                "key": "placement",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::placement::PlacementModifier"
                    }
                }
            }
        ]
    }
}

