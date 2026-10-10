"""
Generated from symbols.json for ::java::data::worldgen::density_function::DistanceToPoint
Local link to file: vanilla_mcdoc/data/worldgen/density_function/DistanceToPoint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.DistanceMetric import DistanceMetric


class DistanceToPoint(GeneratedModel):
    point: tuple[int, int, int]
    metric: DistanceMetric
