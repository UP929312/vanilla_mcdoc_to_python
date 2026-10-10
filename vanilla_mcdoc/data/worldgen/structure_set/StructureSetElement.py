"""
Generated from symbols.json for ::java::data::worldgen::structure_set::StructureSetElement
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/StructureSetElement.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class StructureSetElement(GeneratedModel):
    structure: Annotated[str, IdSpec(registry='worldgen/structure')]
    weight: Annotated[int, Field(ge=1)]
