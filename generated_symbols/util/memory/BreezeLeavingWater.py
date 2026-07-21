# Generated from symbols.json for ::java::util::memory::BreezeLeavingWater
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeLeavingWater(ExpirableValue):
    value: Any  # If present, the breeze is in water.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeLeavingWater": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::ExpirableValue"
                }
            },
            {
                "kind": "pair",
                "desc": "If present, the breeze is in water.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

