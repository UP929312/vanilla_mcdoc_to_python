"""
Generated from symbols.json for ::java::world::entity::mob::breedable::Breedable
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/Breedable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.AgeableMob import AgeableMob
from vanilla_mcdoc.world.entity.mob.MobBase import MobBase


class Breedable(AgeableMob, MobBase):
    InLove: Annotated[int, Field(ge=0)] | None = None  # Ticks until it stops searching for a mate.
    LoveCause: MinecraftUUID | None = None  # Player that caused this mob to breed.
