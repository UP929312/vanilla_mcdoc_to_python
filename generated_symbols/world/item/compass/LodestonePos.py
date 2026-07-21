# Generated from symbols.json for ::java::world::item::compass::LodestonePos
from dataclasses import dataclass


@dataclass(kw_only=True)
class LodestonePos:
    X: int | None = None
    Y: int | None = None
    Z: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::compass::LodestonePos": {
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

