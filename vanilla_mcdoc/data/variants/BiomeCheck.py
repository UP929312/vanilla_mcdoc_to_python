"""
Generated from symbols.json for ::java::data::variants::BiomeCheck
Local link to file: vanilla_mcdoc/data/variants/BiomeCheck.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class BiomeCheck(GeneratedModel):
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]]  # Checks if the entity is spawning in specific biomes.
