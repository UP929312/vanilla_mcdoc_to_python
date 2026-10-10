"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CaveSurface
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/CaveSurface.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.base import GeneratedModel


class CaveSurface(GeneratedModel):
    surface: Literal['floor'] | Literal['ceiling']
    floor_to_ceiling_search_range: int
