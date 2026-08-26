"""
Generated from symbols.json for ::java::data::worldgen::processor_list::PosRuleTest
Local link to file: generated_symbols/data/worldgen/processor_list/PosRuleTest.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.processor_list.AxisAlignedLinearPos import AxisAlignedLinearPos
from generated_symbols.data.worldgen.processor_list.LinearPos import LinearPos


@dataclass(kw_only=True)
class PosRuleTestAxisAlignedLinearPos(AxisAlignedLinearPos):
    predicate_type: Literal['minecraft:axis_aligned_linear_pos']


@dataclass(kw_only=True)
class PosRuleTestLinearPos(LinearPos):
    predicate_type: Literal['minecraft:linear_pos']


type PosRuleTest = PosRuleTestAxisAlignedLinearPos | PosRuleTestLinearPos


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::PosRuleTest": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "pos_rule_test"
                                }
                            }
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
                                "predicate_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:pos_rule_test"
                }
            }
        ]
    }
}

