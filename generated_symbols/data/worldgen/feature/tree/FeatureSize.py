"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FeatureSize
Local link to file: generated_symbols/data/worldgen/feature/tree/FeatureSize.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.feature.tree.ThreeLayersFeatureSize import ThreeLayersFeatureSize
from generated_symbols.data.worldgen.feature.tree.TwoLayersFeatureSize import TwoLayersFeatureSize


@dataclass(kw_only=True)
class FeatureSizeThreeLayersFeatureSize(ThreeLayersFeatureSize):
    type: Literal['minecraft:three_layers_feature_size']


@dataclass(kw_only=True)
class FeatureSizeTwoLayersFeatureSize(TwoLayersFeatureSize):
    type: Literal['minecraft:two_layers_feature_size']


type FeatureSize = FeatureSizeThreeLayersFeatureSize | FeatureSizeTwoLayersFeatureSize


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::FeatureSize": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/feature_size_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:feature_size"
                }
            }
        ]
    }
}

