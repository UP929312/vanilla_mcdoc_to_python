"""
Generated from symbols.json for ::java::data::worldgen::feature::ForestRockConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/ForestRockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class ForestRockConfig(GeneratedModel):
    state: BlockState
