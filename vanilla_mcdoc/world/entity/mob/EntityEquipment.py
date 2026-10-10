"""
Generated from symbols.json for ::java::world::entity::mob::EntityEquipment
Local link to file: vanilla_mcdoc/world/entity/mob/EntityEquipment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.util.slot.EquipmentSlot import EquipmentSlot
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


type EntityEquipment = dict[EquipmentSlot, ItemStack]
