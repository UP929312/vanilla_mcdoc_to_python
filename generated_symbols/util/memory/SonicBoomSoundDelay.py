# Generated from symbols.json for ::java::util::memory::SonicBoomSoundDelay
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class SonicBoomSoundDelay(ExpirableValue):
    value: Any  # If present, will delay the warden's sonic boom animation.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SonicBoomSoundDelay": {
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
                "desc": "If present, will delay the warden's sonic boom animation.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

