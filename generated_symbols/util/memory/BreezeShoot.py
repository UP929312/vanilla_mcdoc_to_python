# Generated from symbols.json for ::java::util::memory::BreezeShoot
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class BreezeShoot(ExpirableValue):
    value: Any  # If present, the breeze is able to shoot a wind charge, and will not long jump or slide.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShoot": {
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
                "desc": "If present, the breeze is able to shoot a wind charge, and will not long jump or slide.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

