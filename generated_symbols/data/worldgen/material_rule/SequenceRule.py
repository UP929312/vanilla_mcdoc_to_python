# Generated from symbols.json for ::java::data::worldgen::material_rule::SequenceRule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef


@dataclass(kw_only=True)
class SequenceRule:
    sequence: list[MaterialRuleRef]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::SequenceRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sequence",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::material_rule::MaterialRuleRef"
                    }
                }
            }
        ]
    }
}

