# Generated from symbols.json for ::java::world::entity::mob::breedable::rabbit::Rabbit
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.rabbit.RabbitType import RabbitType


@dataclass(kw_only=True)
class Rabbit(Breedable):
    RabbitType: RabbitType | None = None
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

