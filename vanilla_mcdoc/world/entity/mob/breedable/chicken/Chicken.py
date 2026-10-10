"""
Generated from symbols.json for ::java::world::entity::mob::breedable::chicken::Chicken
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/chicken/Chicken.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Chicken(Breedable):
    IsChickenJockey: bool | None = None  # Whether it is from a chicken jockey. If true it will despawn and will drop more experience.
    EggLayTime: int | None = None  # Time until it lays another egg.
    variant: Annotated[str, IdSpec(registry='chicken_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='chicken_sound_variant')] | None = None
