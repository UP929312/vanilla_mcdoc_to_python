"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Camel
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/Camel.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase import HorseBase


class Camel(HorseBase):
    IsSitting: bool | None = None  # Whether it is sitting.
    LastPoseTick: int | None = None  # The tick when it started changing its pose.
