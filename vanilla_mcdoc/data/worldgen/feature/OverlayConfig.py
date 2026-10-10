"""
Generated from symbols.json for ::java::data::worldgen::feature::OverlayConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/OverlayConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef


class OverlayConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: PlacedFeatureListRef  # The features to generate, in order.  All features are placed regardless of individual placement success.
