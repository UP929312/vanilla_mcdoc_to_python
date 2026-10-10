"""
Generated from symbols.json for ::java::data::worldgen::carver::CanyonShape
Local link to file: vanilla_mcdoc/data/worldgen/carver/CanyonShape.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class CanyonShape(GeneratedModel):
    distance_factor: FloatProvider[float] | float
    thickness: FloatProvider[float] | float
    width_smoothness: Annotated[int, Field(ge=0)]
    horizontal_radius_factor: FloatProvider[float] | float
    vertical_radius_default_factor: float
    vertical_radius_center_factor: float
    y_scale: FloatProvider[float] | float
