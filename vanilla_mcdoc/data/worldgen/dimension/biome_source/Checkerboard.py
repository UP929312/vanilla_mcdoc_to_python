"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Checkerboard
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/Checkerboard.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Checkerboard(GeneratedModel):
    scale: Annotated[int, Field(ge=0, le=62)] | None = None
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
