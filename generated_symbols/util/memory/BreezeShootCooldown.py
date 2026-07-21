# Generated from symbols.json for ::java::util::memory::BreezeShootCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeShootCooldown(ExpirableValue):
    value: Any  # If present, the breeze will not shoot a wind charge. Set after shooting


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootCooldown": {
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
                "desc": "If present, the breeze will not shoot a wind charge. Set after shooting",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

