"""
Generated from symbols.json for ::java::util::memory::RoarSoundDelay
Local link to file: generated_symbols/util/memory/RoarSoundDelay.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class RoarSoundDelay(ExpirableValue):
    value: ValueStruct  # If present, the warden doesn't roar.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::RoarSoundDelay": {
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
