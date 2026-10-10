"""
Generated from symbols.json for ::java::data::worldgen::density_function::InvervalSelect
Local link to file: vanilla_mcdoc/data/worldgen/density_function/InvervalSelect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class InvervalSelect(GeneratedModel):
    input: DensityFunctionRef
    thresholds: Annotated[list[NoiseRange], Field(min_length=1)]  # Must have exactly one fewer element than `functions`.
    functions: Annotated[list[DensityFunctionRef], Field(min_length=2)]  # Must have exactly one more element than `thresholds`.
