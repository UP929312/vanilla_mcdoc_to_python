"""
Generated from symbols.json for ::java::util::memory::LikedNoteblockCooldownTicks
Local link to file: vanilla_mcdoc/util/memory/LikedNoteblockCooldownTicks.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.util.memory.ExpirableValue import ExpirableValue


class LikedNoteblockCooldownTicks(ExpirableValue):
    value: int  # Ticks before the allay stops putting items at the liked note block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LikedNoteblockCooldownTicks": {
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
                "desc": "Ticks before the allay stops putting items at the liked note block.",
                "key": "value",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
