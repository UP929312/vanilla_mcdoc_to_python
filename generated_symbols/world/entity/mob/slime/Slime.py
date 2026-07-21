# Generated from symbols.json for ::java::world::entity::mob::slime::Slime
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.slime.CubeMob import CubeMob


@dataclass(kw_only=True)
class Slime(MobBase, CubeMob):
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

