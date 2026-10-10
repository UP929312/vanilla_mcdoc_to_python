"""
Generated from symbols.json for ::java::util::memory::TouchCooldown
Local link to file: vanilla_mcdoc/util/memory/TouchCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class TouchCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not react to being pushed by another mob. Set to 20 when touched.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::TouchCooldown": {
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
                "desc": "If present, the warden will not react to being pushed by another mob. Set to 20 when touched.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
