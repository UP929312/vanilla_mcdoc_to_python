"""
Generated from symbols.json for ::java::world::entity::mob::allay::Allay
Local link to file: vanilla_mcdoc/world/entity/mob/allay/Allay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.game_event.VibrationListener import VibrationListener
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Allay(MobBase):
    DuplicationCooldown: int | None = None  # Ticks until the allay can duplicate. This is set to 6000 game ticks (5 minutes) when the allay duplicates.
    Inventory: tuple[ItemStack] | None = None  # Items it has picked up. Note that the item given by the player is in the allay's `HandItems[0]` tag, not here.
    listener: VibrationListener | None = None  # Vibration game event listener.
