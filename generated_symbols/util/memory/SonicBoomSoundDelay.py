"""
Generated from symbols.json for ::java::util::memory::SonicBoomSoundDelay
Local link to file: generated_symbols/util/memory/SonicBoomSoundDelay.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SonicBoomSoundDelay(ExpirableValue):
    value: ValueStruct  # If present, will delay the warden's sonic boom animation.


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

