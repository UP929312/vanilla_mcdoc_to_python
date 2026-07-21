# Generated from symbols.json for ::java::util::memory::LastWorkedAtPoi
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class LastWorkedAtPoi(ExpirableValue):
    value: int  # The gametime tick that the villager last worked at their job site.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LastWorkedAtPoi": {
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
                "desc": "The gametime tick that the villager last worked at their job site.",
                "key": "value",
                "type": {
                    "kind": "long"
                }
            }
        ]
    }
}

