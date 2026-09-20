"""
Generated from symbols.json for ::java::util::memory::GolemDetectedRecently
Local link to file: generated_symbols/util/memory/GolemDetectedRecently.py
"""
# ~~~ CODE ~~~
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class GolemDetectedRecently(ExpirableValue):
    value: bool  # Whether the villager has detected an iron golem recently.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::GolemDetectedRecently": {
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
                "desc": "Whether the villager has detected an iron golem recently.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

