# Generated from symbols.json for ::java::world::entity::mob::snow_golem::SnowGolem
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class SnowGolem(MobBase):
    Pumpkin: bool | None = None  # Whether it has a pumpkin.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::snow_golem::SnowGolem": {
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
                "desc": "Whether it has a pumpkin.",
                "key": "Pumpkin",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

