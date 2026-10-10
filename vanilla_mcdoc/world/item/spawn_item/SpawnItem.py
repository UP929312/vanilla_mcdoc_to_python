"""
Generated from symbols.json for ::java::world::item::spawn_item::SpawnItem
Local link to file: vanilla_mcdoc/world/item/spawn_item/SpawnItem.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class SpawnItem(ItemBase):
    EntityTag: AnyEntity | None = None  # Data of the spawned entity.
