# Generated from symbols.json for ::java::data::worldgen::material_condition::NotCondition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef


@dataclass(kw_only=True)
class NotCondition:
    invert: MaterialConditionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::NotCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "invert",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::material_condition::MaterialConditionRef"
                }
            }
        ]
    }
}

