"""
Generated from symbols.json for ::java::world::entity::mob::raider::Pillager
Local link to file: generated_symbols/world/entity/mob/raider/Pillager.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


class Pillager(RaiderBase):
    Inventory: Annotated[list[ItemStack], Field(min_length=0, max_length=5)] | None = None


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
