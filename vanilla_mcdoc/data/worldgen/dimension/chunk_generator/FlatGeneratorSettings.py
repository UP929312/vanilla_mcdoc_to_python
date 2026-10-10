"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::FlatGeneratorSettings
Local link to file: vanilla_mcdoc/data/worldgen/dimension/chunk_generator/FlatGeneratorSettings.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer import FlatGeneratorLayer


class FlatGeneratorSettings(GeneratedModel):
    biome: Annotated[str, IdSpec(registry='worldgen/biome')] | None = None
    lakes: bool | None = None
    features: bool | None = None
    layers: list[FlatGeneratorLayer]
    structure_overrides: list[Annotated[str, IdSpec(registry='worldgen/structure_set')]] | Annotated[str, IdSpec(registry='worldgen/structure_set', tags='allowed')] | None = None
