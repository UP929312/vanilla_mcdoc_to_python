# Generated from symbols.json for ::java::world::entity::mob::bat::Bat
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Bat(MobBase):
    BatFlags: bool | None = None  # Whether it is upside down.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::bat::Bat": {
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
                "desc": "Whether it is upside down.",
                "key": "BatFlags",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

