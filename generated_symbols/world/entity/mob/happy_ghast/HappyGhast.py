# Generated from symbols.json for ::java::world::entity::mob::happy_ghast::HappyGhast
from dataclasses import dataclass
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class HappyGhast(MobBase, AgeableMob):
    still_timeout: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::happy_ghast::HappyGhast": {
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
                    "path": "::java::world::entity::mob::AgeableMob"
                }
            },
            {
                "kind": "pair",
                "key": "still_timeout",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

