# Generated from symbols.json for ::java::util::memory::LongJumpCoolingDown
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class LongJumpCoolingDown(ExpirableValue):
    value: int  # Ticks before the goat can long jump again.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LongJumpCoolingDown": {
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
                "desc": "Ticks before the goat can long jump again.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

