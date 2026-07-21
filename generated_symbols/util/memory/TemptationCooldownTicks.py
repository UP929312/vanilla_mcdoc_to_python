# Generated from symbols.json for ::java::util::memory::TemptationCooldownTicks
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class TemptationCooldownTicks(ExpirableValue):
    value: int  # Ticks before the mob can be tempted again.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::TemptationCooldownTicks": {
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
                "desc": "Ticks before the mob can be tempted again.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

