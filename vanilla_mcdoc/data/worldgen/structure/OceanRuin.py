"""
Generated from symbols.json for ::java::data::worldgen::structure::OceanRuin
Local link to file: vanilla_mcdoc/data/worldgen/structure/OceanRuin.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.BiomeTemperature import BiomeTemperature


class OceanRuin(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    biome_temp: BiomeTemperature
    large_probability: Annotated[float, Field(ge=0, le=1)]
    cluster_probability: Annotated[float, Field(ge=0, le=1)]
