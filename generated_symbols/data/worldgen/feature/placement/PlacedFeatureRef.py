# Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeatureRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeature import PlacedFeature


type PlacedFeatureRef = PlacedFeature | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::PlacedFeatureRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::feature::placement::PlacedFeature"
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/placed_feature"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

