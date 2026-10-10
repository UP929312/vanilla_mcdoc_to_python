"""
Generated from symbols.json for ::java::world::entity::mob::slime::CubeMob
Local link to file: vanilla_mcdoc/world/entity/mob/slime/CubeMob.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CubeMob(GeneratedModel):
    Size: Annotated[int, Field(ge=0, le=126)] | None = None
    wasOnGround: bool | None = None  # Whether it is on the ground.
