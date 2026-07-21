# Generated from symbols.json for ::java::util::memory::TouchCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class TouchCooldown(ExpirableValue):
    value: Any  # If present, the warden will not react to being pushed by another mob. Set to 20 when touched.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::TouchCooldown": {
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
                "desc": "If present, the warden will not react to being pushed by another mob. Set to 20 when touched.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

