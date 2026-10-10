"""
Generated from symbols.json for ::java::data::worldgen::density_function::RangeChoice
Local link to file: vanilla_mcdoc/data/worldgen/density_function/RangeChoice.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class RangeChoice(GeneratedModel):
    input: DensityFunctionRef
    min_inclusive: NoiseRange
    max_exclusive: NoiseRange
    when_in_range: DensityFunctionRef
    when_out_of_range: DensityFunctionRef
