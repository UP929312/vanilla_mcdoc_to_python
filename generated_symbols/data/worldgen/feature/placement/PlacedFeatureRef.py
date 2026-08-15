"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeatureRef
Local link to file: generated_symbols/data/worldgen/feature/placement/PlacedFeatureRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacedFeature import PlacedFeature


type PlacedFeatureRef = PlacedFeature | Annotated[str, IdSpec(registry='worldgen/placed_feature')]


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

