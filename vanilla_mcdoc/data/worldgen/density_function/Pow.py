"""
Generated from symbols.json for ::java::data::worldgen::density_function::Pow
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Pow.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class Pow(GeneratedModel):
    base: DensityFunctionRef
    exponent: DensityFunctionRef
