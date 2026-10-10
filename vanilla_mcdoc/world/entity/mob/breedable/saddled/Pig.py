"""
Generated from symbols.json for ::java::world::entity::mob::breedable::saddled::Pig
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/saddled/Pig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.entity.mob.breedable.saddled.Saddled import Saddled


class Pig(Saddled):
    variant: Annotated[str, IdSpec(registry='pig_variant')] | None = None
    sound_variant: Annotated[str, IdSpec(registry='pig_sound_variant')] | None = None
