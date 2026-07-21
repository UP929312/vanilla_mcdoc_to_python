# Generated from symbols.json for ::java::util::memory::ItemPickupCooldownTicks
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
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

