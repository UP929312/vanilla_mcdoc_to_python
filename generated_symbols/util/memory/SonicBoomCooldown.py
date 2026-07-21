# Generated from symbols.json for ::java::util::memory::SonicBoomCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class SonicBoomCooldown(ExpirableValue):
    value: Any  # If present, the warden will not use the sonic boom attack.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SonicBoomCooldown": {
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
                "desc": "If present, the warden will not use the sonic boom attack.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

