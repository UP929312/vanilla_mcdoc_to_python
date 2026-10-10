"""
Generated from symbols.json for ::java::data::worldgen::density_function::Noise
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Noise.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef


class Noise(GeneratedModel):
    noise: NoiseParametersRef
    xz_scale: float
    y_scale: float
    shift_x: DensityFunctionRef | None = None  # Defaults to constant 0.
    shift_y: DensityFunctionRef | None = None  # Defaults to constant 0.
    shift_z: DensityFunctionRef | None = None  # Defaults to constant 0.
