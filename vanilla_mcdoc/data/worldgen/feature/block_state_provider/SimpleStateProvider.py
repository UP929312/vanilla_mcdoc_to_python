"""
Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::SimpleStateProvider
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_state_provider/SimpleStateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class SimpleStateProvider(GeneratedModel):
    state: BlockState
