"""
Generated from symbols.json for ::java::data::worldgen::feature::CoralConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/CoralConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


class CoralConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    feature: PlacedFeatureRef
