# Generated from symbols.json for ::java::world::entity::mob::breedable::horse::SkeletonHorse
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.horse.HorseBase import HorseBase


@dataclass(kw_only=True)
class SkeletonHorse(HorseBase):
    SkeletonTrap: bool | None = None  # Whether it was spawned by a trap.
    SkeletonTrapTime: int | None = None  # Ticks it has existed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::SkeletonHorse": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::horse::HorseBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it was spawned by a trap.",
                "key": "SkeletonTrap",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks it has existed.",
                "key": "SkeletonTrapTime",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

