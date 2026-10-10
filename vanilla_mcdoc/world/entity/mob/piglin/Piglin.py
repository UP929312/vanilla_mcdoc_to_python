"""
Generated from symbols.json for ::java::world::entity::mob::piglin::Piglin
Local link to file: vanilla_mcdoc/world/entity/mob/piglin/Piglin.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.piglin.PiglinBase import PiglinBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Piglin(PiglinBase):
    IsBaby: bool | None = None  # Whether it is a baby.
    CannotHunt: bool | None = None  # Whether it does not hunt hoglins.
    Inventory: Annotated[list[ItemStack], Field(min_length=0, max_length=8)] | None = None
