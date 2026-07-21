# Generated from symbols.json for ::java::world::entity::item::Uuid
from dataclasses import dataclass


@dataclass(kw_only=True)
class Uuid:
    L: int | None = None  # Lower bits of the target player's UUID
    M: int | None = None  # Upper bits of the target player's UUID


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::item::Uuid": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Lower bits of the target player's UUID",
                "key": "L",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Upper bits of the target player's UUID",
                "key": "M",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

