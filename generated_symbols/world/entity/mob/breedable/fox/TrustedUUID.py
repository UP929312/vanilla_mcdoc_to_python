# Generated from symbols.json for ::java::world::entity::mob::breedable::fox::TrustedUUID
from dataclasses import dataclass


@dataclass(kw_only=True)
class TrustedUUID:
    L: int | None = None  # Lower bits of the trusted player's UUID.
    M: int | None = None  # Upper bits of the trusted player's UUID.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::fox::TrustedUUID": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Lower bits of the trusted player's UUID.",
                "key": "L",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Upper bits of the trusted player's UUID.",
                "key": "M",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

