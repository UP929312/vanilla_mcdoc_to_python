# Generated from symbols.json for ::java::world::entity::mob::ghast::Ghast
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.entity.mob.MobBase import MobBase


@dataclass(kw_only=True)
class Ghast(MobBase):
    ExplosionPower: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Explosion radius of fireballs that are shot from it.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::ghast::Ghast": {
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
                "desc": "Explosion radius of fireballs that are shot from it.",
                "key": "ExplosionPower",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

