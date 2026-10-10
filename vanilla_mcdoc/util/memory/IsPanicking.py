"""
Generated from symbols.json for ::java::util::memory::IsPanicking
Local link to file: vanilla_mcdoc/util/memory/IsPanicking.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class IsPanicking(ExpirableValue):
    value: bool  # Whether the mob is currently panicking.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsPanicking": {
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
                "desc": "Whether the mob is currently panicking.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
