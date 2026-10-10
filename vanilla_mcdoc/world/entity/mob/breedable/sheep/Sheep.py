"""
Generated from symbols.json for ::java::world::entity::mob::breedable::sheep::Sheep
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/sheep/Sheep.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.DyeColorByte import DyeColorByte


class Sheep(Breedable):
    Sheared: bool | None = None  # Whether it has been shorn.
    Color: DyeColorByte | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::sheep::Sheep": {
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
                "desc": "Whether it has been shorn.",
                "key": "Sheared",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::DyeColorByte"
                },
                "optional": True
            }
        ]
    }
}
