"""
Generated from symbols.json for ::java::data::worldgen::density_function::TilingMode
Local link to file: vanilla_mcdoc/data/worldgen/density_function/TilingMode.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class TilingMode(StrEnum):
    CLAMPTOEDGE = "clamp_to_edge"
    REPEAT = "repeat"
    MIRROREDREPEAT = "mirrored_repeat"
