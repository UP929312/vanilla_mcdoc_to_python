"""
Generated from symbols.json for ::java::util::memory::BreezeJumpInhaling
Local link to file: vanilla_mcdoc/util/memory/BreezeJumpInhaling.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeJumpInhaling(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not long jump or shoot a wind charge when stuck.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeJumpInhaling": {
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
                "desc": "If present, the breeze will not long jump or shoot a wind charge when stuck.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
