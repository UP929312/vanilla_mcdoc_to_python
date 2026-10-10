"""
Generated from symbols.json for ::java::util::GlobalPos
Local link to file: vanilla_mcdoc/util/GlobalPos.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class GlobalPos(GeneratedModel):
    pos: tuple[int, int, int]  # Coordinates of the location in [x, y, z]
    dimension: Annotated[str, IdSpec(registry='dimension')]  # Dimension of the location
