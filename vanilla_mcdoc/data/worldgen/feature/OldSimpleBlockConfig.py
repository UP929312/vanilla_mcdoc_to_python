"""
Generated from symbols.json for ::java::data::worldgen::feature::OldSimpleBlockConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/OldSimpleBlockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class OldSimpleBlockConfig(GeneratedModel):
    place_on: list[BlockState]
    place_in: list[BlockState]
    place_under: list[BlockState]
