"""
Generated from symbols.json for ::java::world::entity::mob::breedable::cow::Cow
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/cow/Cow.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Cow(Breedable):
    variant: Annotated[str, IdSpec(registry='cow_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='cow_sound_variant')] | None = None
