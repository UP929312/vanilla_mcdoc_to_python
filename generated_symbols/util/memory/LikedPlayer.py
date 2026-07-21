# Generated from symbols.json for ::java::util::memory::LikedPlayer
from dataclasses import dataclass
from generated_symbols.util.memory.ExpirableValue import ExpirableValue


@dataclass(kw_only=True)
class LikedPlayer(ExpirableValue):
    value: tuple[int, int, int, int]  # The UUID of the player entity that the allay likes.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LikedPlayer": {
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
                "desc": "The UUID of the player entity that the allay likes.",
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

