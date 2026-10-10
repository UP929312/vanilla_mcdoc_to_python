"""
Generated from symbols.json for ::java::data::worldgen::density_function::Spline
Local link to file: vanilla_mcdoc/data/worldgen/density_function/Spline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.CubicSpline import CubicSpline


class Spline(GeneratedModel):
    spline: CubicSpline
