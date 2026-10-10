"""
Generated from symbols.json for ::java::data::worldgen::noise_settings::Aquifer
Local link to file: vanilla_mcdoc/data/worldgen/noise_settings/Aquifer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Aquifer(GeneratedModel):
    barrier: DensityFunctionRef
    fluid_level_floodedness: DensityFunctionRef
    fluid_level_spread: DensityFunctionRef
    lava: DensityFunctionRef
    exclusion: DensityFunctionRef
    surface_level: DensityFunctionRef
