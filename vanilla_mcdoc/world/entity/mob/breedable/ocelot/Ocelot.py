"""
Generated from symbols.json for ::java::world::entity::mob::breedable::ocelot::Ocelot
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/ocelot/Ocelot.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Ocelot(Breedable):
    Trusting: bool | None = None  # Whether it trusts players.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::ocelot::Ocelot": {
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
                "desc": "Whether it trusts players.",
                "key": "Trusting",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
