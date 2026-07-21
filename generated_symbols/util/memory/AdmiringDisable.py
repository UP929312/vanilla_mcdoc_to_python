# Generated from symbols.json for ::java::util::memory::AdmiringDisable
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class AdmiringDisable(ExpirableValue):
    value: bool  # Whether the piglin cannot admire an item. Set when converting, when attacked, or when admiring an item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::AdmiringDisable": {
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
                "desc": "Whether the piglin cannot admire an item.\nSet when converting, when attacked, or when admiring an item.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

