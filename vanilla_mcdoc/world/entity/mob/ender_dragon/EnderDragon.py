"""
Generated from symbols.json for ::java::world::entity::mob::ender_dragon::EnderDragon
Local link to file: vanilla_mcdoc/world/entity/mob/ender_dragon/EnderDragon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.ender_dragon.DragonPhase import DragonPhase


class EnderDragon(MobBase):
    DragonPhase_: DragonPhase | None = Field(default=None, alias='DragonPhase')  # The dragon's current state.
    DragonDeathTime: int | None = None  # Number of ticks the dragon has been dead for, or `0` when alive. At `150`, the dragon begins spawning experience orbs every 5 ticks (first drop at 155). Removes dragon at values `200` and higher.
    sitting_damage_received: float | None = None  # The amount of damage the dragon has received while perched. When this value is `50` or higher, it is reset to `0` and the dragon ends its perch.
