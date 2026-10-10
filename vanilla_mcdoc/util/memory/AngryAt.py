"""
Generated from symbols.json for ::java::util::memory::AngryAt
Local link to file: generated_symbols/util/memory/AngryAt.py
"""
# ~~~ CODE ~~~
from generated_symbols.minecraft_types import MinecraftUUID
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


class AngryAt(ExpirableValue):
    value: MinecraftUUID  # The target of the piglin or piglin brute.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::AngryAt": {
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
                "desc": "The target of the piglin or piglin brute.",
                "key": "value",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                }
            }
        ]
    }
}
