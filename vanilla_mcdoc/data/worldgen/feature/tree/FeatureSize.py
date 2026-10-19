"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::FeatureSize
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/FeatureSize.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.worldgen.feature.tree.ThreeLayersFeatureSize import ThreeLayersFeatureSize
from vanilla_mcdoc.data.worldgen.feature.tree.TwoLayersFeatureSize import TwoLayersFeatureSize


class FeatureSizeThreeLayersFeatureSize(ThreeLayersFeatureSize):
    type: Literal['minecraft:three_layers_feature_size', 'three_layers_feature_size'] = 'minecraft:three_layers_feature_size'


class FeatureSizeTwoLayersFeatureSize(TwoLayersFeatureSize):
    type: Literal['minecraft:two_layers_feature_size', 'two_layers_feature_size'] = 'minecraft:two_layers_feature_size'


type FeatureSize = Annotated[
    Annotated[FeatureSizeThreeLayersFeatureSize, Tag('minecraft:three_layers_feature_size')]
    | Annotated[FeatureSizeTwoLayersFeatureSize, Tag('minecraft:two_layers_feature_size')],
    Discriminator(tag_of('type')),
]
