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
