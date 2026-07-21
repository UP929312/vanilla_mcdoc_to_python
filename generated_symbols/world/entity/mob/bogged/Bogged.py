# Generated from symbols.json for ::java::world::entity::mob::bogged::Bogged
from dataclasses import dataclass
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Bogged(MobBase):
    sheared: bool | None = None  # Whether the mushrooms on this bogged have been sheared.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::bogged::Bogged": {
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
                "desc": "Whether the mushrooms on this bogged have been sheared.",
                "key": "sheared",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

