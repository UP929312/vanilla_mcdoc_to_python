"""
Generated from symbols.json for ::java::data::worldgen::surface_builder::ConfiguredSurfaceBuilder
Local link to file: vanilla_mcdoc/data/worldgen/surface_builder/ConfiguredSurfaceBuilder.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class ConfigStruct(GeneratedModel):
    top_material: BlockState
    under_material: BlockState
    underwater_material: BlockState


class ConfiguredSurfaceBuilder(GeneratedModel):
    type: Annotated[str, IdSpec(registry='worldgen/surface_builder')]
    config: ConfigStruct
