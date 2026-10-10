"""
Generated from symbols.json for ::java::world::item::crossbow::Crossbow
Local link to file: vanilla_mcdoc/world/item/crossbow/Crossbow.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Crossbow(ItemBase):
    ChargedProjectiles: Annotated[list[ItemStack], Field(min_length=0, max_length=3)] | None = None  # Projectiles that are loaded.
    Charged: bool | None = None  # Whether the crossbow is charged.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::crossbow::Crossbow": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Projectiles that are loaded.",
                "key": "ChargedProjectiles",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::ItemStack"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the crossbow is charged.",
                "key": "Charged",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
