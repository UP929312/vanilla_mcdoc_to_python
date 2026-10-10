"""
Generated from symbols.json for ::java::world::entity::ominous_item_spawner::OminousItemSpawner
Local link to file: vanilla_mcdoc/world/entity/ominous_item_spawner/OminousItemSpawner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class OminousItemSpawner(EntityBase):
    item: ItemStack | None = None
    spawn_item_after_ticks: int | None = None
