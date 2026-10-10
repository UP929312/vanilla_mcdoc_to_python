"""
Generated from symbols.json for ::java::data::worldgen::density_function::SplinePoint
Local link to file: vanilla_mcdoc/data/worldgen/density_function/SplinePoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSpline


class SplinePoint(GeneratedModel):
    location: float
    derivative: float
    value: CubicSpline
