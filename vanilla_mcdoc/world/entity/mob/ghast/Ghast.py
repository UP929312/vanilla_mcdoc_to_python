"""
Generated from symbols.json for ::java::world::entity::mob::ghast::Ghast
Local link to file: vanilla_mcdoc/world/entity/mob/ghast/Ghast.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Ghast(MobBase):
    ExplosionPower: Annotated[int, Field(ge=0)] | None = None  # Explosion radius of fireballs that are shot from it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::ghast::Ghast": {
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
                "desc": "Explosion radius of fireballs that are shot from it.",
                "key": "ExplosionPower",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}
