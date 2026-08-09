# Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRule
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class MaterialRuleUnknown:
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
class MaterialRuleSequence:
    type: Literal['minecraft:sequence']
    sequence: list[MaterialRuleRef]


type MaterialRule = MaterialRuleUnknown | MaterialRuleBlock | MaterialRuleCondition | MaterialRuleSequence


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

