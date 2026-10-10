"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeatureRef
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/PlacedFeatureRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature


type PlacedFeatureRef = PlacedFeature | Annotated[str, IdSpec(registry='worldgen/placed_feature')]
