"""
Generated from symbols.json for ::java::util::memory::SonicBoomCooldown
Local link to file: generated_symbols/util/memory/SonicBoomCooldown.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class SonicBoomCooldown(ExpirableValue):
    value: ValueStruct  # If present, the warden will not use the sonic boom attack.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::SonicBoomCooldown": {
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
                "desc": "If present, the warden will not use the sonic boom attack.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

