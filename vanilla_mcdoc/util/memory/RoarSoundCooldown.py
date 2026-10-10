"""
Generated from symbols.json for ::java::util::memory::RoarSoundCooldown
Local link to file: vanilla_mcdoc/util/memory/RoarSoundCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class RoarSoundCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden doesn't roar.


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
