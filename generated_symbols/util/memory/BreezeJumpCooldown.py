# Generated from symbols.json for ::java::util::memory::BreezeJumpCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeJumpCooldown(ExpirableValue):
    value: Any  # If present, the breeze will not long jump or slide. Set after performing a long jump.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeJumpCooldown": {
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
                "desc": "If present, the breeze will not long jump or slide. Set after performing a long jump.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

