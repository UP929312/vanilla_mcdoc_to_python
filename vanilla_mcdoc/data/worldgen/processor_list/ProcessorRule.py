"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorRule
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/ProcessorRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.BlockEntityModifier import BlockEntityModifier
    from vanilla_mcdoc.data.worldgen.processor_list.PosRuleTest import PosRuleTest
    from vanilla_mcdoc.data.worldgen.processor_list.RuleTest import RuleTest
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class ProcessorRule(GeneratedModel):
    position_predicate: PosRuleTest | None = None
    location_predicate: RuleTest
    input_predicate: RuleTest
    output_state: BlockState
    block_entity_modifier: BlockEntityModifier | None = None
