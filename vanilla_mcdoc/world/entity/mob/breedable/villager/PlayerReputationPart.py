"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::PlayerReputationPart
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/PlayerReputationPart.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.villager.ReputationPart import ReputationPart


class PlayerReputationPart(GeneratedModel):
    Type: ReputationPart | None = None
    Value: Annotated[int, Field(ge=5, le=100)] | Literal[20] | Annotated[int, Field(ge=5, le=200)] | Annotated[int, Field(ge=1, le=25)] | None = None
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.
