"""
Generated from symbols.json for ::java::data::worldgen::material_condition::WaterCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/WaterCondition.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class WaterCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    offset: int
    surface_depth_multiplier: Annotated[int, Field(ge=-20, le=20)]
    add_stone_depth: bool
