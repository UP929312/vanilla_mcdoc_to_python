"""
Generated from symbols.json for ::java::data::worldgen::structure_set::ConcentricRingsPlacement
Local link to file: vanilla_mcdoc/data/worldgen/structure_set/ConcentricRingsPlacement.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.worldgen.structure_set.SpreadingPlacementBase import SpreadingPlacementBase
from vanilla_mcdoc.minecraft_types import IdSpec


class ConcentricRingsPlacement(SpreadingPlacementBase):
    distance: Annotated[int, Field(ge=0, le=1023)]
    spread: Annotated[int, Field(ge=0, le=1023)]
    count: Annotated[int, Field(ge=1, le=4095)]
    preferred_biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
