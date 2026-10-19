"""Vanilla's data/dimension/ files"""
from vanilla_mcdoc.data.worldgen.dimension.Dimension import Dimension
from vanilla_mcdoc.data.worldgen.dimension.biome_source.BiomeSource import BiomeSourceMultiNoiseNether, BiomeSourceMultiNoiseOverworld, BiomeSourceTheEnd
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.ChunkGenerator import ChunkGeneratorNoise

OVERWORLD = Dimension(
    type='minecraft:overworld',
    generator=ChunkGeneratorNoise(
        settings='minecraft:overworld',
        biome_source=BiomeSourceMultiNoiseOverworld(type='minecraft:multi_noise', preset='minecraft:overworld'),
        type='minecraft:noise',
    ),
)

THE_END = Dimension(
    type='minecraft:the_end',
    generator=ChunkGeneratorNoise(
        settings='minecraft:end',
        biome_source=BiomeSourceTheEnd(type='minecraft:the_end'),
        type='minecraft:noise',
    ),
)

THE_NETHER = Dimension(
    type='minecraft:the_nether',
    generator=ChunkGeneratorNoise(
        settings='minecraft:nether',
        biome_source=BiomeSourceMultiNoiseNether(type='minecraft:multi_noise', preset='minecraft:nether'),
        type='minecraft:noise',
    ),
)
