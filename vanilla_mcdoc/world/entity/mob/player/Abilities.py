"""
Generated from symbols.json for ::java::world::entity::mob::player::Abilities
Local link to file: vanilla_mcdoc/world/entity/mob/player/Abilities.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class Abilities(GeneratedModel):
    walkSpeed: Annotated[float, Field(ge=0.1, le=0.1)] | None = None  # Speed that the player walks at.
    flySpeed: Annotated[float, Field(ge=0.05, le=0.05)] | None = None  # Speed that the player flies at.
    mayfly: bool | None = None  # Whether the player can fly.
    flying: bool | None = None  # Whether the player is flying.
    invulnerable: bool | None = None  # Whether the player can only take damage from the void.
    mayBuild: bool | None = None  # Whether the player may build.
    instabuild: bool | None = None  # Whether the player destroys blocks instantly.
