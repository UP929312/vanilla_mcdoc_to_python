"""
Generated from symbols.json for ::java::data::worldgen::dimension::Dimension
Local link to file: vanilla_mcdoc/data/worldgen/dimension/Dimension.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.dimension.DimensionTypeRef import DimensionTypeRef
    from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGenerator


class Dimension(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dimension'

    type: DimensionTypeRef
    generator: ChunkGenerator
