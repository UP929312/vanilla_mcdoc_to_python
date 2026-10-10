"""
Generated from symbols.json for ::java::world::entity::mob::zombie::Zombie
Local link to file: vanilla_mcdoc/world/entity/mob/zombie/Zombie.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Zombie(MobBase):
    IsBaby: bool | None = None  # Whether it is a baby.
    CanBreakDoors: bool | None = None  # Whether it can break doors.
    DrownedConversionTime: int | None = None  # Ticks until it converts.
    InWaterTime: int | None = None  # Ticks it has been in the water.
    FrostbiteConversionTime: int | None = None  # Ticks until it converts.
    FreezingTime: int | None = None  # Ticks it has been in the powdered snow.
