"""
Generated from symbols.json for ::java::data::worldgen::feature::HugeFungusConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/HugeFungusConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class HugeFungusConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    hat_state: BlockState
    decor_state: BlockState
    stem_state: BlockState
    valid_base_block: BlockState
    planted: bool | None = None
    replaceable_blocks: BlockPredicate
