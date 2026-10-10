"""
Generated from symbols.json for ::java::util::memory::BreezeShoot
Local link to file: generated_symbols/util/memory/BreezeShoot.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class BreezeShoot(ExpirableValue):
    value: ValueStruct  # If present, the breeze is able to shoot a wind charge, and will not long jump or slide.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::BreezeShoot": {
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
                "desc": "If present, the breeze is able to shoot a wind charge, and will not long jump or slide.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
