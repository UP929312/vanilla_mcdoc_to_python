"""
Generated from symbols.json for ::java::data::worldgen::material_condition::NotCondition
Local link to file: generated_symbols/data/worldgen/material_condition/NotCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialConditionRef import MaterialConditionRef


class NotCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

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

