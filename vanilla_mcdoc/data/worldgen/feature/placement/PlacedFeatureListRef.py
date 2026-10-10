"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacedFeatureListRef
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/PlacedFeatureListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature import PlacedFeature


type PlacedFeatureListRef = PlacedFeature | Annotated[str, IdSpec(registry='worldgen/placed_feature', tags='allowed')] | Annotated[list[Annotated[str, IdSpec(registry='worldgen/placed_feature')] | PlacedFeature], Field(min_length=1)]
