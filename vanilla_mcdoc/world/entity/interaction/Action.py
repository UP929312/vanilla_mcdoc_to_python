"""
Generated from symbols.json for ::java::world::entity::interaction::Action
Local link to file: vanilla_mcdoc/world/entity/interaction/Action.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftUUID


class Action(GeneratedModel):
    player: MinecraftUUID | None = None
    timestamp: Annotated[int, Field(ge=0)] | None = None  # Game tick of when the event occured.
