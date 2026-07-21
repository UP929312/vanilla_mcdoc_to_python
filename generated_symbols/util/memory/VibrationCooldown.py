# Generated from symbols.json for ::java::util::memory::VibrationCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class VibrationCooldown(ExpirableValue):
    value: Any  # If present, the warden will not react to vibrations. Set to 40 when receiving a vibration.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::VibrationCooldown": {
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
                "desc": "If present, the warden will not react to vibrations. Set to 40 when receiving a vibration.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

