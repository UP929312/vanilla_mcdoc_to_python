# Generated from symbols.json for ::java::util::memory::DangerDetectedRecently
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
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

