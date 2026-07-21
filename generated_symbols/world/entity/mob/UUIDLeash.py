# Generated from symbols.json for ::java::world::entity::mob::UUIDLeash
from dataclasses import dataclass


@dataclass(kw_only=True)
class UUIDLeash:
    UUIDMost: int | None = None  # Upper bits of the other entity's UUID.
    UUIDLeast: int | None = None  # Lower bits of the other entity's UUID.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::UUIDLeash": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Upper bits of the other entity's UUID.",
                "key": "UUIDMost",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Lower bits of the other entity's UUID.",
                "key": "UUIDLeast",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

