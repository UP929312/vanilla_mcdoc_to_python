"""
Generated from symbols.json for ::java::world::entity::mob::creaking::Creaking
Local link to file: vanilla_mcdoc/world/entity/mob/creaking/Creaking.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Creaking(MobBase):
    home_pos: tuple[int, int, int] | None = None  # The creaking heart block that this is linked to.
