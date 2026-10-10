"""
Generated from symbols.json for ::java::world::entity::mob::creeper::Creeper
Local link to file: vanilla_mcdoc/world/entity/mob/creeper/Creeper.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Creeper(MobBase):
    powered: bool | None = None  # Whether it is being struck by lightning.
    ExplosionRadius: int | None = None  # Radius of the explosion.
    Fuse: int | None = None  # Ticks until it explodes.
    ignited: bool | None = None  # Whether it was lit with flint and steel.
