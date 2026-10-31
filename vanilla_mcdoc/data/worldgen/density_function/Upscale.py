"""
Generated from symbols.json for ::java::data::worldgen::density_function::Upscale
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Upscale.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.UpscaleAxis import UpscaleAxis


class Upscale(GeneratedModel):
    input: DensityFunctionRef
    x: UpscaleAxis
    y: UpscaleAxis
    z: UpscaleAxis
