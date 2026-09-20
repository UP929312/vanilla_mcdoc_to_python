"""
Generated from symbols.json for ::java::util::memory::ChargeCooldownTicks
Local link to file: generated_symbols/util/memory/ChargeCooldownTicks.py
"""
# ~~~ CODE ~~~
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class ChargeCooldownTicks(ExpirableValue):
    value: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::ChargeCooldownTicks": {
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
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

