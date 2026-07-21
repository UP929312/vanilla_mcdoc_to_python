# Generated from symbols.json for ::java::util::memory::IsInWater
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class IsInWater(ExpirableValue):
    value: Any  # Whether the frog is currently in water.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsInWater": {
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
                "desc": "Whether the frog is currently in water.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

