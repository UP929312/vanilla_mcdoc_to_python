"""
Generated from symbols.json for ::java::world::entity::display::Brightness
Local link to file: vanilla_mcdoc/world/entity/display/Brightness.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class Brightness(GeneratedModel):
    sky: Annotated[int, Field(ge=0, le=15)]  # Value of skylight.
    block: Annotated[int, Field(ge=0, le=15)]  # Value of block light.
