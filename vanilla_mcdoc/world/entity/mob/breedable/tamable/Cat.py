"""
Generated from symbols.json for ::java::world::entity::mob::breedable::tamable::Cat
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/tamable/Cat.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable import Tamable

if TYPE_CHECKING:
    from vanilla_mcdoc.util.DyeColorByte import DyeColorByte


class Cat(Tamable):
    CollarColor: DyeColorByte | None = None  # Collar color, present for stray cats. Defaults to 14 (red).
    variant: Annotated[str, IdSpec(registry='cat_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cat_sound_variant')] | None = None
