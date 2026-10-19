"""Vanilla's data/tags/worldgen/world_preset/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

EXTENDED = Tag(values=['#minecraft:normal', 'minecraft:debug_all_block_states'])

NORMAL = Tag(
    values=[
        'minecraft:normal',
        'minecraft:flat',
        'minecraft:large_biomes',
        'minecraft:amplified',
        'minecraft:single_biome_surface',
    ],
)
