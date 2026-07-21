# Generated from symbols.json for ::java::util::memory::LastSlept
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class LastSlept(ExpirableValue):
    value: int  # The gametime tick that the villager last slept in a bed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LastSlept": {
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
                "desc": "The gametime tick that the villager last slept in a bed.",
                "key": "value",
                "type": {
                    "kind": "long"
                }
            }
        ]
    }
}

