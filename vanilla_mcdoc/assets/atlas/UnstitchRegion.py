"""
Generated from symbols.json for ::java::assets::atlas::UnstitchRegion
Local link to file: vanilla_mcdoc/assets/atlas/UnstitchRegion.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class UnstitchRegion(GeneratedModel):
    sprite: Annotated[str, IdSpec(registry='texture', definition=True)]
    x: float
    y: float
    width: float
    height: float
