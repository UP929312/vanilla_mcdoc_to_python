"""
Generated from symbols.json for ::java::data::worldgen::world_preset::FlatGeneratorPreset
Local link to file: vanilla_mcdoc/data/worldgen/world_preset/FlatGeneratorPreset.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings


class FlatGeneratorPreset(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/flat_level_generator_preset'

    display: Annotated[str, IdSpec(registry='item', exclude=('air',))]
    settings: FlatGeneratorSettings
