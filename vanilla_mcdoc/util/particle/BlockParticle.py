"""
Generated from symbols.json for ::java::util::particle::BlockParticle
Local link to file: vanilla_mcdoc/util/particle/BlockParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockParticle(GeneratedModel):
    block_state: BlockState
