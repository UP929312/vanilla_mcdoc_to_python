"""
Generated from symbols.json for ::java::data::worldgen::material_rule::BlockRule
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/BlockRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class BlockRule(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    result_state: BlockState
