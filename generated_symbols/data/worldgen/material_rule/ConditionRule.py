"""
Generated from symbols.json for ::java::data::worldgen::material_rule::ConditionRule
Local link to file: generated_symbols/data/worldgen/material_rule/ConditionRule.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef


@dataclass(kw_only=True)
class ConditionRule:
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

    if_true: MaterialConditionRef
    then_run: MaterialRuleRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::ConditionRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "if_True",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::material_condition::MaterialConditionRef"
                }
            },
            {
                "kind": "pair",
                "key": "then_run",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::material_rule::MaterialRuleRef"
                }
            }
        ]
    }
}

