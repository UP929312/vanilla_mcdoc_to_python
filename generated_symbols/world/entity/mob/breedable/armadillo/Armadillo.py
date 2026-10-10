"""
Generated from symbols.json for ::java::world::entity::mob::breedable::armadillo::Armadillo
Local link to file: generated_symbols/world/entity/mob/breedable/armadillo/Armadillo.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.armadillo.ArmadilloState import ArmadilloState


class Armadillo(Breedable):
    state: ArmadilloState | None = None
    scute_time: Annotated[int, Field(ge=0)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::armadillo::Armadillo": {
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
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::armadillo::ArmadilloState"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "scute_time",
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

