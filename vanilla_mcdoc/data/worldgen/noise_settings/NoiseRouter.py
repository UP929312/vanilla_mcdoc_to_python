"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseRouter
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/NoiseRouter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class NoiseRouter(GeneratedModel):
    temperature: DensityFunctionRef
    vegetation: DensityFunctionRef
    continents: DensityFunctionRef
    erosion: DensityFunctionRef
    depth: DensityFunctionRef
    ridges: DensityFunctionRef
    chunk_surface_level: DensityFunctionRef
    final_density: DensityFunctionRef
