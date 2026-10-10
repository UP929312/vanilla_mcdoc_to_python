"""
Generated from symbols.json for ::java::data::worldgen::material_rule::SequenceRule
Local link to file: generated_symbols/data/worldgen/material_rule/SequenceRule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_rule.MaterialRuleRef import MaterialRuleRef


class SequenceRule(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_rule'

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
