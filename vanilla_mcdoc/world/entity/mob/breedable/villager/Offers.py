"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::Offers
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/Offers.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.villager.Recipe import Recipe


class Offers(GeneratedModel):
    Recipes: list[Recipe] | None = None  # Trades it has to offer.
