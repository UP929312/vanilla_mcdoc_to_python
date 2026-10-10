"""
Generated from symbols.json for ::java::data::variants::SpawnPrioritySelector
Local link to file: vanilla_mcdoc/data/variants/SpawnPrioritySelector.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.SpawnCondition import SpawnCondition


class SpawnPrioritySelector(GeneratedModel):
    condition: SpawnCondition | None = None  # The spawn condition to check. If not present, the condition always matches.
    priority: int  # The spawn priority to use.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SpawnPrioritySelector": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The spawn condition to check. If not present, the condition always matches.",
                "key": "condition",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::SpawnCondition"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The spawn priority to use.",
                "key": "priority",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
