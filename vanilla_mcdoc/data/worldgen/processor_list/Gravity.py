"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Gravity
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/Gravity.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType


class Gravity(GeneratedModel):
    heightmap: HeightmapType
    offset: int
