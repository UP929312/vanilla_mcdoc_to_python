"""
Generated from symbols.json for ::java::data::worldgen::material_condition::YAboveCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/YAboveCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchor


class YAboveCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    anchor: VerticalAnchor
    surface_depth_multiplier: Annotated[int, Field(ge=-20, le=20)]
    add_stone_depth: bool
