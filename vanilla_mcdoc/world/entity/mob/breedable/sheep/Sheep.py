"""
Generated from symbols.json for ::java::world::entity::mob::breedable::sheep::Sheep
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/sheep/Sheep.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.DyeColorByte import DyeColorByte


class Sheep(Breedable):
    Sheared: bool | None = None  # Whether it has been shorn.
    Color: DyeColorByte | None = None
