"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::NoiseThresholdProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/NoiseThresholdProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BaseNoiseProvider import BaseNoiseProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class NoiseThresholdProvider(BaseNoiseProvider):
    threshold: Annotated[float, Field(ge=-1, le=1)]
    high_chance: Annotated[float, Field(ge=0, le=1)]
    default_state: BlockState
    low_states: list[BlockState]
    high_states: list[BlockState]
