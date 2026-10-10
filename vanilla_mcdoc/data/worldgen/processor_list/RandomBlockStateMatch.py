"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockStateMatch
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/RandomBlockStateMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class RandomBlockStateMatch(GeneratedModel):
    block_state: BlockState
    probability: Annotated[float, Field(ge=0, le=1)]
