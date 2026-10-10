"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::Horse
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/Horse.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase import HorseBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.horse.HorseVariantAndMarkings import HorseVariantAndMarkings


class Horse(HorseBase):
    Variant: HorseVariantAndMarkings | None = None  # Variant of the horse. Stored as `baseColor | (markings << 8)`.
