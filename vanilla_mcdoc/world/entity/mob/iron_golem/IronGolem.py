"""
Generated from symbols.json for ::java::world::entity::mob::iron_golem::IronGolem
Local link to file: vanilla_mcdoc/world/entity/mob/iron_golem/IronGolem.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob


class IronGolem(MobBase, NeutralMob):
    PlayerCreated: bool | None = None  # Whether a player created it.
