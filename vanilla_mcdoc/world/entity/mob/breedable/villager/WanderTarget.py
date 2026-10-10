"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::WanderTarget
Local link to file: generated_symbols/world/entity/mob/breedable/villager/WanderTarget.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class WanderTarget(GeneratedModel):
    X: int | None = None
    Y: int | None = None
    Z: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::WanderTarget": {
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
