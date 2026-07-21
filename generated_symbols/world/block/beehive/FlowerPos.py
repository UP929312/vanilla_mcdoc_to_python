# Generated from symbols.json for ::java::world::block::beehive::FlowerPos
from dataclasses import dataclass


@dataclass(kw_only=True)
class FlowerPos:
    X: int | None = None
    Y: int | None = None
    Z: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::beehive::FlowerPos": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "X",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Y",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Z",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

