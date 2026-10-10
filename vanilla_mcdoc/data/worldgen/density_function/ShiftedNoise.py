"""
Generated from symbols.json for ::java::data::worldgen::density_function::ShiftedNoise
Local link to file: vanilla_mcdoc/data/worldgen/density_function/ShiftedNoise.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.density_function.Noise import Noise

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class ShiftedNoise(Noise):
    shift_x: DensityFunctionRef
    shift_y: DensityFunctionRef
    shift_z: DensityFunctionRef
