"""
Generated from symbols.json for ::java::data::worldgen::density_function::Clamp
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Clamp.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class Clamp(GeneratedModel):
    input: DensityFunctionRef
    min: NoiseRange
    max: NoiseRange
