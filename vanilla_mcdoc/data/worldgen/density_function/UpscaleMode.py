"""
Generated from symbols.json for ::java::data::worldgen::density_function::UpscaleMode
Local link to file: vanilla_mcdoc/data/worldgen/density_function/UpscaleMode.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class UpscaleMode(StrEnum):
    NEARESTNEIGHBOR = "nearest_neighbor"
    INTERPOLATELINEAR = "interpolate_linear"
    INTERPOLATECOSINE = "interpolate_cosine"
    INTERPOLATECUBIC = "interpolate_cubic"
    BSPLINECUBIC = "b_spline_cubic"
