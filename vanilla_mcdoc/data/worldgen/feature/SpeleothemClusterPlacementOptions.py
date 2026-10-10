"""
Generated from symbols.json for ::java::data::worldgen::feature::SpeleothemClusterPlacementOptions
Local link to file: vanilla_mcdoc/data/worldgen/feature/SpeleothemClusterPlacementOptions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.SpeleothemBaseBlockTransformer import SpeleothemBaseBlockTransformer
    from vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementMode import SpeleothemClusterPlacementMode


class SpeleothemClusterPlacementOptions(GeneratedModel):
    placement_mode: SpeleothemClusterPlacementMode
    base_block_transformer: SpeleothemBaseBlockTransformer
    allow_water_placement: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SpeleothemClusterPlacementOptions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "placement_mode",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::SpeleothemClusterPlacementMode"
                }
            },
            {
                "kind": "pair",
                "key": "base_block_transformer",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::SpeleothemBaseBlockTransformer"
                }
            },
            {
                "kind": "pair",
                "key": "allow_water_placement",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
