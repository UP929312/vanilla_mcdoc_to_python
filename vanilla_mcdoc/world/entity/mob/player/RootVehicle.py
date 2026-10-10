"""
Generated from symbols.json for ::java::world::entity::mob::player::RootVehicle
Local link to file: vanilla_mcdoc/world/entity/mob/player/RootVehicle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class RootVehicle(GeneratedModel):
    Attach: MinecraftUUID | None = None  # Ridden entity's UUID.
    Entity: AnyEntity | None = None  # The ridden entity.
