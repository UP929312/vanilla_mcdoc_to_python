"""
Generated from symbols.json for ::java::data::worldgen::density_function::DomainWarp
Local link to file: vanilla_mcdoc/data/worldgen/density_function/DomainWarp.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef


class DomainWarp(GeneratedModel):
    input: DensityFunctionRef
    offset_x: DensityFunctionRef | None = None  # Defaults to constant 0.  At least one of the offsets must be specified.
    offset_y: DensityFunctionRef | None = None  # Defaults to constant 0.  At least one of the offsets must be specified.
    offset_z: DensityFunctionRef | None = None  # Defaults to constant 0.  At least one of the offsets must be specified.
