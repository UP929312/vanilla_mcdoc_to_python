"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::HeightmapConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/HeightmapConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightmapType import HeightmapType


class HeightmapConfig(GeneratedModel):
    heightmap: HeightmapType
