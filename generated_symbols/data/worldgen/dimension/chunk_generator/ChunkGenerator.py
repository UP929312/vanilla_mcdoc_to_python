"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::ChunkGenerator
Local link to file: generated_symbols/data/worldgen/dimension/chunk_generator/ChunkGenerator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.dimension.chunk_generator.Flat import Flat
from generated_symbols.data.worldgen.dimension.chunk_generator.Noise import Noise


@dataclass(kw_only=True)
class ChunkGeneratorFlat(Flat):
    type: Literal['minecraft:flat'] = 'minecraft:flat'


@dataclass(kw_only=True)
class ChunkGeneratorNoise(Noise):
    type: Literal['minecraft:noise'] = 'minecraft:noise'


type ChunkGenerator = ChunkGeneratorFlat | ChunkGeneratorNoise


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::chunk_generator::ChunkGenerator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/chunk_generator"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:chunk_generator"
                }
            }
        ]
    }
}

