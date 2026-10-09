"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRule
Local link to file: generated_symbols/data/worldgen/material_rule/MaterialRule.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.worldgen.material_rule.BlockRule import BlockRule
from generated_symbols.data.worldgen.material_rule.ConditionRule import ConditionRule
from generated_symbols.data.worldgen.material_rule.OreVeinifier import OreVeinifier
from generated_symbols.data.worldgen.material_rule.SequenceRule import SequenceRule
from minecraft_registry import IdSpec


class MaterialRuleUnknown(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Annotated[str, IdSpec(registry='worldgen/material_rule_type')]


class MaterialRuleBlock(BlockRule):
    type: Literal['minecraft:block', 'block'] = 'minecraft:block'


class MaterialRuleCondition(ConditionRule):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'


class MaterialRuleOreVein(OreVeinifier):
    type: Literal['minecraft:ore_vein', 'ore_vein'] = 'minecraft:ore_vein'


class MaterialRuleSequence(SequenceRule):
    type: Literal['minecraft:sequence', 'sequence'] = 'minecraft:sequence'


type MaterialRule = MaterialRuleUnknown | MaterialRuleBlock | MaterialRuleCondition | MaterialRuleOreVein | MaterialRuleSequence


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::MaterialRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_rule"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/material_rule_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:material_rule"
                }
            }
        ]
    }
}

