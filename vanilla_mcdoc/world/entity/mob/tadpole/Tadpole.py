"""
Generated from symbols.json for ::java::world::entity::mob::tadpole::Tadpole
Local link to file: vanilla_mcdoc/world/entity/mob/tadpole/Tadpole.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Tadpole(MobBase):
    Age: int | None = None  # Age of it in ticks. When greater than or equal to 24000, it grows into a frog.
    FromBucket: bool | None = None  # If it was released from a bucket.
