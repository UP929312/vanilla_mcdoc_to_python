"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::SurfaceRelativeThresholdFilter
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/SurfaceRelativeThresholdFilter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType


class SurfaceRelativeThresholdFilter(GeneratedModel):
    heightmap: HeightmapType
    min_inclusive: int | None = None
    max_inclusive: int | None = None
