"""
Generated from symbols.json for ::java::world::entity::mob::slime::SulfurCube
Local link to file: vanilla_mcdoc/world/entity/mob/slime/SulfurCube.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase
from vanilla_mcdoc.world.entity.mob.slime.CubeMob import CubeMob


class SulfurCube(AgeableMob, CubeMob, MobBase):
    pickup_timer: Annotated[int, Field(ge=0)] | None = None
    from_bucket: bool | None = None
    fuse: Annotated[int, Field(ge=-1)] | None = None  # `-1` represents "not ignited".
