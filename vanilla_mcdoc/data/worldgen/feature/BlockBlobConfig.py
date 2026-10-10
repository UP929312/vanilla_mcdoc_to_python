"""
Generated from symbols.json for ::java::data::worldgen::feature::BlockBlobConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/BlockBlobConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockBlobConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    can_place_on: BlockPredicate
