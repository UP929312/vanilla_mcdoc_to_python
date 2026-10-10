"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockIgnore
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/BlockIgnore.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockIgnore(GeneratedModel):
    blocks: list[BlockState]
