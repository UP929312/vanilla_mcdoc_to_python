"""
Generated from symbols.json for ::java::world::entity::mob::raider::Ravager
Local link to file: vanilla_mcdoc/world/entity/mob/raider/Ravager.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.raider.RaiderBase import RaiderBase


class Ravager(RaiderBase):
    AttackTick: int | None = None  # Ticks until it can attack.
    RoarTick: int | None = None  # Ticks until it can roar.
    StunTick: int | None = None  # Ticks it is stunned for.
