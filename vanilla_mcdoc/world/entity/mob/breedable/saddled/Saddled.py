"""
Generated from symbols.json for ::java::world::entity::mob::breedable::saddled::Saddled
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/saddled/Saddled.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.saddled.ItemBasedSteering import ItemBasedSteering


class Saddled(Breedable):
    item_based_steering: ItemBasedSteering | None = None
