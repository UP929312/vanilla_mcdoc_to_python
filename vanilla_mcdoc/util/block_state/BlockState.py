"""
Generated from symbols.json for ::java::util::block_state::BlockState
Local link to file: vanilla_mcdoc/util/block_state/BlockState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.util.block_state.FullBlockState import FullBlockState


type BlockState = Annotated[str, IdSpec(registry='block')] | KnownBlockId | FullBlockState
