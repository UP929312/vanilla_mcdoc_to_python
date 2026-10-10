"""
Generated from symbols.json for ::java::data::worldgen::WeightListHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/WeightListHeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


class WeightListHeightProvider(GeneratedModel):
    distribution: NonEmptyWeightedList[HeightProvider]
