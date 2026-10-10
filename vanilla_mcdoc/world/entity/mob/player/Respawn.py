"""
Generated from symbols.json for ::java::world::entity::mob::player::Respawn
Local link to file: vanilla_mcdoc/world/entity/mob/player/Respawn.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Respawn(GeneratedModel):
    pos: tuple[int, int, int]  # The block coordinates of the player's respawn point
    yaw: float  # The Y-rotation of the player's respawn point
    pitch: float  # The X-rotation of the player's respawn point
    forced: bool | None = None  # Whether the player must spawn at the respawn point.
    dimension: Annotated[str, IdSpec(registry='dimension')]  # Dimension of the player's respawn point.
