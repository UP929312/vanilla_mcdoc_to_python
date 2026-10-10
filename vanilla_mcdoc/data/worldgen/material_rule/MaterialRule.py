"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRule
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/MaterialRule.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.material_rule.BlockRule import BlockRule
from vanilla_mcdoc.data.worldgen.material_rule.ConditionRule import ConditionRule
from vanilla_mcdoc.data.worldgen.material_rule.OreVeinifier import OreVeinifier
from vanilla_mcdoc.data.worldgen.material_rule.SequenceRule import SequenceRule
from vanilla_mcdoc.minecraft_types import IdSpec


class MaterialRuleUnknown(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Annotated[str, IdSpec(registry='worldgen/material_rule_type')]


class MaterialRuleBlock(BlockRule):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Literal['minecraft:block', 'block'] = 'minecraft:block'


class MaterialRuleCondition(ConditionRule):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'


class MaterialRuleOreVein(OreVeinifier):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Literal['minecraft:ore_vein', 'ore_vein'] = 'minecraft:ore_vein'


class MaterialRuleSequence(SequenceRule):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Literal['minecraft:sequence', 'sequence'] = 'minecraft:sequence'


type MaterialRule = MaterialRuleUnknown | MaterialRuleBlock | MaterialRuleCondition | MaterialRuleOreVein | MaterialRuleSequence
