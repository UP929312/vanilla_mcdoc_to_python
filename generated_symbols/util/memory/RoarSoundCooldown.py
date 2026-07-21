# Generated from symbols.json for ::java::util::memory::RoarSoundCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class RoarSoundCooldown(ExpirableValue):
    value: Any  # If present, the warden doesn't roar.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::RoarSoundCooldown": {
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
                "desc": "If present, the warden doesn't roar.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

