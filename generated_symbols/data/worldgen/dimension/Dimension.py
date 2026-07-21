# Generated from symbols.json for ::java::data::worldgen::dimension::Dimension
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.DimensionTypeRef import DimensionTypeRef
    from generated_symbols.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGenerator


@dataclass(kw_only=True)
class Dimension:
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

