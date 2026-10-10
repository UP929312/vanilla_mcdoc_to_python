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
