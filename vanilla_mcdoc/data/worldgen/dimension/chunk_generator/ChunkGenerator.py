"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::ChunkGenerator
Local link to file: vanilla_mcdoc/data/worldgen/dimension/chunk_generator/ChunkGenerator.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Flat import Flat
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Noise import Noise


class ChunkGeneratorFlat(Flat):
    type: Literal['minecraft:flat', 'flat'] = 'minecraft:flat'


class ChunkGeneratorNoise(Noise):
    type: Literal['minecraft:noise', 'noise'] = 'minecraft:noise'


type ChunkGenerator = Annotated[
    ChunkGeneratorFlat | ChunkGeneratorNoise,
    Field(discriminator='type'),
]


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
