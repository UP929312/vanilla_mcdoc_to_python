"""
Generated from symbols.json for ::java::world::entity::mob::Squid
Local link to file: vanilla_mcdoc/world/entity/mob/Squid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Squid(AgeableMob, MobBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::Squid": {
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::AgeableMob"
                }
            }
        ]
    }
}
