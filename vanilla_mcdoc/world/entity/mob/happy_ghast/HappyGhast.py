"""
Generated from symbols.json for ::java::world::entity::mob::happy_ghast::HappyGhast
Local link to file: vanilla_mcdoc/world/entity/mob/happy_ghast/HappyGhast.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class HappyGhast(AgeableMob, MobBase):
    still_timeout: int | None = None
