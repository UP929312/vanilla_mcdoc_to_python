"""
Generated from symbols.json for ::java::data::worldgen::material_condition::BiomeCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/BiomeCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class BiomeCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    biome_is: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
