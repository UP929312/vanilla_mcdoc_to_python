"""
Generated from symbols.json for ::java::util::memory::HasHuntingCooldown
Local link to file: vanilla_mcdoc/util/memory/HasHuntingCooldown.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


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
