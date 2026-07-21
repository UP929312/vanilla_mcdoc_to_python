# Generated from symbols.json for ::java::util::memory::BreezeJumpInhaling
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeJumpInhaling(ExpirableValue):
    value: Any  # If present, the breeze will not long jump or shoot a wind charge when stuck.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeJumpInhaling": {
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
                "desc": "If present, the breeze will not long jump or shoot a wind charge when stuck.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

