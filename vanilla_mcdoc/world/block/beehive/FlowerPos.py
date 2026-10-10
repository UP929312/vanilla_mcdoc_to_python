"""
Generated from symbols.json for ::java::world::block::beehive::FlowerPos
Local link to file: vanilla_mcdoc/world/block/beehive/FlowerPos.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class FlowerPos(GeneratedModel):
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
