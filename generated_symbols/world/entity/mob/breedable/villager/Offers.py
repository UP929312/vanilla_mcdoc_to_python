# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::Offers
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.villager.Recipe import Recipe


@dataclass(kw_only=True)
class Offers:
    Recipes: list[Recipe] | None = None  # Trades it has to offer.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::Offers": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Trades it has to offer.",
                "key": "Recipes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::breedable::villager::Recipe"
                    }
                },
                "optional": True
            }
        ]
    }
}

