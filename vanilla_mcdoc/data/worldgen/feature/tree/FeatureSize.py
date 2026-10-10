"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FeatureSize
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/FeatureSize.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.tree.ThreeLayersFeatureSize import ThreeLayersFeatureSize
from vanilla_mcdoc.data.worldgen.feature.tree.TwoLayersFeatureSize import TwoLayersFeatureSize


class FeatureSizeThreeLayersFeatureSize(ThreeLayersFeatureSize):
    type: Literal['minecraft:three_layers_feature_size', 'three_layers_feature_size'] = 'minecraft:three_layers_feature_size'


class FeatureSizeTwoLayersFeatureSize(TwoLayersFeatureSize):
    type: Literal['minecraft:two_layers_feature_size', 'two_layers_feature_size'] = 'minecraft:two_layers_feature_size'


type FeatureSize = Annotated[
    FeatureSizeThreeLayersFeatureSize | FeatureSizeTwoLayersFeatureSize,
    Field(discriminator='type'),
]


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
