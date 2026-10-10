"""
Generated from symbols.json for ::java::data::worldgen::feature::SpikeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SpikeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class SpikeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    can_place_on: BlockPredicate
    can_replace: BlockPredicate
