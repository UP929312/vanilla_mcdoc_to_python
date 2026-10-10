"""
Generated from symbols.json for ::java::world::item::leather_armor::LeatherArmor
Local link to file: vanilla_mcdoc/world/item/leather_armor/LeatherArmor.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.leather_armor.ColorDisplay import ColorDisplay


class LeatherArmor(ItemBase):
    display: ColorDisplay | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::leather_armor::LeatherArmor": {
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
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::leather_armor::ColorDisplay"
                },
                "optional": True
            }
        ]
    }
}
