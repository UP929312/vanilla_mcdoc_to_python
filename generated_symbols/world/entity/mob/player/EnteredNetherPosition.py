# Generated from symbols.json for ::java::world::entity::mob::player::EnteredNetherPosition
from dataclasses import dataclass


@dataclass(kw_only=True)
class EnteredNetherPosition:
    x: float | None = None
    y: float | None = None
    z: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::EnteredNetherPosition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "x",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "y",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "z",
                "type": {
                    "kind": "double"
                },
                "optional": True
            }
        ]
    }
}

