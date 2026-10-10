"""
Generated from symbols.json for ::java::world::entity::mob::player::PlayerEquipment
Local link to file: vanilla_mcdoc/world/entity/mob/player/PlayerEquipment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.player.PlayerEquipmentSlot import PlayerEquipmentSlot
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


type PlayerEquipment = dict[PlayerEquipmentSlot, ItemStack]
