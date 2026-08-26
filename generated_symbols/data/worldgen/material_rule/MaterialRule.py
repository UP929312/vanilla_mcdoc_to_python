"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRule
Local link to file: generated_symbols/data/worldgen/material_rule/MaterialRule.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class MaterialRuleUnknown:
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    type: Annotated[str, IdSpec(registry='worldgen/material_rule_type')]


@dataclass(kw_only=True)
class MaterialRuleBlock:
    type: Literal['minecraft:block']
    result_state: BlockState


@dataclass(kw_only=True)
class MaterialRuleCondition:
    type: Literal['minecraft:condition']
    if_true: MaterialConditionRef
    then_run: MaterialRuleRef


@dataclass(kw_only=True)
class MaterialRuleOreVein:
    type: Literal['minecraft:ore_vein']
    ore_block: BlockState
    raw_ore_block: BlockState
    filler_block: BlockState
    raw_ore_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    density: DensityFunctionRef
    richness: DensityFunctionRef
    filler_gap: DensityFunctionRef


@dataclass(kw_only=True)
class MaterialRuleSequence:
    type: Literal['minecraft:sequence']
    sequence: list[MaterialRuleRef]


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

