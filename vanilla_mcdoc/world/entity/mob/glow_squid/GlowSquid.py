"""
Generated from symbols.json for ::java::world::entity::mob::glow_squid::GlowSquid
Local link to file: vanilla_mcdoc/world/entity/mob/glow_squid/GlowSquid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class GlowSquid(AgeableMob, MobBase):
    DarkTicksRemaining: int | None = None  # Ticks that it will wait before glowing.
