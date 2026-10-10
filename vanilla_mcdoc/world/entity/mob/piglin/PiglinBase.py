"""
Generated from symbols.json for ::java::world::entity::mob::piglin::PiglinBase
Local link to file: vanilla_mcdoc/world/entity/mob/piglin/PiglinBase.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class PiglinBase(MobBase):
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zombified piglin when it is in the Overworld.
    TimeInOverworld: int | None = None  # Ticks it has been in the overworld.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::piglin::PiglinBase": {
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
                "desc": "Whether it will not transform to a zombified piglin when it is in the Overworld.",
                "key": "IsImmuneToZombification",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks it has been in the overworld.",
                "key": "TimeInOverworld",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
