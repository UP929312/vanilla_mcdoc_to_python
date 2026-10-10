"""
Generated from symbols.json for ::java::assets::texture_meta::TileScaling
Local link to file: vanilla_mcdoc/assets/texture_meta/TileScaling.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TileScaling(GeneratedModel):
    width: Annotated[int, Field(ge=1)]
    height: Annotated[int, Field(ge=1)]
