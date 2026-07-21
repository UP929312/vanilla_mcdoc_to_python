# Generated from symbols.json for ::java::world::entity::mob::iron_golem::IronGolem
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob


@dataclass(kw_only=True)
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

