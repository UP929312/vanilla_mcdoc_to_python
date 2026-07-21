# Generated from symbols.json for ::java::world::entity::mob::slime::SulfurCube
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.world.entity.mob.AgeableMob import AgeableMob
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.slime.CubeMob import CubeMob


@dataclass(kw_only=True)
class SulfurCube(MobBase, AgeableMob, CubeMob):
    pickup_timer: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
    from_bucket: bool | None = None
    fuse: Annotated[int, 'Range | Min `-1` and above | inclusive'] | None = None  # `-1` represents "not ignited".


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::slime::SulfurCube": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::slime::CubeMob"
                }
            },
            {
                "kind": "pair",
                "key": "pickup_timer",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "from_bucket",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "`-1` represents \"not ignited\".",
                "key": "fuse",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": -1
                    }
                },
                "optional": True
            }
        ]
    }
}

