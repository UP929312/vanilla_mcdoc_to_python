# Generated from symbols.json for ::java::world::entity::mob::zoglin::Zoglin
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Zoglin(MobBase):
    IsBaby: bool | None = None  # Whether it is a baby.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::zoglin::Zoglin": {
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
                "desc": "Whether it is a baby.",
                "key": "IsBaby",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

