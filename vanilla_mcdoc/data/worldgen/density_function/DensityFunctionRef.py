"""
Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunctionRef
Local link to file: vanilla_mcdoc/data/worldgen/density_function/DensityFunctionRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunction


type DensityFunctionRef = Annotated[str, IdSpec(registry='worldgen/density_function')] | DensityFunction
