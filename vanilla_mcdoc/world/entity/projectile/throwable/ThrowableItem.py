"""
Generated from symbols.json for ::java::world::entity::projectile::throwable::ThrowableItem
Local link to file: vanilla_mcdoc/world/entity/projectile/throwable/ThrowableItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.projectile.throwable.Throwable import Throwable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class ThrowableItem(Throwable):
    Item: ItemStack | None = None  # Item representation of the projectile.
