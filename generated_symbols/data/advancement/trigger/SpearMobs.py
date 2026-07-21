# Generated from symbols.json for ::java::data::advancement::trigger::SpearMobs
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase


@dataclass(kw_only=True)
class SpearMobs(TriggerBase):
    count: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::SpearMobs": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
                }
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

