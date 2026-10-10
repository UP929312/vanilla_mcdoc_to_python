"""
Generated from symbols.json for ::java::world::entity::mob::breedable::mooshroom::Mooshroom
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/mooshroom/Mooshroom.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.MooshroomType import MooshroomType
    from vanilla_mcdoc.world.component.item.SuspiciousStewEffect import SuspiciousStewEffect


class Mooshroom(Breedable):
    Type: MooshroomType | None = None
    stew_effects: list[SuspiciousStewEffect] | None = None
