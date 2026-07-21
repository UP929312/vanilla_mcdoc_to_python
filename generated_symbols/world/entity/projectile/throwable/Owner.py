# Generated from symbols.json for ::java::world::entity::projectile::throwable::Owner
from dataclasses import dataclass


@dataclass(kw_only=True)
class Owner:
    M: int | None = None  # Upper bits of the owner's UUID.
    L: int | None = None  # Lower bits of the owner's UUID.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::projectile::throwable::Owner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Upper bits of the owner's UUID.",
                "key": "M",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Lower bits of the owner's UUID.",
                "key": "L",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

