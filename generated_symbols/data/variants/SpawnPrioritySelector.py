# Generated from symbols.json for ::java::data::variants::SpawnPrioritySelector
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.variants.SpawnCondition import SpawnCondition


@dataclass(kw_only=True)
class SpawnPrioritySelector:
    priority: int  # The spawn priority to use.
    condition: SpawnCondition | None = None  # The spawn condition to check. If not present, the condition always matches.


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

