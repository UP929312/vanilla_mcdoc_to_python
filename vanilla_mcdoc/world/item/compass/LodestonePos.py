"""
Generated from symbols.json for ::java::world::item::compass::LodestonePos
Local link to file: vanilla_mcdoc/world/item/compass/LodestonePos.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class LodestonePos(GeneratedModel):
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
