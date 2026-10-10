"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::CarvingMaskConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/CarvingMaskConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CarveStep import CarveStep


class CarvingMaskConfig(GeneratedModel):
    step: CarveStep
