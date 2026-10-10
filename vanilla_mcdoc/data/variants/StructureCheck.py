"""
Generated from symbols.json for ::java::data::variants::StructureCheck
Local link to file: vanilla_mcdoc/data/variants/StructureCheck.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class StructureCheck(GeneratedModel):
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]]  # Checks if the entity is spawning in specific structures.
