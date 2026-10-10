"""
Generated from symbols.json for ::java::data::worldgen::feature::SimpleRandomSelectorConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SimpleRandomSelectorConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef import PlacedFeatureListRef


class SimpleRandomSelectorConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    features: PlacedFeatureListRef
