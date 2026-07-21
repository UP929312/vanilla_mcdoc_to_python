# Generated from symbols.json for ::java::util::memory::IsTempted
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class IsTempted(ExpirableValue):
    value: bool  # Whether the mob is currently tempted by a player.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::IsTempted": {
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
                "desc": "Whether the mob is currently tempted by a player.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

