# Generated from symbols.json for ::java::data::worldgen::material_rule::ConditionRule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef


@dataclass(kw_only=True)
class ConditionRule:
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

