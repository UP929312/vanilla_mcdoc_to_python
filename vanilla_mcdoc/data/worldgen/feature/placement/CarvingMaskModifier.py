"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::CarvingMaskModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/CarvingMaskModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CarveStep import CarveStep


class CarvingMaskModifier(GeneratedModel):
    step: CarveStep
