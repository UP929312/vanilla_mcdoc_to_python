"""
Generated from symbols.json for ::java::world::entity::mob::wither::Wither
Local link to file: vanilla_mcdoc/world/entity/mob/wither/Wither.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Wither(MobBase):
    Invul: int | None = None  # Ticks it is invulnerable for.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::wither::Wither": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks it is invulnerable for.",
                "key": "Invul",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
