# Generated from symbols.json for ::java::world::entity::mob::breedable::hoglin::Hoglin
from dataclasses import dataclass
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


@dataclass(kw_only=True)
class Hoglin(Breedable):
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zoglin when it is in the Overword.
    CannotBeHunted: bool | None = None  # Whether it cannot be hunted by piglins
    TimeInOverworld: int | None = None  # The number of ticks it has been in the overworld.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::hoglin::Hoglin": {
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
                "desc": "Whether it will not transform to a zoglin when it is in the Overword.",
                "key": "IsImmuneToZombification",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it cannot be hunted by piglins",
                "key": "CannotBeHunted",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The number of ticks it has been in the overworld.",
                "key": "TimeInOverworld",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

