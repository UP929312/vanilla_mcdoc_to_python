"""
Generated from symbols.json for ::java::data::worldgen::density_function::TwoArguments
Local link to file: vanilla_mcdoc/data/worldgen/density_function/TwoArguments.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class TwoArguments(GeneratedModel):
    left: DensityFunctionRef
    right: DensityFunctionRef
