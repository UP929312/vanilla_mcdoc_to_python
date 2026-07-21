# Generated from symbols.json for ::java::util::memory::BreezeShootRecover
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeShootRecover(ExpirableValue):
    value: Any  # If present, the breeze will not shoot a wind charge.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootRecover": {
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
                "desc": "If present, the breeze will not shoot a wind charge.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

