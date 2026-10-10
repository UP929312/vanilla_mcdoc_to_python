"""
Generated from symbols.json for ::java::util::memory::RamCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/RamCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class RamCooldownTicks(ExpirableValue):
    value: int  # Ticks before the goat can ram again.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::RamCooldownTicks": {
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
                "desc": "Ticks before the goat can ram again.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
