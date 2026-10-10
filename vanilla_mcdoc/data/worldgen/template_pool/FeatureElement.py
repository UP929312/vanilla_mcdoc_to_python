"""
Generated from symbols.json for ::java::data::worldgen::template_pool::FeatureElement
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/FeatureElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.template_pool.ElementBase import ElementBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef


class FeatureElement(ElementBase):
    feature: PlacedFeatureRef
