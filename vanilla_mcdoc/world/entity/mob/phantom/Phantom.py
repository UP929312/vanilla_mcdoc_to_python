"""
Generated from symbols.json for ::java::world::entity::mob::phantom::Phantom
Local link to file: vanilla_mcdoc/world/entity/mob/phantom/Phantom.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Phantom(MobBase):
    anchor_pos: tuple[int, int, int] | None = None  # Approximate circle coordinates.
    size: Annotated[int, Field(ge=0, le=64)] | None = None
