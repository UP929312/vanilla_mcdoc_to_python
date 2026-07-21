# Generated from symbols.json for ::java::world::entity::mob::fish::Fish
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Fish(MobBase):
    FromBucket: bool | None = None  # If it was released from a bucket.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::fish::Fish": {
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
                "desc": "If it was released from a bucket.",
                "key": "FromBucket",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

