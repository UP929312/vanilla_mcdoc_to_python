# Generated from symbols.json for ::java::world::entity::end_crystal::BeamTarget
from dataclasses import dataclass


@dataclass(kw_only=True)
class BeamTarget:
    X: int | None = None
    Y: int | None = None
    Z: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::end_crystal::BeamTarget": {
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

