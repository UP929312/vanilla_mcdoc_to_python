"""
Generated from symbols.json for ::java::world::entity::mob::vex::Vex
Local link to file: vanilla_mcdoc/world/entity/mob/vex/Vex.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Vex(MobBase):
    bound_pos: tuple[int, int, int] | None = None  # Coordinates of the center of its wander bounds.
    life_ticks: int | None = None  # Ticks until it starts to die.
    owner: MinecraftUUID | None = None  # The owner of this vex.
