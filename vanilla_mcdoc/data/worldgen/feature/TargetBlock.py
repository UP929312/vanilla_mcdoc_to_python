"""
Generated from symbols.json for ::java::data::worldgen::feature::TargetBlock
Local link to file: vanilla_mcdoc/data/worldgen/feature/TargetBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.RuleTest import RuleTest
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class TargetBlock(GeneratedModel):
    target: RuleTest
    state: BlockState
