"""
Generated from symbols.json for ::java::util::memory::BreezeShootCharging
Local link to file: generated_symbols/util/memory/BreezeShootCharging.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeShootCharging(ExpirableValue):
    value: ValueStruct  # If present, the breeze will not shoot a wind charge. Set when starting to shoot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShootCharging": {
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
                "desc": "If present, the breeze will not shoot a wind charge. Set when starting to shoot.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
