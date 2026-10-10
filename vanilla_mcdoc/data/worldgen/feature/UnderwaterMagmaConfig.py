"""
Generated from symbols.json for ::java::data::worldgen::feature::UnderwaterMagmaConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/UnderwaterMagmaConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class UnderwaterMagmaConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    floor_search_range: Annotated[int, Field(ge=0, le=512)]
    placement_radius_around_floor: Annotated[int, Field(ge=0, le=64)]
    placement_probability_per_valid_position: Annotated[float, Field(ge=0, le=1)]
