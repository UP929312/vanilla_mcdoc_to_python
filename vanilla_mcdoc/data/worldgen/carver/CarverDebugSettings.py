"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverDebugSettings
Local link to file: vanilla_mcdoc/data/worldgen/carver/CarverDebugSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class CarverDebugSettings(GeneratedModel):
    debug_mode: bool | None = None
    air_state: BlockState
    water_state: BlockState
    lava_state: BlockState
    barrier_state: BlockState
