"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::VillagerBase
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/VillagerBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.villager.Offers import Offers
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class VillagerBase(GeneratedModel):
    Inventory: Annotated[list[ItemStack], Field(min_length=0, max_length=8)] | None = None  # Slots from 0 to 7.
    Offers_: Offers | None = Field(default=None, alias='Offers')  # Trade offers it has.
