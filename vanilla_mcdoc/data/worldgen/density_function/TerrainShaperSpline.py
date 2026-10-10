"""
Generated from symbols.json for ::java::data::worldgen::density_function::TerrainShaperSpline
Local link to file: vanilla_mcdoc/data/worldgen/density_function/TerrainShaperSpline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange
    from vanilla_mcdoc.data.worldgen.density_function.SplineType import SplineType


class TerrainShaperSpline(GeneratedModel):
    spline: SplineType
    min_value: NoiseRange
    max_value: NoiseRange
    continentalness: DensityFunctionRef
    erosion: DensityFunctionRef
    weirdness: DensityFunctionRef
