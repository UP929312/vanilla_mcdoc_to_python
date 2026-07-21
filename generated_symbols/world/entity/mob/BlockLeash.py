# Generated from symbols.json for ::java::world::entity::mob::BlockLeash
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockLeash:
    X: int | None = None  # X coordiante of leash knot.
    Y: int | None = None  # Y coordiante of leash knot.
    Z: int | None = None  # Z coordiante of leash knot.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::BlockLeash": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "X coordiante of leash knot.",
                "key": "X",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Y coordiante of leash knot.",
                "key": "Y",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Z coordiante of leash knot.",
                "key": "Z",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

