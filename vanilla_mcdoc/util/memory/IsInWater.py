"""
Generated from symbols.json for ::java::util::memory::IsInWater
Local link to file: vanilla_mcdoc/util/memory/IsInWater.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ValueStruct(GeneratedModel):
    pass


class IsInWater(ExpirableValue):
    value: ValueStruct  # Whether the frog is currently in water.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsInWater": {
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
                "desc": "Whether the frog is currently in water.",
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}
