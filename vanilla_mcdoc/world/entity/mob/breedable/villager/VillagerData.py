"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::VillagerData
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/VillagerData.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class VillagerData(GeneratedModel):
    level: int | None = None  # Used for trading and badge rendering.
    profession: Annotated[str, IdSpec(registry='villager_profession')] | None = None
    type: Annotated[str, IdSpec(registry='villager_type')] | None = None
