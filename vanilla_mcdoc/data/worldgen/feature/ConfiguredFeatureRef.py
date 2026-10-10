"""
Generated from symbols.json for ::java::data::worldgen::feature::ConfiguredFeatureRef
Local link to file: vanilla_mcdoc/data/worldgen/feature/ConfiguredFeatureRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.ConfiguredFeature import ConfiguredFeature


type ConfiguredFeatureRef = Annotated[str, IdSpec(registry='worldgen/feature')] | ConfiguredFeature
