# Generated from symbols.json for ::java::util::memory::UniversalAnger
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class UniversalAnger(ExpirableValue):
    value: bool  # Whether the piglin is being universally angered. Only used when the `universalAnger` gamerule is enabled.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::UniversalAnger": {
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
                "desc": "Whether the piglin is being universally angered. Only used when the `universalAnger` gamerule is enabled.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

