"""
Generated from symbols.json for ::java::data::worldgen::carver::CaveConfig
Local link to file: vanilla_mcdoc/data/worldgen/carver/CaveConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider


class CaveConfig(CarverConfigBase):
    __resource_dir__: ClassVar[str] = 'worldgen/carver'

    count: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]
    thickness: FloatProvider[Annotated[float, Field(ge=0)]] | Annotated[float, Field(ge=0)]
    weird_thickness_bias: bool | None = None  # Defaults to `false`.
    room_vertical_radius_multiplier: FloatProvider[float] | float
    horizontal_radius_multiplier: FloatProvider[float] | float
    vertical_radius_multiplier: FloatProvider[float] | float
    start_vertical_radius_multiplier: FloatProvider[float] | float | None = None  # Defaults to constant 1.0
    floor_level: FloatProvider[Annotated[float, Field(ge=-1, le=1)]] | Annotated[float, Field(ge=-1, le=1)]
