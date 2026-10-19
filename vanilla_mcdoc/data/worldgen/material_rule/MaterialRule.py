"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRule
Local link to file: vanilla_mcdoc/data/worldgen/material_rule/MaterialRule.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.material_rule.BlockRule import BlockRule
from vanilla_mcdoc.data.worldgen.material_rule.ConditionRule import ConditionRule
from vanilla_mcdoc.data.worldgen.material_rule.OreVeinifier import OreVeinifier
from vanilla_mcdoc.data.worldgen.material_rule.SequenceRule import SequenceRule


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


class MaterialRuleBandlands(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Literal['minecraft:bandlands', 'bandlands'] = 'minecraft:bandlands'


type MaterialRule = Annotated[
    Annotated[MaterialRuleBlock, Tag('minecraft:block')]
    | Annotated[MaterialRuleCondition, Tag('minecraft:condition')]
    | Annotated[MaterialRuleOreVein, Tag('minecraft:ore_vein')]
    | Annotated[MaterialRuleSequence, Tag('minecraft:sequence')]
    | Annotated[MaterialRuleBandlands, Tag('minecraft:bandlands')],
    Discriminator(tag_of('type')),
]
