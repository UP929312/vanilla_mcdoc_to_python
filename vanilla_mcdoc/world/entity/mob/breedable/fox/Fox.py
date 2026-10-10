"""
Generated from symbols.json for ::java::world::entity::mob::breedable::fox::Fox
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/fox/Fox.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.FoxType import FoxType


class Fox(Breedable):
    Trusted: list[MinecraftUUID] | None = None  # List of trusted players.
    Sleeping: bool | None = None  # Whether it is sleeping.
    Type: FoxType | None = None  # The type of fox.
    Sitting: bool | None = None  # Whether it is sitting.
    Crouching: bool | None = None  # Whether it is crouching.
