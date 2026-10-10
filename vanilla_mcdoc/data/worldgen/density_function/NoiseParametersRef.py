"""
Generated from symbols.json for ::java::data::worldgen::density_function::NoiseParametersRef
Local link to file: vanilla_mcdoc/data/worldgen/density_function/NoiseParametersRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters


type NoiseParametersRef = Annotated[str, IdSpec(registry='worldgen/noise')] | NoiseParameters
