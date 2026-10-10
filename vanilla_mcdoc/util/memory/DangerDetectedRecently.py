"""
Generated from symbols.json for ::java::util::memory::DangerDetectedRecently
Local link to file: vanilla_mcdoc/util/memory/DangerDetectedRecently.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class DangerDetectedRecently(ExpirableValue):
    value: bool  # Whether the armadillo has detected danger recently.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::DangerDetectedRecently": {
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
                "desc": "Whether the armadillo has detected danger recently.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}
