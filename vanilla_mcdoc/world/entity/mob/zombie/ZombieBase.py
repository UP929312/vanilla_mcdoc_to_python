"""
Generated from symbols.json for ::java::world::entity::mob::zombie::ZombieBase
Local link to file: vanilla_mcdoc/world/entity/mob/zombie/ZombieBase.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.zombie.DrowningTracker import DrowningTracker
from vanilla_mcdoc.world.entity.mob.zombie.FreezingTracker import FreezingTracker


class ZombieBase(DrowningTracker, FreezingTracker, MobBase):
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
