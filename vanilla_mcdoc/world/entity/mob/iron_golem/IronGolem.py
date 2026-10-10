"""
Generated from symbols.json for ::java::world::entity::mob::iron_golem::IronGolem
Local link to file: vanilla_mcdoc/world/entity/mob/iron_golem/IronGolem.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob


class IronGolem(MobBase, NeutralMob):
    PlayerCreated: bool | None = None  # Whether a player created it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::iron_golem::IronGolem": {
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::NeutralMob"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether a player created it.",
                "key": "PlayerCreated",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
