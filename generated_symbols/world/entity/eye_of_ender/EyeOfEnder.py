# Generated from symbols.json for ::java::world::entity::eye_of_ender::EyeOfEnder
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
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

