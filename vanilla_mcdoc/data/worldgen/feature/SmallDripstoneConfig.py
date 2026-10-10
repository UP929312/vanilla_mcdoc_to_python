"""
Generated from symbols.json for ::java::data::worldgen::feature::SmallDripstoneConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SmallDripstoneConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class SmallDripstoneConfig(GeneratedModel):
    max_placements: Annotated[int, Field(ge=0, le=100)] | None = None
    empty_space_search_radius: Annotated[int, Field(ge=0, le=20)] | None = None
    max_offset_from_origin: Annotated[int, Field(ge=0, le=20)] | None = None
    chance_of_taller_dripstone: Annotated[float, Field(ge=0, le=1)] | None = None
