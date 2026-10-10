"""
Generated from symbols.json for ::java::data::worldgen::feature::WeightedRandomFeatureConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/WeightedRandomFeatureConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from vanilla_mcdoc.util.WeightedList import WeightedList


class WeightedRandomFeatureConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: WeightedList[PlacedFeatureRef]
