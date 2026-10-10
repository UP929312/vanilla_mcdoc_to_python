"""
Generated from symbols.json for ::java::world::entity::eye_of_ender::EyeOfEnder
Local link to file: vanilla_mcdoc/world/entity/eye_of_ender/EyeOfEnder.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class EyeOfEnder(EntityBase):
    Item: ItemStack | None = None  # Item to render as.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::eye_of_ender::EyeOfEnder": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Item to render as.",
                "key": "Item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            }
        ]
    }
}
