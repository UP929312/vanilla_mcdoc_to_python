"""
Generated from symbols.json for ::java::world::entity::mob::slime::Slime
Local link to file: vanilla_mcdoc/world/entity/mob/slime/Slime.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.slime.CubeMob import CubeMob


class Slime(CubeMob, MobBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::slime::Slime": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::slime::CubeMob"
                }
            }
        ]
    }
}
