"""
Generated from symbols.json for ::java::data::worldgen::dimension::Dimension
Local link to file: generated_symbols/data/worldgen/dimension/Dimension.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.DimensionTypeRef import DimensionTypeRef
    from generated_symbols.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGenerator


class Dimension(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dimension'

    type: DimensionTypeRef
    generator: ChunkGenerator


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::Dimension": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::DimensionTypeRef"
                }
            },
            {
                "kind": "pair",
                "key": "generator",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::chunk_generator::ChunkGenerator"
                }
            }
        ]
    }
}
