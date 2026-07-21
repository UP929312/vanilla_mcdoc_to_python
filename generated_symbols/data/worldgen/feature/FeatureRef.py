# Generated from symbols.json for ::java::data::worldgen::feature::FeatureRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


type FeatureRef = PlacedFeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::FeatureRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::feature::ConfiguredFeatureRef",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

