"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::NoiseProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/NoiseProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class NoiseProvider(BaseNoiseProvider):
    states: list[BlockState]
