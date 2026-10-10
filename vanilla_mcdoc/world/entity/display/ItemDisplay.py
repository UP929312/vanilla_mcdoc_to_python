"""
Generated from symbols.json for ::java::world::entity::display::ItemDisplay
Local link to file: vanilla_mcdoc/world/entity/display/ItemDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ItemDisplayContext import ItemDisplayContext
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ItemDisplay(DisplayBase):
    item: ItemStack | None = None  # Item stack to display.
    item_display: ItemDisplayContext | None = None  # Describes item model transform applied to item (as defined in the `display` section in model JSON). Defaults to `fixed`.
