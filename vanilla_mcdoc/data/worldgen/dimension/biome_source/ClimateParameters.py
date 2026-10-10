"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::ClimateParameters
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/ClimateParameters.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameter import ClimateParameter


class ClimateParameters(GeneratedModel):
    temperature: ClimateParameter
    humidity: ClimateParameter
    continentalness: ClimateParameter
    erosion: ClimateParameter
    weirdness: ClimateParameter
    depth: ClimateParameter
    offset: Annotated[float, Field(ge=0, le=1)]
