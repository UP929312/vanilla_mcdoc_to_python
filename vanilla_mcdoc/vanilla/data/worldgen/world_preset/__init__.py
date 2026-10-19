"""Vanilla's data/worldgen/world_preset/ files"""
from vanilla_mcdoc.data.worldgen.dimension.Dimension import Dimension
from vanilla_mcdoc.data.worldgen.dimension.biome_source.BiomeSource import BiomeSourceFixed, BiomeSourceMultiNoiseNether, BiomeSourceMultiNoiseOverworld, BiomeSourceTheEnd
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGeneratorDebug, ChunkGeneratorFlat, ChunkGeneratorNoise
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer import FlatGeneratorLayer
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings
from vanilla_mcdoc.data.worldgen.world_preset.WorldPreset import WorldPreset

AMPLIFIED = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorNoise(
                settings='minecraft:amplified',
                biome_source=BiomeSourceMultiNoiseOverworld(type='minecraft:multi_noise', preset='minecraft:overworld'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)

DEBUG_ALL_BLOCK_STATES = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(type='minecraft:overworld', generator=ChunkGeneratorDebug(type='minecraft:debug')),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)

FLAT = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorFlat(
                settings=FlatGeneratorSettings(
                    biome='minecraft:plains',
                    lakes=False,
                    features=False,
                    layers=[
                        FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
                        FlatGeneratorLayer(height=2, block='minecraft:dirt'),
                        FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
                    ],
                    structure_overrides=['minecraft:strongholds', 'minecraft:villages'],
                ),
                type='minecraft:flat',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)

FLAT_ALL_DIMENSIONS = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorFlat(
                settings=FlatGeneratorSettings(
                    biome='minecraft:desert',
                    lakes=False,
                    features=False,
                    layers=[
                        FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
                        FlatGeneratorLayer(height=67, block='minecraft:sandstone'),
                    ],
                ),
                type='minecraft:flat',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorFlat(
                settings=FlatGeneratorSettings(
                    biome='minecraft:the_end',
                    lakes=False,
                    features=False,
                    layers=[
                        FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
                        FlatGeneratorLayer(height=3, block='minecraft:end_stone'),
                    ],
                ),
                type='minecraft:flat',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorFlat(
                settings=FlatGeneratorSettings(
                    biome='minecraft:basalt_deltas',
                    lakes=False,
                    features=False,
                    layers=[
                        FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
                        FlatGeneratorLayer(height=3, block='minecraft:basalt'),
                    ],
                ),
                type='minecraft:flat',
            ),
        ),
    },
)

LARGE_BIOMES = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorNoise(
                settings='minecraft:large_biomes',
                biome_source=BiomeSourceMultiNoiseOverworld(type='minecraft:multi_noise', preset='minecraft:overworld'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)

NORMAL = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorNoise(
                settings='minecraft:overworld',
                biome_source=BiomeSourceMultiNoiseOverworld(type='minecraft:multi_noise', preset='minecraft:overworld'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)

SINGLE_BIOME_SURFACE = WorldPreset(
    dimensions={
        'minecraft:overworld': Dimension(
            type='minecraft:overworld',
            generator=ChunkGeneratorNoise(
                settings='minecraft:overworld',
                biome_source=BiomeSourceFixed(biome='minecraft:plains', type='minecraft:fixed'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_end': Dimension(
            type='minecraft:the_end',
            generator=ChunkGeneratorNoise(
                settings='minecraft:end',
                biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
                type='minecraft:noise',
            ),
        ),
        'minecraft:the_nether': Dimension(
            type='minecraft:the_nether',
            generator=ChunkGeneratorNoise(
                settings='minecraft:nether',
                biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
                type='minecraft:noise',
            ),
        ),
    },
)
