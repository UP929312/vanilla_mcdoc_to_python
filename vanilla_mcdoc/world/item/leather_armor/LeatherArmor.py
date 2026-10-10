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
