# Generated from symbols.json for ::java::world::entity::mob::raider::Pillager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Pillager(RaiderBase):
    Inventory: Annotated[list[ItemStack], 'Length = 0-5 (both inclusive)'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::raider::Pillager": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::raider::RaiderBase"
                }
            },
            {
                "kind": "pair",
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
                        "max": 5
                    }
                },
                "optional": True
            }
        ]
    }
}

