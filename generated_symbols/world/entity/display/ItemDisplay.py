# Generated from symbols.json for ::java::world::entity::display::ItemDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from generated_symbols.assets.model.ItemDisplayContext import ItemDisplayContext
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class ItemDisplay(DisplayBase):
    item: ItemStack | None = None  # Item stack to display.
    item_display: ItemDisplayContext | None = None  # Describes item model transform applied to item (as defined in the `display` section in model JSON). Defaults to `fixed`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::ItemDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::DisplayBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Item stack to display.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Describes item model transform applied to item (as defined in the `display` section in model JSON). Defaults to `fixed`.",
                "key": "item_display",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ItemDisplayContext"
                },
                "optional": True
            }
        ]
    }
}

