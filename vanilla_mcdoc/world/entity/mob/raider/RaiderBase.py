"""
Generated from symbols.json for ::java::world::entity::mob::raider::RaiderBase
Local link to file: vanilla_mcdoc/world/entity/mob/raider/RaiderBase.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class RaiderBase(MobBase):
    Patrolling: bool | None = None  # Whether the raider is patrolling.
    PatrolLeader: bool | None = None  # Whether the raider is leading the patrol.
    patrol_target: tuple[int, int, int] | None = None  # Where the raider is heading towards.
    CanJoinRaid: bool | None = None  # Whether the raider can join raids and count towards the progress bar.
    RaidId: int | None = None  # Id of the raid that the raider is in.
    Wave: Annotated[int, Field(ge=0, le=8)] | None = None  # Wave that the raider is in.
