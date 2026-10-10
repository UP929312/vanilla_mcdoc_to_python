"""
Generated from symbols.json for ::java::data::worldgen::feature::SequenceConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SequenceConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef


class SequenceConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: PlacedFeatureListRef  # The features to generate, in order.  If any feature in the list is not placed, the following features will also be skipped.
