# Generated from symbols.json for ::java::util::memory::HasHuntingCooldown
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class HasHuntingCooldown(ExpirableValue):
    value: bool  # Whether the axolotl is in a hunting cooldown.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::HasHuntingCooldown": {
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
                "desc": "Whether the axolotl is in a hunting cooldown.",
                "key": "value",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

