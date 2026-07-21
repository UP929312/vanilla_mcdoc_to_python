# Generated from symbols.json for ::java::util::memory::HuntedRecently
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class HuntedRecently(ExpirableValue):
    value: bool  # Whether the piglin just hunted recently. Set after hunting or spawning in a bastion remnant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::HuntedRecently": {
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
                "desc": "Whether the piglin just hunted recently.\nSet after hunting or spawning in a bastion remnant.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

