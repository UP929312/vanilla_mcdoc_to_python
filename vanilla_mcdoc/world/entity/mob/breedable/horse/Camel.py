"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Camel
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/Camel.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase import HorseBase


class Camel(HorseBase):
    IsSitting: bool | None = None  # Whether it is sitting.
    LastPoseTick: int | None = None  # The tick when it started changing its pose.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::horse::Camel": {
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
                "desc": "Whether it is sitting.",
                "key": "IsSitting",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The tick when it started changing its pose.",
                "key": "LastPoseTick",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}
