"""
Generated from symbols.json for ::java::util::memory::TouchCooldown
Local link to file: generated_symbols/util/memory/TouchCooldown.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


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

