"""
Generated from symbols.json for ::java::data::worldgen::material_rule::SequenceRule
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/SequenceRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef


class SequenceRule(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    sequence: list[MaterialRuleRef]
