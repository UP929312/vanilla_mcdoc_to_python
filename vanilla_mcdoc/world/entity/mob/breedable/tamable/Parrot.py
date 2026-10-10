"""
Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Parrot
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/tamable/Parrot.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.tamable.ParrotVariantInt import ParrotVariantInt


class Parrot(Tamable):
    Variant: ParrotVariantInt | None = None
