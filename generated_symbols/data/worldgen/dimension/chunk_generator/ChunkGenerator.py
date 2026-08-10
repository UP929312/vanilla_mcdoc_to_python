"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::ChunkGenerator
Local link to file: generated_symbols/data/worldgen/dimension/chunk_generator/ChunkGenerator.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.BiomeSource import BiomeSource
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings
    from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettingsRef import NoiseGeneratorSettingsRef


@dataclass(kw_only=True)
class ChunkGeneratorFlat:
    type: Literal['minecraft:flat']
    settings: FlatGeneratorSettings


@dataclass(kw_only=True)
class ChunkGeneratorNoise:
    type: Literal['minecraft:noise']
    settings: NoiseGeneratorSettingsRef
    biome_source: BiomeSource


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

