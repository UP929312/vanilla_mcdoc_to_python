"""
Generated from symbols.json for ::java::world::entity::mob::breedable::rabbit::Rabbit
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/rabbit/Rabbit.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.rabbit.RabbitType import RabbitType


class Rabbit(Breedable):
    RabbitType_: RabbitType | None = Field(default=None, alias='RabbitType')
    MoreCarrotTicks: int | None = None  # Ticks down once a carrot crop is eaten


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::rabbit::Rabbit": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::Breedable"
                }
            },
            {
                "kind": "pair",
                "key": "RabbitType",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::rabbit::RabbitType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks down once a carrot crop is eaten",
                "key": "MoreCarrotTicks",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
