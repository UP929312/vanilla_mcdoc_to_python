# Generated from symbols.json for ::java::world::entity::mob::tadpole::Tadpole
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Tadpole(MobBase):
    Age: int | None = None  # Age of it in ticks. When greater than or equal to 24000, it grows into a frog.
    FromBucket: bool | None = None  # If it was released from a bucket.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::tadpole::Tadpole": {
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
                "desc": "Age of it in ticks. When greater than or equal to 24000, it grows into a frog.",
                "key": "Age",
                "type": {
                    "kind": "int"
                },
                "optional": True
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

