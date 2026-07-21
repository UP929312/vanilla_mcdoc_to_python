# Generated from symbols.json for ::java::world::entity::mob::Squid
from dataclasses import dataclass
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Squid(MobBase, AgeableMob):
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

