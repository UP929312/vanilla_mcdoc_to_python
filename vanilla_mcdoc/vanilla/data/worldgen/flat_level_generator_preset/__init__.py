"""Vanilla's data/worldgen/flat_level_generator_preset/ files"""
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer import FlatGeneratorLayer
from vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings
from vanilla_mcdoc.data.worldgen.world_preset.FlatGeneratorPreset import FlatGeneratorPreset

BOTTOMLESS_PIT = FlatGeneratorPreset(
    display='minecraft:feather',
    settings=FlatGeneratorSettings(
        biome='minecraft:plains',
        lakes=False,
        features=False,
        layers=[
            FlatGeneratorLayer(height=2, block='minecraft:cobblestone'),
            FlatGeneratorLayer(height=3, block='minecraft:dirt'),
            FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
        ],
        structure_overrides='minecraft:villages',
    ),
)

CLASSIC_FLAT = FlatGeneratorPreset(
    display='minecraft:grass_block',
    settings=FlatGeneratorSettings(
        biome='minecraft:plains',
        lakes=False,
        features=False,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=2, block='minecraft:dirt'),
            FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
        ],
        structure_overrides='minecraft:villages',
    ),
)

DESERT = FlatGeneratorPreset(
    display='minecraft:sand',
    settings=FlatGeneratorSettings(
        biome='minecraft:desert',
        lakes=False,
        features=True,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=3, block='minecraft:stone'),
            FlatGeneratorLayer(height=52, block='minecraft:sandstone'),
            FlatGeneratorLayer(height=8, block='minecraft:sand'),
        ],
        structure_overrides=['minecraft:desert_pyramids', 'minecraft:mineshafts', 'minecraft:strongholds', 'minecraft:villages'],
    ),
)

OVERWORLD = FlatGeneratorPreset(
    display='minecraft:short_grass',
    settings=FlatGeneratorSettings(
        biome='minecraft:plains',
        lakes=True,
        features=True,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=59, block='minecraft:stone'),
            FlatGeneratorLayer(height=3, block='minecraft:dirt'),
            FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
        ],
        structure_overrides=[
            'minecraft:mineshafts',
            'minecraft:pillager_outposts',
            'minecraft:ruined_portals',
            'minecraft:strongholds',
            'minecraft:villages',
        ],
    ),
)

REDSTONE_READY = FlatGeneratorPreset(
    display='minecraft:redstone',
    settings=FlatGeneratorSettings(
        biome='minecraft:desert',
        lakes=False,
        features=False,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=3, block='minecraft:stone'),
            FlatGeneratorLayer(height=116, block='minecraft:sandstone'),
        ],
        structure_overrides=[],
    ),
)

SNOWY_KINGDOM = FlatGeneratorPreset(
    display='minecraft:snow',
    settings=FlatGeneratorSettings(
        biome='minecraft:snowy_plains',
        lakes=False,
        features=False,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=59, block='minecraft:stone'),
            FlatGeneratorLayer(height=3, block='minecraft:dirt'),
            FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
            FlatGeneratorLayer(height=1, block='minecraft:snow'),
        ],
        structure_overrides=['minecraft:igloos', 'minecraft:villages'],
    ),
)

THE_VOID = FlatGeneratorPreset(
    display='minecraft:barrier',
    settings=FlatGeneratorSettings(
        biome='minecraft:the_void',
        lakes=False,
        features=True,
        layers=[FlatGeneratorLayer(height=1, block='minecraft:air')],
        structure_overrides=[],
    ),
)

TUNNELERS_DREAM = FlatGeneratorPreset(
    display='minecraft:stone',
    settings=FlatGeneratorSettings(
        biome='minecraft:windswept_hills',
        lakes=False,
        features=True,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=230, block='minecraft:stone'),
            FlatGeneratorLayer(height=5, block='minecraft:dirt'),
            FlatGeneratorLayer(height=1, block='minecraft:grass_block'),
        ],
        structure_overrides=['minecraft:mineshafts', 'minecraft:strongholds'],
    ),
)

WATER_WORLD = FlatGeneratorPreset(
    display='minecraft:water_bucket',
    settings=FlatGeneratorSettings(
        biome='minecraft:deep_ocean',
        lakes=False,
        features=False,
        layers=[
            FlatGeneratorLayer(height=1, block='minecraft:bedrock'),
            FlatGeneratorLayer(height=64, block='minecraft:deepslate'),
            FlatGeneratorLayer(height=5, block='minecraft:stone'),
            FlatGeneratorLayer(height=5, block='minecraft:dirt'),
            FlatGeneratorLayer(height=5, block='minecraft:gravel'),
            FlatGeneratorLayer(height=90, block='minecraft:water'),
        ],
        structure_overrides=['minecraft:ocean_monuments', 'minecraft:ocean_ruins', 'minecraft:shipwrecks'],
    ),
)
