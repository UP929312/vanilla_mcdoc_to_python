"""
Generated from symbols.json for ::java::world::entity::mob::piglin::PiglinBase
Local link to file: vanilla_mcdoc/world/entity/mob/piglin/PiglinBase.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class PiglinBase(MobBase):
    IsImmuneToZombification: bool | None = None  # Whether it will not transform to a zombified piglin when it is in the Overworld.
    TimeInOverworld: int | None = None  # Ticks it has been in the overworld.
