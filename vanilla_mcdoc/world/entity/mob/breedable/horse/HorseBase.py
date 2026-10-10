"""
Generated from symbols.json for ::java::world::entity::mob::breedable::horse::HorseBase
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/horse/HorseBase.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import MinecraftUUID
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class HorseBase(Breedable):
    Bred: bool | None = None  # Unknown use. Remains `0` even if it was bred.
    EatingHaystack: bool | None = None  # Whether it is eating a haystack.
    Tame: bool | None = None  # Whether it has been tamed.
    Temper: Annotated[int, Field(ge=0, le=100)] | None = None  # Higher values make it easier to tame. Increases with feeding.
    Owner: MinecraftUUID | None = None  # Player who tamed it.
