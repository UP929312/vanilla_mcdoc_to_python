"""
Generated from symbols.json for ::java::util::memory::AdmiringItem
Local link to file: vanilla_mcdoc/util/memory/AdmiringItem.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class AdmiringItem(ExpirableValue):
    value: bool  # Whether the piglin is currently admiring an item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::AdmiringItem": {
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
                "desc": "Whether the piglin is currently admiring an item.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
