"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeature
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/PlacedFeature.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.ConfiguredFeatureRef import ConfiguredFeatureRef
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier import PlacementModifier


class PlacedFeature(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/placed_feature'

    feature: ConfiguredFeatureRef
    placement: list[PlacementModifier]
