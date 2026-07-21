# Generated from symbols.json for ::java::world::entity::mob::breedable::sheep::Sheep
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from generated_symbols.util.DyeColorByte import DyeColorByte


@dataclass(kw_only=True)
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

