"""
Generated from symbols.json for ::java::util::game_event::ReceivingEvent
Local link to file: vanilla_mcdoc/util/game_event/ReceivingEvent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID


class ReceivingEvent(GeneratedModel):
    game_event: Annotated[str, IdSpec(registry='game_event')]
    distance: Annotated[float, Field(ge=0)]  # Distance in blocks to the source
    pos: tuple[float, float, float]  # Origin of the event
    source: MinecraftUUID | None = None  # UUID of the source entity of the event, if one exists
    projectile_owner: MinecraftUUID | None = None  # UUID of the owner of the projectile, if one exists
