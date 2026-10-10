"""
Generated from symbols.json for ::java::data::structure::RandomizedPalette
Local link to file: vanilla_mcdoc/data/structure/RandomizedPalette.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class RandomizedPalette(GeneratedModel):
    palettes: list[list[BlockState]]  # Sets of different block states used in the structure, a random palette gets selected based on coordinates.
