# Generated from symbols.json for ::java::world::entity::evoker_fangs::Owner
from dataclasses import dataclass


@dataclass(kw_only=True)
class Owner:
    OwnerUUIDMost: int | None = None  # Upper bits of the owner's UUID.
    OwnerUUIDLeast: int | None = None  # Lower bits of the owner's UUID.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::evoker_fangs::Owner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Upper bits of the owner's UUID.",
                "key": "OwnerUUIDMost",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Lower bits of the owner's UUID.",
                "key": "OwnerUUIDLeast",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

