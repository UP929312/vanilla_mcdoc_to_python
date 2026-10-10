"""
Generated from symbols.json for ::java::world::component::item::TeleportRandomlyConsumeEffect
Local link to file: vanilla_mcdoc/world/component/item/TeleportRandomlyConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TeleportRandomlyConsumeEffect(GeneratedModel):
    diameter: Annotated[float, Field(ge=1)] | None = None  # Defaults to 16.
    directional_particles: bool | None = None  # Whether to show a particle trail into the direction of teleportation.  Defaults to `true`.
