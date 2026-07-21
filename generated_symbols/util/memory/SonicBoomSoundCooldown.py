# Generated from symbols.json for ::java::util::memory::SonicBoomSoundCooldown
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class SonicBoomSoundCooldown(ExpirableValue):
    value: Any  # If present, the warden's sonic boom animation will not spawn particles and play sounds.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SonicBoomSoundCooldown": {
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
                "desc": "If present, the warden's sonic boom animation will not spawn particles and play sounds.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

