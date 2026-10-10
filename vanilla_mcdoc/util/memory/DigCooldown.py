"""
Generated from symbols.json for ::java::util::memory::DigCooldown
Local link to file: vanilla_mcdoc/util/memory/DigCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class DigCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not dig down.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::DigCooldown": {
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
                "desc": "If present, the warden will not dig down.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
