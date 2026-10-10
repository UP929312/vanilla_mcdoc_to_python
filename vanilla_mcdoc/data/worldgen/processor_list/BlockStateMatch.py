"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockStateMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/BlockStateMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockStateMatch(GeneratedModel):
    block_state: BlockState
