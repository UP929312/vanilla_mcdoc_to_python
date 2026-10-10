"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::SkeletonHorse
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/SkeletonHorse.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase import HorseBase


class SkeletonHorse(HorseBase):
    SkeletonTrap: bool | None = None  # Whether it was spawned by a trap.
    SkeletonTrapTime: int | None = None  # Ticks it has existed.
