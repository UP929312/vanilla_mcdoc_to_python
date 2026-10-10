"""
Generated from symbols.json for ::java::data::worldgen::density_function::FindTopSurface
Local link to file: vanilla_mcdoc/data/worldgen/density_function/FindTopSurface.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class FindTopSurface(GeneratedModel):
    density: DensityFunctionRef
    upper_bound: DensityFunctionRef
    lower_bound: Annotated[int, Field(ge=-4064, le=4062)]
    cell_height: Annotated[int, Field(ge=1)]
