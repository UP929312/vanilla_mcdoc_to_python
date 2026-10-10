"""
Generated from symbols.json for ::java::data::worldgen::carver::CanyonConfig
Local link to file: vanilla_mcdoc/data/worldgen/carver/CanyonConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.data.worldgen.carver.CarverConfigBase import CarverConfigBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider
    from vanilla_mcdoc.data.worldgen.carver.CanyonShape import CanyonShape


class CanyonConfig(CarverConfigBase):
    __resource_dir__: ClassVar[str] = 'worldgen/carver'

    vertical_rotation: FloatProvider[float] | float
    shape: CanyonShape
