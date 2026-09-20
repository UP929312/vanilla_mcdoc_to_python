"""
Generated from symbols.json for ::java::util::memory::AttackTargetCooldown
Local link to file: generated_symbols/util/memory/AttackTargetCooldown.py
"""
# ~~~ CODE ~~~
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class AttackTargetCooldown(ExpirableValue):
    value: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::AttackTargetCooldown": {
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

