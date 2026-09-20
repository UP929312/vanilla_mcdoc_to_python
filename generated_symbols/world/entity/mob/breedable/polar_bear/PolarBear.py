"""
Generated from symbols.json for ::java::world::entity::mob::breedable::polar_bear::PolarBear
Local link to file: generated_symbols/world/entity/mob/breedable/polar_bear/PolarBear.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable


class PolarBear(Breedable, NeutralMob):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::polar_bear::PolarBear": {
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::NeutralMob"
                }
            }
        ]
    }
}

