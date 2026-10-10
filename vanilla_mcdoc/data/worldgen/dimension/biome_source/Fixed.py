"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Fixed
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/Fixed.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Fixed(GeneratedModel):
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]
