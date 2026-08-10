"""
Generated from symbols.json for ::java::data::worldgen::processor_list::PosRuleTest
Local link to file: generated_symbols/data/worldgen/processor_list/PosRuleTest.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.processor_list.LinearPos import LinearPos

if TYPE_CHECKING:
    from generated_symbols.util.direction.Axis import Axis


@dataclass(kw_only=True)
class PosRuleTestAxisAlignedLinearPos(LinearPos):
    predicate_type: Literal['minecraft:axis_aligned_linear_pos']
    axis: Axis


@dataclass(kw_only=True)
class PosRuleTestLinearPos:
    predicate_type: Literal['minecraft:linear_pos']
    min_dist: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None
    max_dist: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None
    min_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None
    max_chance: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


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

