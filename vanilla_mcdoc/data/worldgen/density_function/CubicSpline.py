"""
Generated from symbols.json for ::java::data::worldgen::density_function::CubicSpline
Local link to file: vanilla_mcdoc/data/worldgen/density_function/CubicSpline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from vanilla_mcdoc.data.worldgen.density_function.SplinePoint import SplinePoint


class CubicSplineStruct(GeneratedModel):
    coordinate: DensityFunctionRef
    points: list[SplinePoint]


type CubicSpline = float | CubicSplineStruct
