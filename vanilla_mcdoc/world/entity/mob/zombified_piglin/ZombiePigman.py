"""
Generated from symbols.json for ::java::world::entity::mob::zombified_piglin::ZombiePigman
Local link to file: vanilla_mcdoc/world/entity/mob/zombified_piglin/ZombiePigman.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.minecraft_types import MinecraftUUIDString
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.NeutralMob import NeutralMob


class ZombiePigman(MobBase, NeutralMob):
    IsBaby: bool | None = None  # Whether it is a baby.
    HurtBy: MinecraftUUIDString | None = None  # Last player to hit a zombie pigman in this zombie pigman's detection range.
