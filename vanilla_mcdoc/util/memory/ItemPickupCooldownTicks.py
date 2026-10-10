"""
Generated from symbols.json for ::java::util::memory::ItemPickupCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/ItemPickupCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class ItemPickupCooldownTicks(ExpirableValue):
    value: int  # Ticks before the allay goes to pick up an item again.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::ItemPickupCooldownTicks": {
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
                "desc": "Ticks before the allay goes to pick up an item again.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
