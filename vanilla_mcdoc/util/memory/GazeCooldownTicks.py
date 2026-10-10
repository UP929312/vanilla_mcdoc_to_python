"""
Generated from symbols.json for ::java::util::memory::GazeCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/GazeCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class GazeCooldownTicks(ExpirableValue):
    value: int  # Ticks before the armadillo or camel can randomly look around again.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::GazeCooldownTicks": {
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
                "desc": "Ticks before the armadillo or camel can randomly look around again.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
