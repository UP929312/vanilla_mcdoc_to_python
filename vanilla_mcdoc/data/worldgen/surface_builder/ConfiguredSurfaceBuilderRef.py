"""
Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilderRef
Local link to file: vanilla_mcdoc/data/worldgen/surface_builder/ConfiguredSurfaceBuilderRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.surface_builder.ConfiguredSurfaceBuilder import ConfiguredSurfaceBuilder


type ConfiguredSurfaceBuilderRef = Annotated[str, IdSpec(registry='worldgen/configured_surface_builder')] | ConfiguredSurfaceBuilder
