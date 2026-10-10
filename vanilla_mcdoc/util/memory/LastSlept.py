"""
Generated from symbols.json for ::java::util::memory::LastSlept
Local link to file: vanilla_mcdoc/util/memory/LastSlept.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


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
