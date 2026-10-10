"""
Generated from symbols.json for ::java::world::entity::mob::fish::Pufferfish
Local link to file: vanilla_mcdoc/world/entity/mob/fish/Pufferfish.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.world.entity.mob.fish.Fish import Fish

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.fish.PuffState import PuffState


class Pufferfish(Fish):
    PuffState_: PuffState | None = Field(default=None, alias='PuffState')  # How puffed it is.
