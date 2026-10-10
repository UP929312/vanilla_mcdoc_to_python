"""
Generated from symbols.json for ::java::data::worldgen::material_condition::StoneDepthCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/StoneDepthCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CaveSurface import CaveSurface


class StoneDepthCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    offset: int
    surface_type: CaveSurface
    add_surface_depth: bool
    secondary_depth_range: int
