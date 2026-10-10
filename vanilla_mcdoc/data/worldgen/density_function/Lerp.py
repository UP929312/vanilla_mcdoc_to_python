"""
Generated from symbols.json for ::java::data::worldgen::density_function::Lerp
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Lerp.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Lerp(GeneratedModel):
    alpha: DensityFunctionRef
    first: DensityFunctionRef
    second: DensityFunctionRef
