"""
Generated from symbols.json for ::java::data::structure::BlockPalette
Local link to file: vanilla_mcdoc/data/structure/BlockPalette.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockPaletteStruct1(GeneratedModel):
    palette: list[BlockState]


class BlockPaletteStruct2(GeneratedModel):
    palettes: list[list[BlockState]]  # Sets of different block states used in the structure, a random palette gets selected based on coordinates.


type BlockPalette = BlockPaletteStruct1 | BlockPaletteStruct2
