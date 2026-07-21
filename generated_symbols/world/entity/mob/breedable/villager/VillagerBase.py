# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::VillagerBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.villager.Offers import Offers
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class VillagerBase:
    Inventory: Annotated[list[ItemStack], 'Length = 0-8 (both inclusive)'] | None = None  # Slots from 0 to 7.
    Offers: Offers | None = None  # Trade offers it has.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::VillagerBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Slots from 0 to 7.",
                "key": "Inventory",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 8
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Trade offers it has.",
                "key": "Offers",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::Offers"
                },
                "optional": True
            }
        ]
    }
}

