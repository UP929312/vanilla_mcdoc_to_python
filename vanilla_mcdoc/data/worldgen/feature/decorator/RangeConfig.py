"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::RangeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/RangeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider


class RangeConfig(GeneratedModel):
    height: HeightProvider
