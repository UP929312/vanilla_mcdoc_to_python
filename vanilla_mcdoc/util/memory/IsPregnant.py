"""
Generated from symbols.json for ::java::util::memory::IsPregnant
Local link to file: generated_symbols/util/memory/IsPregnant.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class IsPregnant(ExpirableValue):
    value: ValueStruct  # Whether the frog is pregnant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsPregnant": {
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
                "desc": "Whether the frog is pregnant.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
