"""
Generated from symbols.json for ::java::world::entity::mob::dolphin::Dolphin
Local link to file: vanilla_mcdoc/world/entity/mob/dolphin/Dolphin.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Dolphin(AgeableMob, MobBase):
    GotFish: bool | None = None  # Whether it has gotten fish from a player.
    Moistness: int | None = None  # Moistness level of the dolphin. Set to 2400 when the dolphin is in water or rain, otherwise decreases by 1 every tick. The dolphin takes damage when level is at 0 or below.
